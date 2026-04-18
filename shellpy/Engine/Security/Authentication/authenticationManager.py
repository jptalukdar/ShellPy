
from shellpy.Engine.UserManagement import UserManager
import logging

logger = logging.getLogger('shellpy.Engine.Authentication')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
#m.update("000005fab4534d05api_key9a0554259914a86fb9e7eb014e4e5d52permswrite")
userManager = UserManager.UserManager()
userManager.addUser('admin','admin')
def setUserManager(customUserManager):
	print(type(customUserManager),type(UserManager))
	global userManager
	userManager=customUserManager
	logging.info('User manager added')



def authorise(user,password):
	#TODO: Has to enable encryption and DB matching
	
	return userManager.validatePass(user,password)
