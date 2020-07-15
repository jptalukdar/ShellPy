import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='ShellPymyapp.log',
                    filemode='w+')
from ShellPy.Engine.Security.Authentication import authenticationManager
from ShellPy.Engine.UserManagement import UserManager
from ShellPy.Engine.Commands import commandsManager
from ShellPy.Engine.Display import displayManager
from ShellPy.Engine.Utility import utility

import pandas as pd
logger = logging.getLogger('ShellPy')

userManager = UserManager.UserManager()
userManager.addUser('admin','admin')   #Add users

authenticationManager.setUserManager(userManager)  #Set the newly created user Manager to for Authentication. It will contain user and password hash with grants later on 

@commandsManager.add('echo')  # This will be triggered when echo command is typed in the shell. A context obejct will be passed here
def echo(context):
	#displayManager.stdout(name)
	return context.get('params') #params will get command parameters if given any

@commandsManager.add('exit')
def handleExit(context):
	exit(0)


@commandsManager.add('load')
def handleSave(context):
	#print('Load')
	filename = context.get('params')
	dataset = pd.read_csv(filename)
	context.add(dataset=dataset)  #context.add(key=value) Allows you to add any extra configuration keys and values.
	return "Dataset {} Loaded".format(filename)
	
@commandsManager.add('head')
def handlehead(context):
	dataset = context.get('dataset')
	if (type(dataset) !=type(None)):
		return dataset.head()
	else:
		return "No Dataset Loaded"


@commandsManager.add('tail')
def handleTail(context):
	dataset = context.get('dataset')
	if (type(dataset) !=type(None)):
		return dataset.tail()
	else:
		return "No Dataset Loaded"

@commandsManager.add('show')
def handleShow(context):
	return context.show()	#This prints available items in context

@commandsManager.add('clear')
def handleClear(context):
	context.clear()
	return "All data cleared"


@commandsManager.add('count')
def handleCount(context):
	dataset = context.get('dataset')
	if (type(dataset) !=type(None)):
		column = context.get('params')
		columns = utility.tokenizier(column,',')
		return dataset.groupby(columns).agg(['count'])
	else:
		return "No Dataset Loaded"
	
from ShellPy.Shells import shellManager
shellManager.runShellEngine()