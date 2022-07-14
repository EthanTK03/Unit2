import sys
import random
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self, parent = None): #Create the window
        super(MainWindow, self).__init__(parent)
        self.resize(500,500)
        self.setWindowTitle("HANGMAN")

        #Display the word
        #Choose a file
        self.display = QLabel(self)
        self.display.setText("Choose a File/Subject")
        self.display.move(280,320)
        #Font for message 1
        font = QFont()
        font.setFamily('Calibri')
        font.setPointSize(14)
        self.display.setFont(font)

        #Choose a subject (dropdown box)
        self.comboBox = QComboBox(self) #Create the comboBox
        self.comboBox.setGeometry(QRect(280,350,150,25)) #Set it's position and size (x,y,width,height)
        # self.comboBox.activated.connect(self.react)
       
        #Subjects to choose from
        self.files = [f for f in os.listdir(".") if f.endswith(".txt")]
        for f in self.files: #find a way to get rid of '.txt' when displaying the file name in the combobox
            self.comboBox.addItem(f)
        self.comboBox.activated.connect(self.activated)
        
        # # comboBox.onClick.getComponent("comboBox").getValue()
        # self.comboBox.currentIndexChanged(self.selectionchange) #selectionchange is a function to be written
        # comboBox.currentText() #Will give the selected file


        #Input a letter
        self.textbox = QLineEdit(self)
        self.textbox.move(290,425)
        self.textbox.resize(80,30)

        self.display2 = QLabel(self)
        self.display2.setText("Guess a Letter")
        self.display2.move(300,400)
        #Font for message 2
        font2 = QFont()
        font2.setFamily('Calibri')
        font2.setPointSize(14)
        self.display2.setFont(font)

        self.displayword = QLabel(self)
        self.displayword.setText('_____________________')
        self.displayword.move(50,435)
        font3 = QFont()
        font3.setFamily('Calibri')
        font3.setPointSize(14)
        self.displayword.setFont(font3)

        #Submit guess (button)
        self.btn = QPushButton(self)
        self.btn.move(370,424)
        self.btn.resize(50,32)
        self.btn.setText("Submit")
        # self.game = Game()

        self.chosenWord = ''
        self.guesses = []
        self.misses = 0


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
        if self.misses >= 1:
            b1 = qp.drawEllipse(9*colsize, 4*rowsize, colsize*2, rowsize*2) #head
        if self.misses >= 2:
            b2 = qp.drawLine(colsize*10,rowsize*6,colsize*10,rowsize*9) #body
        if self.misses >= 3:
            b3 = qp.drawLine(colsize*10,rowsize*7,colsize*12,rowsize*6) #left arm
        if self.misses >= 4:
            b4 = qp.drawLine(colsize*10,rowsize*7,colsize*8,rowsize*6) #right arm
        if self.misses >= 5:
            b5 = qp.drawLine(colsize*10,rowsize*9,colsize*11,rowsize*11) #left leg
        if self.misses >= 6:
            b6 = qp.drawLine(colsize*10,rowsize*9,colsize*9,rowsize*11) #right leg

    def activated(self):
        file = self.files[self.comboBox.currentIndex()]
        # open file and get random word
        # set that word to self.display3
        text = []
        wordfile = open(file)
        for line in wordfile:
            text.append(line.strip().lower())
        print(len(text))
        ran = random.randrange(0,len(text))
        self.chosenWord = text[ran]
        print(text[ran])
        self.guesses = []
        self.misses = 0
        self.repaint()

        #Guess Letter, reveal part of word
        self.btn.clicked.connect(self.getLetter)
        print()

    def getLetter(self):
        choice = self.textbox.text()
        if choice in self.guesses:
            return
        self.guesses.append(choice)
        # self.comboBox.activated.connect(self.react)

        print(choice) #This is where I change the underscore to the letter if guessed correctly
        disp = ''
        for c in self.chosenWord: #self.chosenWord is the random word from the selected file
            if c in self.guesses: #c is each letter, changes to underscore initially and back when guessed
                disp = disp + c + ' '
            else:
                disp = disp + '_ '
        self.displayword.setText(disp)
        self.misses = 0
        for g in self.guesses:
            if not g in self.chosenWord:
                self.misses = self.misses + 1
        self.repaint()

        done = True
        for c in self.chosenWord:
            if not c in self.guesses:
                done = False
        if done:
            dialog = QMessageBox()
            dialog.setWindowTitle("Game Over")
            dialog.setText("You've saved him!\n \nThank You For Playing")
            dialog.exec()

        if self.misses >= 6:
                dialog = QMessageBox()
                dialog.setWindowTitle("Game Over")
                dialog.setText("There's No Saving Him Now \n \nThank You for Playing!")
                dialog.exec()

    def btnPressEvent(self,event):
        if count >= 1:
            qp.drawEllipse(9*colsize, 4*rowsize, colsize*2, rowsize*2)

        if choice not in text[ran]:
            qp.drawEllipse(9*colsize, 4*rowsize, colsize*2, rowsize*2)

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()