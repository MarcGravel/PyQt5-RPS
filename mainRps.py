import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors")
        self.setGeometry(500, 500, 550, 500)
        self.UI()
    
    #function to create UI widgets    
    def UI(self):
        ####Labels####
        self.startingPlayerScore = 0
        self.startingComputerScore = 0
        
        self.playerLabel = QLabel("Your Score: "+str(self.startingPlayerScore), self)
        self.playerLabel.move(30, 20)
        self.playerLabel.setFont(QFont("Helvetica", 16))
        
        self.computerLabel = QLabel("Computer Score: "+str(self.startingComputerScore), self)
        self.computerLabel.move(320, 20)
        self.computerLabel.setFont(QFont("Helvetica", 16))
        
        versusLabel = QLabel("VS", self)
        versusLabel.move(240, 150)
        versusLabel.setFont(QFont("Helvetica", 25))
        
        ####Images####
        self.rockImg = QPixmap("images/rock.png").scaledToWidth(150)
        self.paperImg = QPixmap("images/paper.png").scaledToWidth(150)
        self.scissorsImg = QPixmap("images/scissors.png").scaledToWidth(150)
        
        QPixmap("images/rock.png").scaledToWidth(150)
        self.playerImage = QLabel(self)
        self.playerImage.setPixmap(self.rockImg)
        self.playerImage.move(30, 100)
        
        self.computerImage = QLabel(self)
        self.computerImage.setPixmap(self.rockImg)
        self.computerImage.move(340, 100)
        
        ###Buttons###
        startBtn = QPushButton("Start", self)
        startBtn.move(180, 300)
        startBtn.setFont(QFont("Arial", 13))
        startBtn.clicked.connect(self.startGame)
        
        stopBtn = QPushButton("Stop", self)
        stopBtn.move(260, 300)
        stopBtn.setFont(QFont("Arial", 13))
        stopBtn.clicked.connect(self.stopGame)
        
        ####Timer####
        self.timer = QTimer(self)
        self.timer.setInterval(60)
        self.timer.timeout.connect(self.playTheGame)
        
        #####show#####
        self.show()
    
    def startGame(self):
        self.timer.start()
    
    def playTheGame(self):
        self.randomComputerInt = randint(1, 3)
        if self.randomComputerInt == 1: 
            self.computerImage.setPixmap(self.rockImg)
        elif self.randomComputerInt == 2: 
            self.computerImage.setPixmap(self.paperImg)
        elif self.randomComputerInt == 3: 
            self.computerImage.setPixmap(self.scissorsImg)
            
        self.randomPlayerInt = randint(1, 3)
        if self.randomPlayerInt == 1: 
            self.playerImage.setPixmap(self.rockImg)
        elif self.randomPlayerInt == 2: 
            self.playerImage.setPixmap(self.paperImg)
        elif self.randomPlayerInt == 3: 
            self.playerImage.setPixmap(self.scissorsImg)
    
    def stopGame(self):
        self.timer.stop()
        
        if (self.randomPlayerInt == 1 and self.randomComputerInt == 2):
            self.startingComputerScore += 1
            self.computerLabel.setText("Computer Score: "+ str(self.startingComputerScore))
        elif (self.randomPlayerInt == 1 and self.randomComputerInt == 3):
            self.startingPlayerScore += 1
            self.playerLabel.setText("Your Score: "+ str(self.startingPlayerScore))
        elif (self.randomPlayerInt == 2 and self.randomComputerInt == 3):
            self.startingComputerScore += 1
            self.computerLabel.setText("Computer Score: "+ str(self.startingComputerScore))
        elif (self.randomPlayerInt == 2 and self.randomComputerInt == 1):
            self.startingPlayerScore += 1
            self.playerLabel.setText("Your Score: "+ str(self.startingPlayerScore))
        elif (self.randomPlayerInt == 3 and self.randomComputerInt == 1):
            self.startingComputerScore += 1
            self.computerLabel.setText("Computer Score: "+ str(self.startingComputerScore))
        elif (self.randomPlayerInt == 3 and self.randomComputerInt == 2):
            self.startingPlayerScore += 1
            self.playerLabel.setText("Your Score: "+ str(self.startingPlayerScore))
        
        if (self.startingPlayerScore == 5 or self.startingComputerScore == 5):
            
            if (self.startingPlayerScore == 5):
                mbox = QMessageBox.information(self, "Winner", "You Win!")
            else:
                mbox = QMessageBox.information(self, "Loser", "You Lose")
                
            self.startingComputerScore = 0
            self.computerLabel.setText("Computer Score: "+ str(self.startingComputerScore))
            self.startingPlayerScore = 0
            self.playerLabel.setText("Your Score: "+ str(self.startingPlayerScore))
    
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__ == "__main__":
    main()