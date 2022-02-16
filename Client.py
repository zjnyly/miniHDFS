import grpc
import os

import NameNode_pb2
import NameNode_pb2_grpc

import DataNode_pb2
import DataNode_pb2_grpc

import hashlib

import json

import setting


class Client:
	def __init__(self, clientName = None):
		self.clientName = clientName
		self.basePath = f"./ClientSpace/{self.clientName}/"
	
	def chooseNameNode(self, nameNode = 0):
		port = str(8000 + nameNode)
		self.nameNode = nameNode
		self.channelToNameNode = grpc.insecure_channel(f'localhost:{port}')
		self.stubForNameNode = NameNode_pb2_grpc.NameNodeStub(self.channelToNameNode)
		
	def checkNameNodeStatus(self):
		try:
			reply = self.stubForNameNode.checkNameNodeStatus(NameNode_pb2.msg(msg = "Are you ok?"))
			if reply.msg == "i'm very ok":
				return True
		except grpc._channel._InactiveRpcError:
			for nameNode in setting.nameNodes:
				if nameNode != self.nameNode:
					print(f"Trying to connect to NameNode {nameNode}")
					self.chooseNameNode(nameNode)
					if self.checkNameNodeStatus() == True:
						return True
			return False
	
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


	def login(self, username = "zjn", password = "123"):
		if self.checkNameNodeStatus() == True:
			userInfo = NameNode_pb2.userInfo(username = username, password = password)
			reply = self.stubForNameNode.bindClient(userInfo)
			if reply.msg == "you are allowed to access":
				print(f"logged in NameNode {self.nameNode} successfully")
			else:
				print("\033[1;37;41m" + reply.msg + "\033[0m")
	
	def register(self, username = "zjn", password = "123"):
		if self.checkNameNodeStatus() == True:
			userInfo = NameNode_pb2.userInfo(username = username, password = password)
			reply = self.stubForNameNode.register(userInfo)
			if reply.msg == "register success":
				print("successfully registered in")
			else:
				print("\033[1;37;41m" + reply.msg + "\033[0m")
	
	def pwd(self):
		if self.checkNameNodeStatus() == True:
			reply = self.stubForNameNode.pwd(NameNode_pb2.msg(msg = ""))
			self.currentPath = reply.msg
			#print(reply.msg)

	def mkdir(self, folderName):
		if self.checkNameNodeStatus() == True:
			reply = self.stubForNameNode.mkdir(NameNode_pb2.msg(msg = folderName))
			if reply.msg != "":
				print("\033[1;37;41m" + reply.msg + "\033[0m")
	
	def cd(self, path):
		if self.checkNameNodeStatus() == True:
			reply = self.stubForNameNode.cd(NameNode_pb2.msg(msg = path)) 
			self.pwd()
		
	def calculateSHA256checksum(self, filePath):
		hash_obj = hashlib.sha256()
		with open(filePath, 'rb') as f:
			while True:
				block = f.read(65536)
				if not block:
					break
				hash_obj.update(block)
		return hash_obj.hexdigest()

	def uploadToNameNode(self, filePath, to, share):
		fileSize = os.path.getsize(filePath)
		fileName = filePath.split("/")[-1]
		checksum = self.calculateSHA256checksum(filePath)

		fileInfo = NameNode_pb2.fileInfo(fileName = fileName, to = to, fileSize = fileSize, checksum = checksum, share = True)
		if self.checkNameNodeStatus() == True:
			reply = self.stubForNameNode.upload(fileInfo)
			return reply
			
	
	def getFileStream(self, src, instructions):
		with open(src, 'rb') as f:
			while True:
				piece = f.read(65536)
				if len(piece) == 0:
					return
				yield DataNode_pb2.uploadFile(instructions=instructions,buffer = piece) 

	def uploadToDataNode(self, reply, filePath):
		self.chooseUploadDataNode(int(reply.giveTo[-1]))
		if clientHandler.checkDataNodeStatus() == True:
			yielder = self.getFileStream(filePath, reply.howTo)
			reply = self.stubForUploadDataNode.upload(yielder)
			if reply.msg == "success":
				return True
			else:
				return False

	def reportErrorToNameNode(self, fileID):
		if self.checkNameNodeStatus() == True:
			reply = self.stubForNameNode.error(NameNode_pb2.msg(msg = fileID))
			if reply.msg != "":
				print("\033[1;37;41m" + reply.msg + "\033[0m")

	def upload(self, filePath, to, share):
		reply = self.uploadToNameNode(filePath, to, share)
		if reply.allow == False:
			print(f"failed to upload file due to {reply.howTo}")
		else:
			
			print("\033[1;37;42m"+"Can Upload To Datanode:"+"\033[0m "+ str(reply.allow))
			print("\033[1;37;43m"+"Give To:"+"\033[0m "+str(reply.giveTo))
			print("\033[1;37;44m"+"Chunks:"+"\033[0m "+str(reply.chunks))
			print("\033[1;37;45m"+"How To:"+"\033[0m "+str(reply.howTo))

			status = self.uploadToDataNode(reply, filePath)
			if status == True:
				print("\033[1;32;47m"+"file successfully uploaded"+"\033[0m ")
			else:
				self.reportErrorToNameNode(reply.howTo)

	def delete(self, filePath, at):

		fileName = filePath.split("/")[-1]

		
		fileInfo = NameNode_pb2.fileInfo(fileName = fileName, to = at, fileSize = 0, checksum = "", share = True)
		if self.checkNameNodeStatus() == True:
			reply = self.stubForNameNode.delete(fileInfo)
			print("\033[1;32;47m"+reply.msg+"\033[0m ")

	def readfile(self, filePath, at):
		fileName = filePath.split("/")[-1]
		fileInfo = NameNode_pb2.fileInfo(fileName = fileName, to = at, fileSize = 0, checksum = "", share = True)
		if self.checkNameNodeStatus() == True:
			reply = self.stubForNameNode.readfile(fileInfo)
			print("\033[1;32;47m"+reply.msg+"\033[0m ")

	def releasefile(self, filePath, at):
		fileName = filePath.split("/")[-1]
		fileInfo = NameNode_pb2.fileInfo(fileName = fileName, to = at, fileSize = 0, checksum = "", share = True)
		if self.checkNameNodeStatus() == True:
			reply = self.stubForNameNode.releasefile(fileInfo)
			print("\033[1;32;47m"+reply.msg+"\033[0m ")


	def saveDataToLocalSpace(self, iterator, fileName):
		for iter in iterator:
			with open(self.basePath+fileName, "ab") as f:
				f.write(iter.buffer)
	
	def coverDataToLocalSpace(self, iterator, fileName):
		for iter in iterator:
			with open(self.basePath+fileName, "wb") as f:
				f.write(iter.buffer)
	
		

	def downloadFromDataNode(self, fileDict, fileName):
		success = 0
		for key, value in json.loads(fileDict).items():
			for FID,  CHECKSUM, ISREPLICA in value:
				self.chooseUploadDataNode(int(key[-1]))
				if self.checkDataNodeStatus() == True:
					
					reply = self.stubForUploadDataNode.get(DataNode_pb2.msg(msg = str(FID)))
					print(FID)
					self.saveDataToLocalSpace(reply, fileName)

					fileCheckSum = self.calculateSHA256checksum(self.basePath+fileName)

					#if fileCheckSum == CHECKSUM:
					return True
		return False

	def download(self, fileName, filePath):
		fileName = fileName.split("/")[-1]
		fileInfo = NameNode_pb2.fileInfo(fileName = fileName, to = filePath, fileSize = 0, checksum = "", share = False)
		
		if os.path.exists(self.basePath+fileName):
			print("\033[1;32;47m"+"File Already Exists"+"\033[0m ")
			return

		if self.checkNameNodeStatus() == True:
			reply = self.stubForNameNode.download(fileInfo)
			print(reply.howTo)
			if reply.allow == False:
				print(reply.howTo)
			else:
				if self.downloadFromDataNode(reply.howTo, fileName) == True:
					print("download file passed chechsum validation")
				else:
					print("file damaged or not exist on datanode")
		
	def ls(self, at):
		if self.checkNameNodeStatus() == True:
			reply = self.stubForNameNode.ls(NameNode_pb2.msg(msg = at))
			lsDict = json.loads(reply.msg)
			
			for key, value in lsDict.items():
				if key == "file":
					print("\033[1;37;41m"+'{0: <6}'.format("FILE")+"\033[0m")
					if value == {}:
						print("(empty)")
						continue
					print("\033[1;37;42m"+'{0: <15}'.format("FILENAME")+"\033[0m",
							"\033[1;37;43m"+'{0: <15}'.format("FILESIZE")+"\033[0m",
							"\033[1;37;44m"+'{0: <15}'.format("OWNER")+"\033[0m",
							"\033[1;37;45m"+'{0: <20}'.format("TIME")+"\033[0m",
							"\033[1;37;46m"+'{0: <15}'.format("SHARED")+"\033[0m")
					for filekey, filevalue in value.items():
						print('{0: <15}'.format(filevalue[1]),
							'{0: <15}'.format(filevalue[2]),
							'{0: <15}'.format(filevalue[4]),
							'{0: <20}'.format(filevalue[6]),
							'{0: <15}'.format(filevalue[5]))
				elif key == "folder":
					print("\033[1;37;46m"+'{0: <6}'.format("FOLDER")+"\033[0m")
					if value == {}:
						print("(empty)")
						continue
					for folderkey, _ in value.items():
						print(folderkey)
	
	def cp(self, filename, current, to):
		if self.checkNameNodeStatus() == True:
			filename = filename.split("/")[-1]
			cpMsg = NameNode_pb2.cpMsg(filename = filename, current = current, to = to)
			reply = self.stubForNameNode.cp(cpMsg)
			print("\033[1;32;47m"+reply.msg+"\033[0m ")
			

	def saveToLocalTemp(self, content):
		with open("./buffer.txt", "w") as f:
				f.write(content)

	def clearLocalTemp(self):
		with open("./buffer.txt", "w") as f:
				f.write("")

	def getEditFileStream(self, src, instructions):
		with open(src, 'rb') as f:
			while True:
				piece = f.read(65536)
				if len(piece) == 0:
					return
				yield DataNode_pb2.saveFile(fileID=instructions,buffer = piece) 

	def edit(self, filename, filepath):

		self.readfile(filename, filepath)

		filename = filename.split("/")[-1]
		fileInfo = NameNode_pb2.fileInfo(fileName = filename, to = filepath, fileSize = 0, checksum = "", share = False)

		if self.checkNameNodeStatus() == True:
			reply = self.stubForNameNode.download(fileInfo)
			print(reply.howTo)
			if reply.allow == False:
				print(reply.howTo)
			else:
				print("\033[1;37;43m"+"please write something"+"\033[0m")
				text = input()

				self.saveToLocalTemp(text)

				for key, value in json.loads(reply.howTo).items():
					for FID,  CHECKSUM, ISREPLICA in value:
						self.chooseUploadDataNode(int(key[-1]))
						if self.checkDataNodeStatus() == True:
							yielder = self.getFileStream("./buffer.txt", str(FID))
							reply = self.stubForUploadDataNode.replica(yielder)
				
				#self.clearLocalTemp()
				if self.checkNameNodeStatus() == True:
					reply = self.stubForNameNode.download(fileInfo)
					if reply.allow == False:
						print(reply.howTo)
					else:
						for key, value in json.loads(reply.howTo).items():
							for FID,  CHECKSUM, ISREPLICA in value:
								self.chooseUploadDataNode(int(key[-1]))
								if self.checkDataNodeStatus() == True:
									
									reply = self.stubForUploadDataNode.get(DataNode_pb2.msg(msg = str(FID)))
									
									self.coverDataToLocalSpace(reply, filename)

									fileCheckSum = self.calculateSHA256checksum(self.basePath+filename)
		self.releasefile(filename, filepath)
		print("\033[1;32;47m"+"Edit Finished, Check Your Local Dir"+"\033[0m ")
		
	def printHelp(self):
		print("\033[1;37;45m" + "BASIC COMMANDS" + "\033[0m")
		print('{0: <30}'.format("help"), "show help info")
		print('{0: <30}'.format("register username passwd"), "register in")
		print('{0: <30}'.format("login username passwd"), "log in")
		print('{0: <30}'.format("cd"), "change dir")
		print('{0: <30}'.format("pwd"), "show dir")
		print('{0: <30}'.format("ls"), "list all files")
		print('{0: <30}'.format("mkdir"), "make new directory")
		print('{0: <30}'.format("upload filename path share"), "upload files")
		print('{0: <30}'.format("download finename path"), "download files")
		print('{0: <30}'.format("delete filename path"), "delete files")
		print('{0: <30}'.format("delete filename path"), "delete files")
		print('{0: <30}'.format("cp filename from to"), "copy file from one dir to another")
		print('{0: <30}'.format("read filename path"), "readfile, get lock")
		print('{0: <30}'.format("release filename path"), "releasefile, release lock")
		print('{0: <30}'.format("edit filename path"), "edit file")


if __name__ == '__main__':

	print("Choose ClientID 1-4")
	number = input()
	
	
	clientHandler = Client(clientName = f"client{number}")
	clientHandler.chooseNameNode(0)

	print("\033[1;32;40m"+"None@:/"+"\033[0m", end=" ")
	command = input()
	command = command.split()
	operation = command[0].lower()
	if operation=='register':
		clientHandler.register(command[1], command[2])
		clientHandler.login(command[1], command[2])
	elif operation=='login':
		clientHandler.login(command[1], command[2])

	clientHandler.cd("/")
	clientHandler.pwd()

	while True:
		command = input()
		if command=="\n" or command==" " or command == "":
			print("\033[1;32;40m"+clientHandler.currentPath+"\033[0m", end=" ")
			continue

		command = command.split()
		operation = command[0].lower()
		clientHandler.pwd()

		if operation=='ls':
			if len(command) == 1:
				clientHandler.ls("")
			else:
				clientHandler.ls(command[1])
		elif operation=="help":
			clientHandler.printHelp()
		elif operation=='cd':
			if len(command) == 1:
				clientHandler.cd("")
			else:
				clientHandler.cd(command[1])
		elif operation=="mkdir":
			if len(command) == 1:
				print("Please enter the correct command")
			else:
				clientHandler.mkdir(command[1])
		elif operation=="pwd":
			clientHandler.pwd()
			print(clientHandler.currentPath, end=" ")
		elif operation=="upload":
			if command[3] == "SHARE":
				share = True 
			else:
				share = False
			clientHandler.upload(command[1], command[2], share)
		elif operation=="delete":
			clientHandler.delete(command[1], command[2])
		elif operation=="download":
			clientHandler.download(command[1], command[2])
		elif operation=="cp":
			clientHandler.cp(command[1], command[2], command[3])
		elif operation == "read":
			clientHandler.readfile(command[1], command[2])
		elif operation == "release":
			clientHandler.releasefile(command[1], command[2])
		elif operation == "edit":
			clientHandler.edit(command[1], command[2])
		else:
			print("Please enter the correct command")
	
	