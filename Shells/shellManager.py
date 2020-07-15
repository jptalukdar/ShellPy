from ShellPy.Engine.Display import displayManager
from ShellPy.Engine.Commands import commandsManager
from ShellPy.Engine.Context import contextManager
from ShellPy.Engine.Security.Authentication import authenticationManager
import time

def runShellEngine():
	displayManager.dispout('Welcome To ShellPy',end='\n')
	user = displayManager.stdin('User: ')
	password = displayManager.getPass('password: ')
	if authenticationManager.authorise(user,password) == False:				#Match user , pass with existing records
		displayManager.dispout('Incorrect password for {}, Closing'.format(user))
		time.sleep(2)
		return
	else:
		context= contextManager.contextManager(user=user)	#Initialize a context object to store context values
		displayManager.dispout("Welcome {}".format(user))


	while(1):
		data = displayManager.stdin('{}$ '.format(user))
		context.add(input=data)				#Store Input in context object
		try:
			data= commandsManager.runCommand(context)
			if (type(data) !=type(None)):		#some data doesn't support boolean operations hence the type
				displayManager.dispout(data)
		except Exception as ex:
			displayManager.dispout('Error Occured: {}'.format(ex))

		#displayManager.dispout('You Have Entered {}'.format(data))


