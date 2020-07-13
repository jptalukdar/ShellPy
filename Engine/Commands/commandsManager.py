import subprocess
import os
from Engine.Display import displayManager
from Engine.Context import contextManager

class commands:
	commandsList = {}

	def addCommand(self,funcname,func):
		self.commandsList[funcname]=func

	def add(funcname):
		def wrapper(func):
			commands.addCommand(commands,funcname,func)
		return wrapper

	def execute(self,funcname,params=None):
		return self.commandsList[funcname](params)

	def findAndExecute(self,funcname,params):
		if funcname in self.commandsList:
			data = self.execute(funcname,params)
			return True,data
		else:
			return False,None
__commands = commands()

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


@commands.add('echo')
def echo(name):
	#displayManager.stdout(name)
	return name

@commands.add('exit')
def handleExit(name):
	exit(0)


@commands.add('save')
def handleSave(context):
	print('Saving')
	pass
	
@commands.add('create')
def handleCreate(context):
	pass

@commands.add('show')
def handleShow(context):
	pass
