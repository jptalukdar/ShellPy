from ShellPy.Engine.Security.Authentication import authenticationManager
from ShellPy.Engine.UserManagement import UserManager
from ShellPy.Engine.Commands import commandsManager

userManager = UserManager.UserManager()
userManager.addUser('admin','admin')

authenticationManager.setUserManager(userManager)

@commandsManager.add('echo')
def echo(context):
	#displayManager.stdout(name)
	return context.get('params')

@commandsManager.add('exit')
def handleExit(context):
	exit(0)


@commandsManager.add('save')
def handleSave(context):
	print('Saving')
	pass
	
@commandsManager.add('create')
def handleCreate(context):
	pass

@commandsManager.add('show')
def handleShow(context):
	return context.show()

@commandsManager.add('do')
def handleDo(context):
    return context



from ShellPy.Shells import shellManager
shellManager.runShellEngine()