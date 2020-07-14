
def stdout(msg,end='\n'):
	print(msg,end=end)

def stderr(msg):
	print("ERROR: {0}".format(msg))

def stdin(promt=None):
	data = input(promt)
	return data

def getPass(promt):
	import getpass
	return getpass.getpass(promt)

def dispout(msg,end='\n',disp='stdin'):
	if disp=='stdin':
		stdout(msg,end)