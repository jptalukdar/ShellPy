import subprocess
import os
from ShellPy.Engine.Display import displayManager
from ShellPy.Engine.Context import contextManager
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='D:/Github/ShellPy/LOGS/ShellPymyapp.log',
                    filemode='w+')
logger = logging.getLogger('ShellPy.Engine.Commands')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

class commands:
	commandsList = {}

	def addCommand(self,funcname,func):
		self.commandsList[funcname]=func

	def execute(self,context):
		funcname = context.get('command')
		return self.commandsList[funcname](context)

	def findAndExecute(self,context):
		funcname = context.get('command')
		logger.info('Executing function: {}'.format(funcname))
		if funcname in self.commandsList:
			data = self.execute(context)
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
	data=context.get('input')  
	command,params = parseCommand(data)
	context.add(command=command,params=params)			#add command and params to context , pass the context to Executor
	results = __commands.findAndExecute(context)        #Retrieving results from executor
	if results[0] == False:
		return "Unknown command: {}".format(command)
	else:
		return results[1] 

def parseCommand(data):			#separate commands and parameters
	data=cleanData(data)
	dataTokensIndex=data.find(' ')
	if dataTokensIndex != -1:
		command=data[:dataTokensIndex]
		params=cleanData(data[dataTokensIndex:])
	else:
		command=data
		params=None
	return command,params

