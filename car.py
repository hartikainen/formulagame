from math import *

class Car:
	
	def __init__(self, character, name, location):
		self.__name = name

		self.__location = location
		self.__gear = 1
		self.__direction = [1,0]
		self.__character = character
		
	def getName(self):
		return str(self.__name)
	
	def getChar(self):
		return self.__character
	
	def move(self, input):
		
		coords = self.allowedMoves()
		newLoc = coords[input-1]
		self.__direction[0] = newLoc[0] - self.__location[0]
		self.__direction[1] = newLoc[1] - self.__location[1]
		self.__location = newLoc
		
		if 1 <= input <= 3:
			self.gearDown()
		elif 7 <= input <= 9:
			self.gearUp()

	def swapDirection(self):
		self.__direction[0], self.__direction[1] = self.__direction[1], self.__direction[0]
		
	def getLocation(self):
		return self.__location
	
	def getGear(self):
		return self.__gear
	
	def getDirection(self):
		return self.__direction
	
	def gearUp(self):
		if self.__gear < 5:
			self.__gear += 1
			
	def gearDown(self):
		if self.__gear > 1:
			self.__gear -= 1
			
	def allowedMoves(self):
		gears = [None]*3
		

		dirRad = atan2(self.__direction[1], self.__direction[0])
		moves = [None] * 9

		gears[1] = self.getSquare(self.__gear)
		
		
		if self.__gear != 1 and self.__gear != 5:        
			gears[0] = self.getSquare(self.__gear-1)
			gears[2] = self.getSquare(self.__gear+1)
		
		elif self.__gear == 1:
			gears[0] = self.getSquare(self.__gear)
			gears[2] = self.getSquare(self.__gear+1)
		
		elif self.__gear == 5:
			gears[0] = self.getSquare(self.__gear-1)
			gears[2] = self.getSquare(self.__gear)

		for i in range(len(gears)):
			x = 0
			diff = 3*pi
			for j in range(len(gears[i])):
				pntRad = atan2(gears[i][j][1] - self.__location[1], gears[i][j][0] - self.__location[0])
				cmp = fabs((pntRad) - (dirRad))
				if cmp < diff:
					moves[3*i] = gears[i][(j+1) % len(gears[i])]
					moves[3*i+1] = gears[i][(j) % len(gears[i])]
					moves[3*i+2] = gears[i][(j-1) % len(gears[i])]
					diff = cmp
					x+=1			
		return moves
	
	def getSquare(self, gear):
		x = self.__location[0]
		y = self.__location[1]
		cords = []
		for x in range(x-gear, x+gear+1):
			cords.append([x, y+gear])

		for y in range(y+gear-1, y-gear-1, -1):
			cords.append([x+gear, y])

		for z in range(x+gear-1, x-gear-1, -1):
			cords.append([z, y - gear])

		for v in range(y-gear+1, y+gear):
			cords.append([x - gear, v])
	
		return cords