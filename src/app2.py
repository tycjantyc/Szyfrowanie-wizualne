from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QLabel, QFileDialog
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import skimage.io as io
import funkcje_pischarnik as f
import numpy as np

class Okno(QMainWindow):
    def __init__(self):
        super(Okno, self).__init__()
        self.setGeometry(500, 500, 900, 500)
        self.setWindowTitle("My window")
        self.label = QtWidgets.QLabel()
        self.label2 = QtWidgets.QLabel()
        self.button1 = QtWidgets.QPushButton()
        self.button2 = QtWidgets.QPushButton()
        self.label = QLabel()
        self.iniUI()

    # Buttons
    def iniUI(self):
        w = QtWidgets.QWidget()
        self.setCentralWidget(w)
        grid = QtWidgets.QGridLayout(w)

        self.button1.setText("Open file")
        self.button1.setMinimumWidth(150)
        self.button1.clicked.connect(self.clicker)
        self.button2.setText("Exit")
        self.button2.clicked.connect(self.close)

        grid.addWidget(self.button1, 0, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
        grid.addWidget(self.label, 0, 1, Qt.AlignLeft |Qt.AlignCenter )
        grid.addWidget(self.label2, 0, 2, Qt.AlignRight | Qt.AlignCenter )
        grid.addWidget(self.button2, 0, 3, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
       
   
   

    def open_file(self):
        print("Open file")
    
    

    
    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "c:\\", "Images (*.png *.xpm *.jpg)")

        self.pixmap = QPixmap(fname[0])
        print(fname[0])

        self.label.setPixmap(self.pixmap)

        image = f.encrypt(fname[0])
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

        self.label2.setPixmap(QPixmap(qImg))
    
def window():
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec_())

window()