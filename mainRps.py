import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors")
        self.setGeometry(500, 500, 550, 500)
        self.UI()
    
    #function to create UI widgets    
    def UI(self):
        ####Labels####
        self.playerLabel = QLabel("Your Score: ", self)
        self.playerLabel.move(30, 20)
        self.playerLabel.setFont(QFont("Helvetica", 16))
        
        self.computerLabel = QLabel("Computer Score: ", self)
        self.computerLabel.move(320, 20)
        self.computerLabel.setFont(QFont("Helvetica", 16))
        
        versusLabel = QLabel("VS", self)
        versusLabel.move(240, 150)
        versusLabel.setFont(QFont("Helvetica", 25))
        
        ####Images####
        self.playerImage = QLabel(self)
        self.playerImage.setPixmap(QPixmap("images/rock.png").scaledToWidth(150))
        self.playerImage.move(30, 100)
        
        self.computerImage = QLabel(self)
        self.computerImage.setPixmap(QPixmap("images/rock.png").scaledToWidth(150))
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
        self.timer.setInterval(1000)
        self.timer.timeout(self.playing)
        
        #####show#####
        self.show()
    
    def startGame(self):
        self.timer.start()
    
    def stopGame(self):
        self.timer.stop()
    
    def playing(self):
        pass
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__ == "__main__":
    main()