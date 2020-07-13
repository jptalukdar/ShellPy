class contextManager():
	contextObjects={}
	counters={}
	__reservekeys = []
	def __init__(self,**kwargs):
		self.contextObjects.update(kwargs)
		self.__reservekeys.append('user')
	def get(self,key):
		return self.contextObjects.get(key)

	def safeGet(self,key,default=None):
		return self.contextObjects.get(key,default)


	def add(self,**kwargs):
		for k,v in kwargs.items():
			self.addPair(k,v)

	def addPair(self,key,value):
		if key not in self.__reservekeys:
			self.contextObjects[key]=value
		else:
			raise Exception('Reserved Keys cannot be added to Context')

	def addCounter(self,key):
		if key not in self.counters:
			self.counters[key]=0

	def incrementCounter(self,key,value=1):
		self.addCounter(key)
		self.counters[key]+=int(value)

	def parse(self,result):
		self.add(**result.getKwargs)


class resultObject():
	resultObject={}
	
	def __init__(self,**kwargs):
		self.resultObject.update(kwargs)

	def get(self,key):
		return self.resultObject.get(key,None)

	def getKwargs(self):
		return self.resultObject