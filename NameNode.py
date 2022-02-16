import grpc
import time
import os

import NameNode_pb2
import NameNode_pb2_grpc

import DataNode_pb2
import DataNode_pb2_grpc

from concurrent import futures

import sqlite3
import json
import queue
import numpy as np
import setting
import random
import pickle


class nameNodeServicer(NameNode_pb2_grpc.NameNodeServicer):
    def __init__(self, connection):
        print("\033[1;37;42m"+"server activated"+"\033[0m ")

        
        self.Clients = {}
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.createUserDB()
        self.createDataNodeDB()
        self.createFileDB()
        self.createLockDB()
        self.fileTree = {}
        self.pos = {}
        self.prepos = {}
        self.dataNodeOnline = {}
        self.loadFileTree()
        self.blocksWaitForWrite = {}
        #self.dropTableFile()


    def loadFileTree(self):
        with open('fileStructure.json', 'r') as f:
            self.fileTree = json.load(f)
        
    
    def saveFileTree(self):
         with open('fileStructure.json', 'w') as f:
            json.dump(self.fileTree, f)

    
    def createUserDB(self):
        sql = '''CREATE TABLE IF NOT EXISTS USER(   UID INTEGER PRIMARY KEY,
                                                    UNAME TEXT,
                                                    PASSWORD TEXT);'''
        self.cursor.execute(sql)
        self.connection.commit()

    def createDataNodeDB(self):
        sql = '''CREATE TABLE IF NOT EXISTS DATANODE( NODEID INTEGER PRIMARY KEY,
                                                      NODENAME TEXT,
                                                      SPACE INTEGER);'''
        self.cursor.execute(sql)
        self.connection.commit()

    def dropTableFile(self):
        sql = "DROP TABLE FILE;"
        self.cursor.execute(sql)
        self.connection.commit()

    def createFileDB(self):
        sql = '''CREATE TABLE IF NOT EXISTS FILE(   FID INTEGER,
                                                    FNAME TEXT,
                                                    FSIZE INTEGER,
                                                    CHECKSUM TEXT,
                                                    PATH TEXT,
                                                    OWNER TEXT,
                                                    SHARE TEXT,
                                                    LASTUPDATE NOT NULL DEFAULT (datetime('now','localtime')),
                                                    ISREPLICA TEXT,
                                                    DATANODE TEXT,
                                                    PRIMARY KEY(FID));'''
        self.cursor.execute(sql)
        self.connection.commit()
    
    def createLockDB(self):
        sql = '''CREATE TABLE IF NOT EXISTS LOCK(   FID INTEGER PRIMARY KEY,
                                                    FNAME TEXT,
                                                    PATH TEXT,
                                                    OWNER TEXT,
                                                    SHARE TEXT,
                                                    STATUS TEXT);'''
        self.cursor.execute(sql)
        self.connection.commit()


    def walk(self, walkSequence, user):
        subTree = self.fileTree["/"]
        for target in walkSequence:
            subTree = subTree[target]

        self.Clients[user][1]= subTree["."]
        self.pos[user] = subTree

    def changeDirectory(self, link, user):
        if link == "":
            self.pos[user] = self.pos[user]
            return 

        if(link[0] == "."):
            self.pos[user] = self.pos[user]
            return 
        if(link[:2] == ".."):
            walkSequence = link.split("/")[:-1]
            self.walk(walkSequence, user)
            return 
        
        if link[-1] == "/":
            link = link[:-1]
      
        walkSequence = link.split("/")[1:]
        self.walk(walkSequence, user) 


    def setDataNodeSpace(self):
        # for i in(len):
        sql = "UPDATE DATANODE SET SPACE = SPACE + (?) WHERE NODENAME = ?;"
        self.cursor.execute(sql, (spaceToChange, nodename))
        self.connection.commit()


    def allocateBlocks(self, fileSize):   
        nodelist = list(self.dataNodeOnline.keys())
        datanode1, datanode2 = random.choices(nodelist, k = 2)

        self.dataNodeOnline[datanode1] -= 2
        self.dataNodeOnline[datanode2] -= 1

        return [datanode1, datanode1, datanode2]
        

    def insertMetaFile(self, fileSize, fileName, to, checksum, user, howTo, giveTo, share):
        
        self.prepos[user] = self.pos[user]
        self.changeDirectory(to, user)
        pwd = self.Clients[user][1]


        sql = '''INSERT INTO LOCK(FNAME, PATH, OWNER, SHARE, STATUS)  VALUES(?,?,?,?,?);'''
        self.cursor.execute(sql, (fileName, pwd, self.Clients[user][0], share, "unlock"))
        self.connection.commit()



        sql = '''INSERT INTO FILE(FNAME, FSIZE, CHECKSUM, PATH, OWNER, SHARE, ISREPLICA, DATANODE)
                                    VALUES(?,?,?,?,?,?,?,?);'''
                        

        self.cursor.execute(sql, (fileName, fileSize, checksum, pwd, self.Clients[user][0], share,
                                    "NO", howTo[0]))
        self.cursor.execute(sql, (fileName, fileSize, checksum, pwd, self.Clients[user][0], share,
                                    "YES", howTo[1]))
        self.cursor.execute(sql, (fileName, fileSize, checksum, pwd, self.Clients[user][0], share,
                                    "YES", howTo[2]))    
        self.connection.commit()
        
        sql = '''SELECT * FROM FILE WHERE FNAME=? AND PATH=? AND OWNER=?;'''
        result = self.cursor.execute(sql, (fileName, pwd, self.Clients[user][0]))

        fileID = []
        for line in result.fetchall():
            fileID.append(line[0])

        self.pos[user]["file"] = {fileName:fileID}
        self.pos[user] = self.prepos[user] 
        self.saveFileTree()
        return fileID

    def listFiles(self, at, user):
        
        self.prepos[user] = self.pos[user]
        self.changeDirectory(at, user)
        pwd = self.Clients[user][1]


        sql = '''SELECT * FROM FILE WHERE PATH=? AND ISREPLICA = ?;'''
        result = self.cursor.execute(sql, (pwd,"NO"))
        fileList = result.fetchall()

        lsInfo = {}
        fileInfo = {}
        for idx,line in enumerate(fileList):
            fileInfo[idx] = line
        
        lsInfo["file"] = fileInfo
        
        folderInfo = {}
        for key, value in self.pos[user].items():
            if key != "file" and key != "." and key != "..":
                folderInfo[key]=""
        
        lsInfo["folder"] = folderInfo        

        self.pos[user] = self.prepos[user] 
        self.saveFileTree()
        return lsInfo



    def findMetaFile(self, fileName, to, user):
        self.prepos[user] = self.pos[user]
        self.changeDirectory(to, user)
        pwd = self.Clients[user][1]

        sql = '''SELECT * FROM FILE WHERE FNAME=? AND PATH=? AND OWNER=?;'''

        result = self.cursor.execute(sql, (fileName, pwd, self.Clients[user][0]))

        lines = result.fetchall()
        if lines[0][5] != self.Clients[user][0]:
            if lines[0][6] != True:
                return None

        searchDict = {}
        for FID, _, _, CHECKSUM, _, _, _, _, ISREPLICA, DATANODE in lines:
            if DATANODE not in searchDict:
                searchDict[DATANODE] = []
            searchDict[DATANODE].append([FID, CHECKSUM, ISREPLICA])

        self.pos[user] = self.prepos[user] 
        return searchDict

    def findMetaFileGlobal(self, fileName, at, user):
        self.prepos[user] = self.pos[user]

        if at[-1] == "/":
            at = at[:-1]

        
        sql = '''SELECT * FROM FILE WHERE FNAME=? AND PATH=? AND OWNER=?;'''
        #sql = '''SELECT * FROM FILE WHERE FNAME=? AND OWNER=?;'''
        result = self.cursor.execute(sql, (fileName, at, self.Clients[user][0]))

        lines = result.fetchall()

        if lines[0][5] != self.Clients[user][0]:
            if lines[0][6] != True:
                return None

        searchDict = {}
        for FID, _, _, _, _, _, _, _, _, DATANODE in lines:
            if DATANODE not in searchDict:
                searchDict[DATANODE] = []
            searchDict[DATANODE].append([FID])



        self.pos[user] = self.prepos[user] 
        return searchDict

    def setLock(self, fileName, at, user, status):

        if at[-1] == "/":
            at = at[:-1]

        sql = '''SELECT * FROM LOCK WHERE FNAME=? AND PATH=?;'''
        result = self.cursor.execute(sql, (fileName, at))
        lines = result.fetchall()
        
        if len(lines) == 0:
            return "Can't Find The File"

        # if not the owner of the file
        if lines[0][3] != self.Clients[user][0]:
            if lines[0][4] != "YES":
                return "Can't Access File Because You Are Not The Owner Of The File And The File Is Not Shared"
        
        if lines[0][5] == "lock" and status == "lock":
            return "The File Is Currently Locked By Other One"
        
        if lines[0][5] == "unlock" and status == "unlock":
            return "The File Lock Has Already Been Unlocked"
        
        sql = '''UPDATE LOCK SET STATUS = ? WHERE FNAME=? AND PATH=? AND OWNER=?;'''
        result = self.cursor.execute(sql, (status, fileName, at, self.Clients[user][0]))
        self.connection.commit()

        if status == "lock":
            return "You Can Access To The File Safely"
        else:
            return "You Have Successfully Released The File Lock"

    def removeMetaFileGlobal(self, fileName, at, user):

        if at[-1] == "/":
            at = at[:-1]

        sql = '''DELETE FROM FILE WHERE FNAME=? AND PATH=? AND OWNER=?;'''
        
        result = self.cursor.execute(sql, (fileName, at, self.Clients[user][0]))
        self.connection.commit()


        self.prepos[user] = self.pos[user]
        self.changeDirectory(at, user)

        del self.pos[user]["file"][fileName]
        self.pos[user] = self.prepos[user] 
        self.saveFileTree()

        return "Meta File Already Removed"


    def chooseUploadDataNode(self, uploadDataNode = 0):
        port = str(9000 + uploadDataNode)
        self.uploadDataNode = uploadDataNode
        self.channelToUploadDataNode = grpc.insecure_channel(f'localhost:{port}')
        self.stubForUploadDataNode = DataNode_pb2_grpc.DataNodeStub(self.channelToUploadDataNode)


    def checkDataNodeStatus(self):
        try:
            reply = self.stubForUploadDataNode.heartbeat(DataNode_pb2.msg(msg = "Are you ok?"))
            if reply.msg == "i'm alive":
                return True
        except grpc._channel._InactiveRpcError:
            return False

    


    ### rpc service for client###
    def checkNameNodeStatus(self, request, context):
        return NameNode_pb2.msg(msg = "i'm very ok")

    def bindClient(self, request, context):
        username = request.username
        password = request.password

        sql = "SELECT * FROM USER WHERE UNAME = ? AND PASSWORD = ?;"
        result = self.cursor.execute(sql,(username, password))
        
        if result.fetchone() is not None:
            self.Clients[context.peer()] = [username, "/"]

            print(f'''Client \033[1;37;44m{username}\033[0m logged in,\
                    IP Address \033[1;37;42m{context.peer()}\033[0m''')
            return NameNode_pb2.msg(msg = "you are allowed to access")
        else:
            return NameNode_pb2.msg(msg = "user not exist")
    
    def register(self, request, context):
        username = request.username
        password = request.password
        sql = "SELECT * FROM USER WHERE UNAME = ?;"
        result = self.cursor.execute(sql,(username,))
       
        if result.fetchone() is None:
            sql = "INSERT INTO USER(UNAME, PASSWORD) VALUES( ?, ?);"
            self.cursor.execute(sql, (username, password))
            self.connection.commit()
            return NameNode_pb2.msg(msg = "register success")
        else:
            return NameNode_pb2.msg(msg = "user already exists")

    def pwd(self, request, context):
        msg = f"{self.Clients[context.peer()][0]}@"\
                + f"{context.peer()}"\
                + f":{self.Clients[context.peer()][1]}$"
        return NameNode_pb2.msg(msg = msg)

    def mkdir(self, request, context):
        folderName = request.msg
        user = context.peer()
        if folderName not in self.pos[user]:
            self.pos[user][folderName] = {".":self.Clients[user][1]+f"/{folderName}", ".." : self.Clients[user][1]}
            self.saveFileTree()
            return NameNode_pb2.msg(msg = "")
        else:
            return NameNode_pb2.msg(msg = "directory already exists")
    
    def cd(self, request, context):
        link = request.msg
        self.changeDirectory(link, context.peer())
        return NameNode_pb2.msg(msg = "")
    
    def download(self, request, context):
        fileName = request.fileName
        to = request.to
        reply = self.findMetaFile(fileName, to, context.peer())

        if reply == None:
            return NameNode_pb2.instructions(allow = False, giveTo = "", chunks = 0, howTo = "File Not Found")
        else:
            return NameNode_pb2.instructions(allow = True, giveTo = "", chunks = 0, howTo = json.dumps(reply))
            

    def upload(self, request, context):
        fileSize = request.fileSize
        fileName = request.fileName
        to = request.to
        checksum = request.checksum
        share = "YES" if request.share == True else "NO"

        howTo = self.allocateBlocks(fileSize)
        allow = True
        chunks = 1
        giveTo = howTo[0]

        fileList = self.insertMetaFile(fileSize, fileName, to, checksum, context.peer(), howTo, giveTo, share)

        instructionDict = {}
        for datanode in howTo:
            instructionDict[datanode] = []

        for datanode, fileID in zip(howTo, fileList):
            instructionDict[datanode].append(fileID)
        howToString = json.dumps(instructionDict)
 
        return NameNode_pb2.instructions(allow = True, giveTo = giveTo, chunks = 1, howTo = howToString)

    def error(self, request, context):

        sql = '''DELETE FROM FILE WHERE FID = ?;'''

        for key, value in json.loads(request.msg).items():
            for fileID in value:
                self.cursor.execute(sql, (fileID,))
                self.connection.commit()
        return NameNode_pb2.msg(msg = "error handled, don't worry")

    def ls(self, request, context):
        
        at = request.msg
        msg = json.dumps(self.listFiles(at,context.peer()))
        return NameNode_pb2.msg(msg = msg)

    def delete(self, request, context):

        fileName = request.fileName
        at = request.to

        fileDict = self.findMetaFileGlobal(fileName, at, context.peer())

        for datanode, replicas in fileDict.items():
            replicastr = json.dumps(replicas)
            self.chooseUploadDataNode(int(datanode[-1]))
            if self.checkDataNodeStatus() == True:
                reply = self.stubForUploadDataNode.remove(DataNode_pb2.msg(msg = replicastr))

        msg = self.removeMetaFileGlobal(fileName, at, context.peer())

        if msg == "Meta File Already Removed":
            return NameNode_pb2.msg(msg = "successfully removed")
        return NameNode_pb2.msg(msg = "Some error occured during deletion")
        
    def readfile(self, request, context):
        fileName = request.fileName
        at = request.to
        msg = self.setLock(fileName, at, context.peer(), "lock")
        return NameNode_pb2.msg(msg = msg)

    def releasefile(self, request, context):
        fileName = request.fileName
        at = request.to
        msg = self.setLock(fileName, at, context.peer(), "unlock")
        return NameNode_pb2.msg(msg = msg)

    def cp(self, request, context):

        filename = request.filename
        current = request.current
        to = request.to

        self.prepos[context.peer()] = self.pos[context.peer()]

        if current[-1] == "/":
            current = current[:-1]
        
        sql = '''SELECT * FROM FILE WHERE FNAME=? AND PATH=? AND OWNER=?;'''
        #sql = '''SELECT * FROM FILE WHERE FNAME=? AND OWNER=?;'''
        result = self.cursor.execute(sql, (filename, current, self.Clients[context.peer()][0]))

        lines = result.fetchall()

        for A, B, C, D, E, F, G, H, I, J in lines:
            sql = '''INSERT INTO FILE(FNAME, FSIZE, CHECKSUM, PATH, OWNER, SHARE, ISREPLICA, DATANODE)
                                    VALUES(?,?,?,?,?,?,?,?);'''
            E = to
            self.cursor.execute(sql, (B, C, D, E, F, G, I, J))
            self.connection.commit()

        return NameNode_pb2.msg(msg = "File Copied To"+to)




    ### rpc service for datanode###
    def join(self, request, context):
        nodename = request.nodeName
        space = request.space

        
        self.dataNodeOnline[nodename] = space

        print(f'''DataNode \033[1;37;44m{nodename}\033[0m joined in,\
                        IP Address \033[1;37;42m{context.peer()}\033[0m''')
        
        sql = "SELECT * FROM DATANODE WHERE NODENAME = ?;"
        result = self.cursor.execute(sql,(nodename,))

        if result.fetchone() is None:
            sql = "INSERT INTO DATANODE(NODENAME, SPACE) VALUES( ?, ?);"
            self.cursor.execute(sql, (nodename, space))
            self.connection.commit()
            return NameNode_pb2.msg(msg = "welcome, my new friend!")
        else:
            sql = "UPDATE DATANODE SET SPACE = ? WHERE NODENAME = ?;"
            self.cursor.execute(sql, (space, nodename))
            self.connection.commit()
            return NameNode_pb2.msg(msg = "welcome, my old friend!")



if __name__=="__main__":
    con = sqlite3.connect("meta.db", check_same_thread=False)

    servicer = nameNodeServicer(con)
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))

    NameNode_pb2_grpc.add_NameNodeServicer_to_server(servicer, server)

    server.add_insecure_port(f'[::]:8001')
    server.start()
    server.wait_for_termination()