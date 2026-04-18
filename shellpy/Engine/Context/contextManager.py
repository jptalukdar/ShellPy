class contextManager():
	contextObjects={}
	sysParam = {}
	counters={}
	
	def __init__(self,**kwargs):
		self.sysParam.update(kwargs)
	
	def clear(self):
		return self.contextObjects.clear()

	def get(self,key):
		return self.contextObjects.get(key)

	def safeGet(self,key,default=None):
		return self.contextObjects.get(key,default)

	def getSysParam(self,key):
		return self.sysParam.get(key)

	def addSysParam(self,**kwargs):
		for k,v in kwargs.items():
			self.addPairSysParam(k,v)

	def addPairSysParam(self,key,value):
		self.sysParam[key]=value

	def add(self,**kwargs):
		for k,v in kwargs.items():
			self.addPair(k,v)

	def addPair(self,key,value):
		self.contextObjects[key]=value

	def addCounter(self,key):
		if key not in self.counters:
			self.counters[key]=0

	def incrementCounter(self,key,value=1):
		self.addCounter(key)
		self.counters[key]+=int(value)

	def parse(self,result):
		self.add(**result.getKwargs)

	def show(self):
		return str(self.contextObjects)


class resultContext(contextManager):
	resultObject={}
	
	def __init__(self,**kwargs):
		self.resultObject.update(kwargs)

	def get(self,key):
		return self.resultObject.get(key,None)

	def getKwargs(self):
		return self.resultObject