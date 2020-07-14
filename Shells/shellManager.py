from ShellPy.Engine.Display import displayManager
from ShellPy.Engine.Commands import commandsManager
from ShellPy.Engine.Context import contextManager
from ShellPy.Engine.Security.Authentication import authenticationManager
import time

def runShellEngine():
	displayManager.stdout('Welcome To ShellPy',end='\n')
	user = displayManager.stdin('User: ')
	password = displayManager.getPass('password: ')
	if authenticationManager.authorise(user,password) == False:				#Match user , pass with existing records
		displayManager.stdout('Incorrect password, Closing')
		time.sleep(2)
		return
	else:
		context= contextManager.contextManager(user=user)
		displayManager.stdout("Welcome {}".format(user))


	while(1):
		data = displayManager.stdin('{}$ '.format(user))
		context.add(data=data)
		try:
			data= commandsManager.runCommand(context)
			if data != None:
				displayManager.stdout(data)
		except Exception as ex:
			displayManager.stdout('Error Occured: {}'.format(ex))

		#displayManager.stdout('You Have Entered {}'.format(data))


