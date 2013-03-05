class Square:
	
	def __init__(self, x, y):
		self.__road = False
		self.__player = False
		self.__banana = False
		self.__visited = False
		self.__finishLine = False
		
		self.__x = x
		self.__y = y

	
	def isFinishLine(self):
		return self.__finishLine
	
	def setFinishLine(self):
		self.__finishLine = True
		self.__road = True

		
	def setVisited(self):
		self.__visited = True	

	def isRoad(self):
		return self.__road

	def setRoad(self):
		self.__road = True

		
	def getPlayer(self):
		return self.__player

	def setPlayer(self, char):
		self.__player = char

	def rmvPlayer(self):
		if self.__player == False:
			print "You're trying to remove player from square without player!"
		else:
			self.__player = False	


	def isBanana(self):
		return self.__banana

	def rmvBanana(self):
		self.__banana = False

	def setBanana(self):
		self.__banana = True
		self.__road = True


	def getCoords(self):
		return (self.__x, self.__y)

		
	def __str__(self):
		if self.getPlayer() == "A":
			return "A"
		elif self.getPlayer() == "B":
			return "B"
		elif self.isFinishLine():
			return "|"
		elif self.isBanana():
			return "x"
		elif self.isRoad():
			return "."
		else:
			return "#"