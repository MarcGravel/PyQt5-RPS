import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors")
        self.setGeometry(500, 500, 550, 500)
        self.UI()
    
    #function to create UI widgets    
    def UI(self):
        
        #####show#####
        self.show()
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__ == "__main__":
    main()