from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog, QGridLayout
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #uic.loadUi("...", self)
        self.interfejs()
        #self.button  = QPushButton()
        

        
    
    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "c:\\", "All files")

        self.pixmap = QPixmap(fname[0])

        self.label.setPixmap(self.pixmap)


    def interfejs(self):

            
            self.setWindowTitle("Prosty kalkulator")
            # etykiety
            etykieta1 = QLabel("Liczba 1:", self)
            etykieta2 = QLabel("Liczba 2:", self)
            etykieta3 = QLabel("Wynik:", self)

            # przypisanie widgetów do układu tabelarycznego
            ukladT = QGridLayout()
            ukladT.addWidget(etykieta1, 0, 0)
            ukladT.addWidget(etykieta2, 0, 1)
            ukladT.addWidget(etykieta3, 0, 2)

            # przypisanie utworzonego układu do okna
            # 1-liniowe pola edycyjne
            self.liczba1Edt = QLineEdit()
            self.liczba2Edt = QLineEdit()
            self.wynikEdt = QLineEdit()

            self.wynikEdt.readonly = True
            self.wynikEdt.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')

            ukladT.addWidget(self.liczba1Edt, 1, 0)
            ukladT.addWidget(self.liczba2Edt, 1, 1)
            ukladT.addWidget(self.wynikEdt, 1, 2)

            # przyciski
            dodajBtn = QPushButton("&Dodaj", self)
            odejmijBtn = QPushButton("&Odejmij", self)
            dzielBtn = QPushButton("&Mnóż", self)
            mnozBtn = QPushButton("D&ziel", self)
            koniecBtn = QPushButton("&Koniec", self)
            koniecBtn.resize(koniecBtn.sizeHint())

            ukladH = QHBoxLayout()
            ukladH.addWidget(dodajBtn)
            ukladH.addWidget(odejmijBtn)
            ukladH.addWidget(dzielBtn)
            ukladH.addWidget(mnozBtn)

            ukladT.addLayout(ukladH, 2, 0, 1, 3)
            ukladT.addWidget(koniecBtn, 3, 0, 1, 3)
            self.setLayout(ukladT)

            self.setGeometry(20, 20, 300, 100)
            self.show()
           


if __name__ == '__main__':
    

    app = QApplication(sys.argv)
    okno = UI()
    sys.exit(app.exec_())