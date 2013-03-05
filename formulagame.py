from track import Track
from square import Square
from car import Car
from math import *

class Formulagame:
    
    def __init__(self, fileName, plr1, plr2):
        self.__track = Track("Tracks/" + fileName)
        self.__progress = True
        self.__moves = 0

        self.__startPosA = []
        self.__startPosB = []
        self.__initStartPos()
        
        self.__winner = None
        self.__winnerMoves = 0
        self.__trackName = fileName
        
        self.__playerA = Car("A", plr1, self.__startPosA)
        self.__playerB = Car("B", plr2, self.__startPosB)
    
    def getGrid(self):
        return self.__track.getGrid()
    
    def __initStartPos(self):
        self.__startPosA = self.__track.getPlayerPos("A")
        self.__startPosB = self.__track.getPlayerPos("B")
    
    def getProgress(self):
        return self.__progress
        
    def getSquare(self, x, y):
        return self.__track.getSquare(x, y) 
        
    def getMoves(self):
        return self.__moves

    # //
    def makeMove(self, input):
        if self.__progress == True:
            car = self.nextPlayer()
            
            startPoint = car.getLocation()

            startSquare = self.getSquare(startPoint[0], startPoint[1])
            startSquare.rmvPlayer()
            
            car.move(input)
            self.__moves += 1
            
            endPoint = car.getLocation()
            bresenham = self.bresenham(startPoint, endPoint)
            
            for point in bresenham:
                midPoint = self.getSquare(point[0], point[1])
                if not midPoint.isRoad():
                    self.__progress = False
                    return "wall", str(car.getName())
                if midPoint.isBanana():
                    car.swapDirection()
                if midPoint.getPlayer():
                    self.__progress = False
                    return "hit", str(car.getName())
                if midPoint.isFinishLine():
                    self.__progress = False
                    return "win", [car.getName(), self.getMoves()/2 + 1]
                midPoint.setVisited()

            square = self.getSquare(endPoint[0], endPoint[1])
            square.setPlayer(car.getChar())
            
            # Get the player, who's next in turn and return, so that we can print the allowed moves on the track!
            nextCar = self.nextPlayer()
            newPlayerMoves = car.allowedMoves()
            
            return bresenham, newPlayerMoves
            
        
    def nextPlayer(self):
        if (self.__moves % 2) == 0:
            return self.__playerA
        else:
            return self.__playerB

    # Bresenham's algorithm to count the square between to locations.
    # http://en.wikipedia.org/wiki/Bresenham's_line_algorithm
    def bresenham(self, oldLocation, newLocation):
        x0 = oldLocation[0]
        x1 = newLocation[0]
        y0 = oldLocation[1]
        y1 = newLocation[1]
        line = []
        sx = 0
        sy = 0
        dx = fabs(x1-x0)
        dy = fabs(y1-y0) 
        if x0 < x1:
            sx = 1 
        else:
            sx = -1
            
        if y0 < y1:
            sy = 1 
        else: 
            sy = -1
            
        diff = dx-dy
    
        while True:
            e2 = 2*diff
            if e2 > -dy:
                diff = diff - dy
                x0 += sx
    
            if e2 <  dx: 
                diff = diff + dx
                y0 = y0 + sy 
            
            line.append([x0,y0])
            
            if x0 == x1 and y0 == y1:
                break
        return line
    
    def getWidth(self):
        return self.__track.getWidth()

    def getHeight(self):
        return self.__track.getHeight()
    
    def __str__(self):
        out = ""
        out += str(self.__track)
        out += str(self.__playerA)
        return out