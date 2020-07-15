import hashlib
import logging

logger = logging.getLogger('ShellPy.Engine.UserManager')
logger.setLevel(logging.DEBUG)



class UserExistsException(Exception):
    def __init__(self,name):
        self.value = name
    
    def __str__(self):
        return('User {} Already exists'.format(self.value))

class UserManager():
    def __init__(self):
        self.__users={}

    def addUser(self,user,password):            
        if user in self.__users:            #Move storing in dictionary to database
            raise UserExistsException(user)
        else:
            self.__users[user]=self.hash(password)
            logging.debug('User {} added'.format(user))
            logging.debug('Available Users : {}'.format(str(self.__users.keys())))
            return 1

    def hash(self,string):
        hashgenerate = hashlib.md5()
        hashgenerate.update(string.encode('utf-8'))
        return hashgenerate.hexdigest()
    def getPassHash(self,user):
        #TODO: retrieve Info from DB
        #hashses = {'admin':'21232f297a57a5a743894a0e4a801fc3'}
        return self.__users.get(user,None)

    def validatePass(self,user,password):
        passHash = self.hash(password)
        logging.debug('Available Users : {}'.format(str(self.__users.keys())))
        if passHash == self.getPassHash(user):
            logging.debug('Password Matched, Granting entry')
            return True
        else:
            logging.debug('Access Denied')
            return False