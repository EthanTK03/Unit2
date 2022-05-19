import sys
import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self, parent = None): #Create the window
        super(MainWindow, self).__init__(parent)
        self.resize(500,500)
        self.setWindowTitle("HANGMAN")

        self.display = QLabel(self)
        self.display.setText("¡Hola Mundo!")
        self.display.move(50,20)
        # self.game = Game()

    #respond to paint events
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(Qt.black)
        size = event.rect().size()

        #draw the board to fit the size
        colsize = size.width() //20
        rowsize = size.height() //20

        #The hanger
        #How it works: each colsize, rowsize is a point, two in one line of code draws a line from point A to point B
        qp.drawLine(colsize*15,rowsize*2,colsize*10,rowsize*2)
        qp.drawLine(colsize*10,rowsize*2,colsize*10,rowsize*4)
        qp.drawLine(colsize*15,rowsize*2,colsize*15,rowsize*12)
        qp.drawLine(colsize*12,rowsize*12,colsize*18,rowsize*12)

        #The hanging man, 6 body parts
        qp.drawEllipse(9*colsize, 4*rowsize, colsize*2, rowsize*2) #head
        qp.drawLine(colsize*10,rowsize*6,colsize*10,rowsize*9) #body
        qp.drawLine(colsize*10,rowsize*7,colsize*12,rowsize*6) #left arm
        qp.drawLine(colsize*10,rowsize*7,colsize*8,rowsize*6) #right arm
        qp.drawLine(colsize*10,rowsize*9,colsize*11,rowsize*11) #left leg
        qp.drawLine(colsize*10,rowsize*9,colsize*9,rowsize*11) #right leg

        #Info text





def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()