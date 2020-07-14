import subprocess
import os
from ShellPy.Engine.Display import displayManager
from ShellPy.Engine.Context import contextManager

class commands:
	commandsList = {}

	def addCommand(self,funcname,func):
		self.commandsList[funcname]=func

	

	def execute(self,funcname,params=None):
		return self.commandsList[funcname](params)

	def findAndExecute(self,funcname,params):
		if funcname in self.commandsList:
			data = self.execute(funcname,params)
			return True,data
		else:
			return False,None
__commands = commands()

def add(funcname):
		def wrapper(func):
			commands.addCommand(commands,funcname,func)
		return wrapper

def cleanData(data):
	return data.strip(' ')

def runCommand(context):   #A context object will be passed by shellManager to execute the command
	data=context.get('data')
	data=cleanData(data)
	dataTokensIndex=data.find(' ')
	if dataTokensIndex != -1:
		command=data[:dataTokensIndex]
		params=data[dataTokensIndex:]
	else:
		command=data
		params=None
	results = __commands.findAndExecute(command,params)
	if results[0] == False:
		#os.system(data)
		return "Unknown command: {}".format(command)
	else:
		return results[1] 

def parseCommand(data):
	# data = data.strip(" ")
	# intialTokens = data.split(" ")
	# tokens = []
	# for token in initialTokens:
	# 	if 
	runCommand(data)


