
from Engine.UserManagement import UserManager

#m.update("000005fab4534d05api_key9a0554259914a86fb9e7eb014e4e5d52permswrite")
userManager = UserManager.UserManager()

def authorise(user,password):
	#TODO: Has to enable encryption and DB matching
	
	return userManager.validatePass(user,password)
