from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QLabel, QFileDialog, QSpinBox
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
        self.label3 = QtWidgets.QLabel()
        self.button1 = QtWidgets.QPushButton()
        self.button2 = QtWidgets.QPushButton()
        self.button_encrypt = QtWidgets.QPushButton()
        self.button_decrypt = QtWidgets.QPushButton()
        
        
        self.fname = None
        self.image = None

        self.iniUI()

    # Buttons
    def iniUI(self):
        
        w = QtWidgets.QWidget()
        self.setCentralWidget(w)
        grid = QtWidgets.QGridLayout(w)

        self.button1.setText("Open file")
        self.button1.setMinimumWidth(150)
        self.fname = self.button1.clicked.connect(self.clicker)
        self.button2.setText("Exit")
        self.button2.clicked.connect(self.close)
        self.button_encrypt.setText("Encrypt image")
        self.button_encrypt.clicked.connect(self.crypting)

        self.button_decrypt.setText("Decrypt image")
        self.button_decrypt.clicked.connect(self.decrypting)

        self.spin_i = QSpinBox()
        self.spin_i.setMinimum(10)
        self.spin_i.setMaximum(50)

        label_i = QLabel()
        label_i.setText("Parametr i:")
        
        
        self.spin_j = QSpinBox()
        self.spin_j.setMinimum(1)
        self.spin_j.setMaximum(5)

        label_j = QLabel()
        label_j.setText("Parametr j:")


        self.spin_i_d = QSpinBox()
        self.spin_i_d.setMinimum(10)
        self.spin_i_d.setMaximum(50)

        label_i_d = QLabel()
        label_i_d.setText("Parametr i:")
        
        
        self.spin_j_d = QSpinBox()
        self.spin_j_d.setMinimum(1)
        self.spin_j_d.setMaximum(5)

        label_j_d= QLabel()
        label_j_d.setText("Parametr j:")
        


        grid.addWidget(self.button1, 2, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)

        grid.addWidget(self.label, 2, 1, Qt.AlignLeft |Qt.AlignCenter )

        grid.addWidget(label_i, 1, 2, Qt.AlignCenter |Qt.AlignCenter )
        grid.addWidget(label_j, 0, 2, Qt.AlignCenter |Qt.AlignCenter )

        grid.addWidget(self.button_encrypt, 2, 3, QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)
        grid.addWidget(self.spin_i, 1, 3, QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        grid.addWidget(self.spin_j, 0, 3, QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)

        grid.addWidget(self.label2, 2, 4, Qt.AlignRight | Qt.AlignCenter )

        grid.addWidget(label_i_d, 1, 5, Qt.AlignLeft |Qt.AlignCenter )
        grid.addWidget(label_j_d, 0, 5, Qt.AlignLeft |Qt.AlignCenter )
        
        

        grid.addWidget(self.button_decrypt, 2, 6, QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)
        grid.addWidget(self.spin_i_d, 1, 6, QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        grid.addWidget(self.spin_j_d, 0, 6, QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)

        grid.addWidget(self.label3, 2, 7, Qt.AlignRight | Qt.AlignCenter )
        grid.addWidget(self.button2, 2, 8, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
       
   
 
    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "c:\\", "Images (*.png *.xpm *.jpg)")

        self.fname = fname

        self.pixmap = QPixmap(fname[0])
        print(fname[0])

        self.label.setPixmap(self.pixmap)

        
        
    def crypting(self):
        image = f.encrypt(self.fname[0], iter_i = self.spin_i.value(), iter_j = self.spin_j.value())

        self.image = image

        height, width, channel = image.shape
        bytesPerLine = 3 * width
        qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)

        self.label2.setPixmap(QPixmap(qImg))
    
    def decrypting(self):
        
        image = f.decrypt(self.image, iter_i = self.spin_i_d.value(), iter_j = self.spin_j_d.value()).astype(np.uint8)
        
        io.imsave('plik.png', image)

        image = io.imread('plik.png', image)

        #print('okej')
        #height, width = image.shape
        #bytesPerLine = 3 * width
        #img = QImage(image.tobytes(), width, height, bytesPerLine, QImage.Format_Grayscale8)
        #print('okej')

        #self.label3.setPixmap(QPixmap(img))
        #print('okej')

    
def window():
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec_())

window()

