from PyQt4 import QtCore, QtGui
import sys
import os
from formulagame import Formulagame

class Formulagame_GUI(QtGui.QMainWindow):
    
    def __init__(self):
        super(Formulagame_GUI, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        # Initialize the buttons for new game, help and quit game, and put then in the menu bar
        #The quick game will start a game with track found in "track1.txt" and player names "player1" and "player2".

        quickGameAction = QtGui.QAction(QtGui.QIcon('pikapeli.png'), 'Quickgame', self)        
        quickGameAction.setShortcut('Ctrl+P')
        quickGameAction.setStatusTip('Start quickgame by clicking here')
        quickGameAction.triggered.connect(self.quickGame)
        
        newGameAction = QtGui.QAction(QtGui.QIcon('uusipeli.png'), 'New Game', self)        
        newGameAction.setShortcut('Ctrl+N')
        newGameAction.setStatusTip('Start game by clicking here')
        newGameAction.triggered.connect(self.newGame)

        HelpAction = QtGui.QAction(QtGui.QIcon("tietoa.png"), "Help", self)
        HelpAction.setShortcut("F1")
        HelpAction.setStatusTip("Help")
        HelpAction.triggered.connect(self.showHelp)
        
        lopetapeliAction = QtGui.QAction(QtGui.QIcon('lopetapeli.png'), 'Exit', self)        
        lopetapeliAction.setShortcut('Ctrl+Q')
        lopetapeliAction.setStatusTip('Exit')
        lopetapeliAction.triggered.connect(QtGui.qApp.quit)

        # Create a new Status bar and Menu bar
        self.statusBar()
        menubar = self.menuBar()
        
        # Add File and Help menus to the Menu bar!
        fileMenu = menubar.addMenu('&File')
        helpMenu = menubar.addMenu("&Help")
        
        # Add actions to the menus.
        fileMenu.addAction(newGameAction)
        fileMenu.addAction(quickGameAction)
        fileMenu.addAction(lopetapeliAction)

        helpMenu.addAction(HelpAction)
        
        # Resize the window
        self.setGeometry(10, 10, 300, 150)
        self.setWindowTitle('Formulagame')    
        self.show()
        
        # Create and add the start screen to the UI
        self.startWindow = StartWindow(self)
        self.setCentralWidget(self.startWindow)

        self.startWindowData()
        
        
        self.startWindow.okButton.clicked.connect(self.startGame)

        # Center the window
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)
        
    def startWindowData(self):
        self.player1 = self.startWindow.player1Edit.text()
        self.player2 = self.startWindow.player2Edit.text()
        self.trackName = self.startWindow.trackEdit.currentText()
        self.startWindow.player1Edit.textChanged[str].connect(self.getData)
        self.startWindow.player2Edit.textChanged[str].connect(self.getData)
        self.startWindow.trackEdit.currentIndexChanged[str].connect(self.getData)
        
        
    def showHelp(self):
        self.helpWindow = HelpWindow()
        self.helpWindow.show()
    
    def newGame(self):
        self.startWindow = StartWindow(self)
        self.startWindowData()
        self.startWindow.okButton.clicked.connect(self.startGame)
        self.setCentralWidget(self.startWindow)
    
    def quickGame(self):
        self.gameArea = GameArea(self, self.trackName, "pelaaja1", "pelaaja2")
        self.setCentralWidget(self.gameArea)
    
    def startGame(self):
        if self.player1 != "" and not (" " in self.player1) and self.player2 != "" and not (" " in self.player2) and self.trackName != "":
            self.gameArea = GameArea(self, self.trackName, self.player1, self.player2)
            self.setCentralWidget(self.gameArea)
        
    def getData(self):
        self.player1 = self.startWindow.player1Edit.text()
        self.player2 = self.startWindow.player2Edit.text()
        self.trackName = self.startWindow.trackEdit.currentText()

class StartWindow(QtGui.QFrame):

    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)

        # Create the text fields for player names
        self.player1Edit = QtGui.QLineEdit()
        self.player1Edit.setText("Player1")
        player1 = QtGui.QLabel('Player 1:')
        self.player2Edit = QtGui.QLineEdit()
        player2 = QtGui.QLabel('Player 2:')
        self.player2Edit.setText("Player2")
         
        # Create the combobox for the track selection
        self.trackEdit = QtGui.QComboBox(self)
        trackList = os.listdir("Tracks/")
        for i in trackList:
            self.trackEdit.addItem(str(i))
        trackName = QtGui.QLabel('Select track:')
        
        # The push button to start the race
        self.okButton = QtGui.QPushButton("Race!")
        
        # The quit button to exit the game
        exitButton = QtGui.QPushButton("Exit")
        exitButton.clicked.connect(QtGui.qApp.quit)
                
        # Create a grid
        grid = QtGui.QGridLayout()
        grid.setSpacing(1)

        # Add the widgets to the grid
        grid.addWidget(player1, 1, 1)
        grid.addWidget(self.player1Edit, 1, 2)

        grid.addWidget(player2, 2, 1)
        grid.addWidget(self.player2Edit, 2, 2)

        grid.addWidget(trackName, 3, 1)
        grid.addWidget(self.trackEdit, 3, 2)
        
        grid.addWidget(self.okButton, 4, 1)
        grid.addWidget(exitButton, 4, 2)

        # Set the grid to the layout
        self.setLayout(grid)

class GameArea(QtGui.QFrame):

    def __init__(self, parent, trackName, player1, player2):
        QtGui.QFrame.__init__(self)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        
        self.trackName = trackName
        self.player1Name = player1
        self.player2Name = player2

        # Create a layout
        self.layout = QtGui.QGridLayout()
        self.layout.setMargin(1)
        self.layout.setSpacing(1)
        
        # Load the formula game from Formulagame -class
        self.game = Formulagame(str(trackName), str(player1), str(player2))
        
        # Initialize the needed variables
        self.oldNextPlayerMoves = []
        self.helpWindow = None
        self.popUpWindow = None
        
        grid = self.game.getGrid()
        
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                label = QtGui.QLabel(grid[row][column])
                self.layout.addWidget( label, column, row )

        self.setLayout(self.layout)

    # keyPressEvent methdod listens the key presses, calls the Formulagame.makeMove() -method and refreshes the window
    def keyPressEvent(self, e):
        if 56 >= e.key() >= 49:
            if self.game.getProgress() == True:
                move, nextPlayerMoves = self.game.makeMove(e.key() - 48)
                if self.game.getProgress() == True:
                    self.refreshWindow(move, nextPlayerMoves)
                else:
                    if move == "hit":
                        finalText = "Player %s hit the other player. His car broke and he lost the game!" % (str(nextPlayerMoves))
                    elif move == "wall":
                        finalText = "Player %s hit the wall! The car broke down and he lost the game!" % (str(nextPlayerMoves))
                    elif move == "win":
                        finalText = "Player %s won the race! Winners name and laps is saved to the results.txt -file!" % (str(nextPlayerMoves[0]))
                        self.saveResults(self.trackName, nextPlayerMoves[0], nextPlayerMoves[1])
                    self.popUpWindow = PopUpWindow(finalText)
     
     
    # Save the results to the file
    def saveResults(self, trackName, playerName, moves):
        f = open('results.txt', 'r+')
        f.seek(0,2)
        f.write(str(trackName)+ ": " + str(playerName) + " , " + str(moves) + " moves\n")
        f.close()
        
    # A method to refresh the window between the moves   
    def refreshWindow(self, points, newPlayerPoints):
        try:
            # Remove the previous player's possible points from the track
            for i in self.oldNextPlayerMoves:
                square = str(self.game.getSquare(i[0], i[1]))
                self.layout.itemAtPosition(i[1], i[0]).widget().setText(square)
                
            # Refresh the square which player drove by
            for i in range(len(points)):
                if i == (len(points)):
                    square = str(self.game.getSquare(points[i][0], points[i][1]))
                    self.layout.itemAtPosition(points[i][1], [i][0]).widget().setText(square)
                
            
            # Mark the squares which the next player can drive to
            for i in range(len(newPlayerPoints)):
                self.layout.itemAtPosition(newPlayerPoints[i][1], newPlayerPoints[i][0]).widget().setText(str(i+1))
            
            
            self.oldNextPlayerMoves = newPlayerPoints
        except AttributeError:
            pass

# popUpWindow will be popped when the game ends.           
class PopUpWindow(QtGui.QMainWindow):
    
    def __init__(self, finalText):
        super(PopUpWindow, self).__init__()
        self.__finalText = finalText
        self.initUI()
        
    def initUI(self):               
        
        # textEdit = QtGui.QTextEdit()
        # textEdit.append(self.finalText)
        
        label = QtGui.QLabel(self.__finalText, self)
        label.move(35,30)

        # self.setCentralWidget(label)

        exitAction = QtGui.QAction(QtGui.QIcon(""), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        self.setGeometry(300, 300, 450, 70)
        self.setWindowTitle('The game ended!')    
        self.show()


# The window to show the contents of help.txt
class HelpWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(HelpWindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.__loadHelpFile()
        
        label = QtGui.QLabel(self.__helpText, self)
        # textEditor = QtGui.QTextEdit()
        # textEditor.append(self.__helpText)
        
        # self.setCentralWidget(textEditor)
        self.setCentralWidget(label)

        # Set the hotkeys
        exitAction = QtGui.QAction(QtGui.QIcon(""), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit')
        exitAction.triggered.connect(self.close)

        # Create the status bar and menu bar for the help window
        self.statusBar()

        menubar = self.menuBar()
        
        # Create the content for the menu bar
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Help')    
        self.show()
    
    
    # Load the contents of help.txt
    def __loadHelpFile(self):
        p = os.path.join(sys.path[0], "help.txt")
        try:
            f = open(p)
            self.__helpText = f.read()
        except:
            self.__helpText = "Loading the help file " + p + " failed!"
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Formulagame_GUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()