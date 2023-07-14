from PyQt5.QtCore import Qt
# Importamo stvari iz pyqt5
from PyQt5.QtWidgets import (
       QApplication, QWidget, QVBoxLayout,
       QPushButton, QLabel)

# Importamo iz drugih fileova
from instr import *
from second_win import *

# Klasa mainwin je sin od QWidget
class MainWin(QWidget):

    # Konstruktor za prozor
    def __init__(self):
        # Prvo zovemo konstruktor od tate
        super().__init__()
        # Postavljamo izgled prozora
        self.set_appear()
        # Pokrecemo elemente prozora(tekst, gumbe...)
        self.initUI()
        # Connects sluzi za spajanje gumba sa odredenom funkcijom
        self.connects()
        # Show moramo pozvati da se prozor vidi
        self.show()

    # Funkcija za elemente na ekranu
    def initUI(self):
        # Stvaramo elemente
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        # Dodajemo elemente u vertikalni poredak
        self.layout = QVBoxLayout()
        # Elemente dodajemo funkcijom addWidget
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)   
        # Obavezno postaviti layout na cijeli window      
        self.setLayout(self.layout)
   
   # Funkcija koju spojimo sa gumbom
    def next_click(self):
        # Pokazi drugi prozor
        self.tw = TestWin()
        # Sakrij prvi prozor
        self.hide()

    # Funkcija za povezivanje gumba sa funkcijom
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    # Funkcija za postavljanje visine, sirine itd..
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

def main():
    app = QApplication([])
    mw = MainWin()
    app.exec_()

# Tu pocinje program
main()
