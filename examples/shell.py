from ShellPy.Engine.Security.Authentication import authenticationManager
from ShellPy.Engine.UserManagement import UserManager
from ShellPy.Engine.Commands import commandsManager

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


@commandsManager.add('save')
def handleSave(context):
	print('Saving')
	context.add(save=context.get('params'))  #context.add(key=value) Allows you to add any extra configuration keys and values.
	
	
@commandsManager.add('create')
def handleCreate(context):

	pass

@commandsManager.add('show')
def handleShow(context):
	return context.show()	#This prints available items in context

@commandsManager.add('do')
def handleDo(context):
    return context



from ShellPy.Shells import shellManager
shellManager.runShellEngine()