from square import Square

MAXIMUM_WIDTH = 220
MAXIMUM_HEIGHT = 220

class Track:
    def __init__(self, file):
    
        self.__width = 0
        self.__height = 0
        self.__squares = []
        self.__startA = [0,0]
        self.__startB = [0,0]
        
        self.__initialize(file)
        
    def getGrid(self):
        out = []
        for x in range(self.__width):
            newRow = []
            for y in range(self.__height):
                square = self.getSquare(x, y)
                newRow.append(str(square))
            out.append(newRow)
        return out
    
    
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height

    # Read the file given as a parameter and initialize the track by it.
    def __initialize(self, file):
        try:
            file = open(file, 'r')
            # Current Line
            cline = ""

            '''
            The track file have to start with the definition of the width and height of the track.
            The definition must be in format (width:XX,height:YY), where X and Y are digits.
            '''

            #First start by initializing the data for the track.
            try:
                cline = file.readline()
                data = cline.split(",")
                
                width = data[0].split(":")
                height = data[1].split(":")
                # Check that the first line has the right format
                if width[0] != "width" or height[0] != "height":
                    raise IOError("The first row of the file must be in format (width:XX,height:YY)!")
                
                # Check that the width is less than MAXIMUM_WIDTH in the beginning of this file.
                if MAXIMUM_WIDTH >= int(width[1]) > 0:
                    self.__width = int(width[1])
                else:
                    raise IOError("Width of the track must be between 1 and %s", MAXIMUM_WIDTH)
                
                # Check that the height is less than MAXIMUM_HEIGHT in the beginning of this file.
                if MAXIMUM_HEIGHT >= int(height[1]) > 0:
                    self.__height = int(height[1])
                else:
                    raise IOError("Height of the track must be between 1 and %s", MAXIMUM_HEIGHT)
                cline = file.readline()
            except IOError:
                print "Reading the data from the first line failed!"
                    
            # Initialize a 2-dimensional array to store the track.
            self.__initTrack()

            y = 0
            while cline != "":
                x = 0
                cline = cline.strip()
                for i in cline:
                    sqr = self.getSquare(int(x), int(y))
                    
                    if i == ".":
                        sqr.setRoad()
                    if i == "A":
                        self.__startA[0], self.__startA[1] = sqr.getCoords()
                        sqr.setRoad()
                        sqr.setPlayer("A")
                    if i == "B":
                        self.__startB[0], self.__startB[1] = sqr.getCoords()
                        sqr.setRoad()
                        sqr.setPlayer("B")
                    if i == "x":
                        sqr.setBanana()
                    if i == "|":
                        sqr.setFinishLine()
                    x += 1
                y += 1
                cline = file.readline()
        except AttributeError:
            pass        
                    
    def getPlayerPos(self, char):
        if char == "A":
            return self.__startA
        elif char == "B":
            return self.__startB
    

    # Method for initializing the 2-dimensional array to store the track.
    # The array is filled up with Square -objects with default values (acting as a wall element).
    def __initTrack(self):
        for x in range(self.__width):
            newColumn = []
            for y in range(self.__height):
                newSquare = Square(x, y)
                newColumn.append(newSquare)
            self.__squares.append(newColumn)
            
    def getSquare(self, x, y):
        try:
            return self.__squares[x][y]
        except IndexError:
            print "You're trying to get a square from an index that does not exist!"
    
    def checkSquare(self, x, y):
        return (0 <= x < self.__width and 0 <= y < self.__height)

    # Return the string description of a track object
    def __str__(self):
        out = ""
        for y in range(self.__height):
            for x in range(self.__width):
                out += str(self.getSquare(x, y))
            out += "\n"
        return out