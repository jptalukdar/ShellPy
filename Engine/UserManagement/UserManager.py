import hashlib



class UserManager():
    def __init__(self):
        pass

    def hash(self,string):
        hashgenerate = hashlib.md5()
        hashgenerate.update(string.encode('utf-8'))
        return hashgenerate.hexdigest()
    def getPassHash(self,user):
        #TODO: retrieve Info from DB
        hashses = {'admin':'21232f297a57a5a743894a0e4a801fc3'}
        return hashses.get(user,None)

    def validatePass(self,user,password):
        passHash = self.hash(password)
        if passHash == self.getPassHash(user):
            return True
        else:
            return False