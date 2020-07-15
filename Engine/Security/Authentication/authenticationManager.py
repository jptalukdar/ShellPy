
from ShellPy.Engine.UserManagement import UserManager
import logging

logger = logging.getLogger('ShellPy.Engine.Authentication')
logger.setLevel(logging.DEBUG)

userManager = UserManager.UserManager()
userManager.addUser('admin','admin')
def setUserManager(customUserManager):
	logging.debug(((type(customUserManager),type(UserManager))))
	global userManager
	userManager=customUserManager
	logging.info('User manager added')



def authorise(user,password):
	#TODO: Has to enable encryption and DB matching
	
	return userManager.validatePass(user,password)
