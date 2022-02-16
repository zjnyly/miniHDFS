import grpc
import time
import os

import NameNode_pb2
import NameNode_pb2_grpc

import DataNode_pb2
import DataNode_pb2_grpc

from concurrent import futures

import json

import setting

class dataNodeServicer(DataNode_pb2_grpc.DataNodeServicer):
    def __init__(self, nodeName = None):
        self.nodeName = nodeName
        self.loadMetaData()
        self.join()
        self.basePath = f"./DataNodeSpace/{self.nodeName}/"
        print("\033[1;37;42m"+"DataNode Activated"+"\033[0m ")
    
    def saveMetaData(self):
        path = f"./DataNodeSpace/{self.nodeName}/meta.json"
        with open(path, 'w') as f:
            json.dump(self.space, f)

    def loadMetaData(self):
        path = f"./DataNodeSpace/{self.nodeName}/meta.json"
        with open(path, 'r') as f:
            self.space = json.load(f)

    def chooseNameNode(self, nameNode = 0):
        port=str(8000+nameNode)
        self.nameNode=nameNode
        self.channelToNameNode=grpc.insecure_channel(f'localhost:{port}')
        self.stubForNameNode=NameNode_pb2_grpc.NameNodeStub(self.channelToNameNode)
		
    def checkNameNodeStatus(self):
        try:
            reply = self.stubForNameNode.checkNameNodeStatus(NameNode_pb2.msg(msg = "Are you ok?"))
            if reply.msg == "i'm very ok":
                return True
        except grpc._channel._InactiveRpcError:
            for nameNode in setting.nameNodes:
                if nameNode != self.nameNode:
                    print(f"Trying to connect to NameNode {self.nodeName}")
                    self.chooseNameNode(nameNode)
                    if self.checkNameNodeStatus() == True:
                        return True
            return False

    def join(self):
        self.chooseNameNode(0)
        if self.checkNameNodeStatus() == True:
            remainingSpace = self.space["space"]
            dataNodeInfo = NameNode_pb2.dataNodeInfo(nodeName = self.nodeName, space = remainingSpace)
            reply = self.stubForNameNode.join(dataNodeInfo) 
            print("\033[1;37;42m"+reply.msg+"\033[0m ")

    def saveToLocal(self, iterator):
        for iter in iterator:
            self.instructions = iter.instructions
            with open(self.basePath+"bufferdata", "ab") as f:
                f.write(iter.buffer)

    def saveReplica(self, iterator):

        for iter in iterator:
            with open(self.basePath+iter.instructions, "ab") as f:
                f.write(iter.buffer)
    
    def removeLocal(self):
        with open(self.basePath+"bufferdata", "w") as f:
            f.write("")

    def chooseUploadDataNode(self, uploadDataNode = 0):
        port = str(9000 + uploadDataNode)
        self.uploadDataNode = uploadDataNode
        self.channelToUploadDataNode = grpc.insecure_channel(f'localhost:{port}')
        self.stubForUploadDataNode = DataNode_pb2_grpc.DataNodeStub(self.channelToUploadDataNode)

    def justRename(self, name):
        with open(self.basePath+"bufferdata", "rb") as f1:
            with open(self.basePath+name, "wb") as f2:
                f2.write(f1.read())


    def checkDataNodeStatus(self):
        try:
            reply = self.stubForUploadDataNode.heartbeat(DataNode_pb2.msg(msg = "Are you ok?"))
            if reply.msg == "i'm alive":
                return True
        except grpc._channel._InactiveRpcError:
            return False

    def getFileStream(self, src, fileID):
    
        with open(src, 'rb') as f:
            while True:
                piece = f.read(65536)
                if len(piece) == 0:
                    return
                yield DataNode_pb2.uploadFile(instructions = fileID, buffer = piece) 

    def makeReplicas(self):
        # try: 
        success = 1
       
        for key, value in json.loads(self.instructions).items():
            for fileID in value:
                if key[-1] == self.nodeName[-1]:
                    self.justRename(str(fileID))
                    continue
                self.chooseUploadDataNode(int(key[-1]))
                if self.checkDataNodeStatus() == True:
                    yielder = self.getFileStream(self.basePath+"bufferdata", str(fileID))
                    reply = self.stubForUploadDataNode.replica(yielder)
                    if reply.msg != "success":
                        success = 0
                else:
                    success = 0
        if success == 0:
            return False
        else:
            return True
        # except:
        #     return False

    # def getFileStream(self, src, instructions):
        
    #     with open(src, 'rb') as f:
    #         while True:
    #             piece = f.read(65536)
    #             if len(piece) == 0:
    #                 return
    #             yield DataNode_pb2.uploadFile(instructions=" ",buffer = piece) 


    ### rpc service ###
    def heartbeat(self, request, context):
        return DataNode_pb2.msg(msg = "i'm alive")
    

    def upload(self, request, context):
    
        self.saveToLocal(request)
        if self.makeReplicas() == True:
            self.removeLocal()
            return DataNode_pb2.msg(msg = "success")
        else:
            self.removeLocal()
            return DataNode_pb2.msg(msg = "fail")
    

    def replica(self, request, context):
        # try:
        self.saveReplica(request)
        return DataNode_pb2.msg(msg = "success")
        # except:
        #     return DataNode_pb2.msg(msg = "fail")
        return

    def get(self, request, context):
        filePath = self.basePath +  str(request.msg)
        yielder = self.getFileStream(filePath, "")
        return yielder

    def remove(self, request, context):

        blocks = json.loads(request.msg)
        
        for block in blocks:
            block = str(block[0])
            path = self.basePath + block
            if os.path.exists(path):
                os.remove(path)

        return DataNode_pb2.msg(msg = "removed")
    
        




if __name__=="__main__":
    print("choose Datanode 1-4")
    number = input()
    servicer = dataNodeServicer(nodeName = f"datanode{number}")
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))

    DataNode_pb2_grpc.add_DataNodeServicer_to_server(servicer, server)

    server.add_insecure_port(f'[::]:900{number}')
    server.start()
    server.wait_for_termination()