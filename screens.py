from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont

class Window1(QWidget):

    def __init__(self):

        super().__init__()

        self.set_appearance()

        self.initUI()

        self.connect_button()

        self.show()

    def set_appearance(self):
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setWindowTitle('Health')

    def initUI(self):
        self.red1 = QHBoxLayout()
        self.tekst1 = QLabel('Welcome to the Health status detection program!')
        self.red1.addWidget(self.tekst1)

        self.red2 = QHBoxLayout()
        self.tekst2 = QLabel('This application allows you to use the Rufier test to make an initial diagnosis of your health.\n'
                        + 'The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.\n'
                        + 'The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;\n'
                        + 'then, within 45 seconds, the subject performs 30 squats.\n'
                        + 'When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\n'
                        + 'and then for the last 15 seconds of the first minute of the recovery period.\n'
                        + 'Important! If you feel unwell during the test (dizziness,\n'
                        + 'tinnitus, shortness of breath, etc.), stop the test and consult a physician.')
        self.red2.addWidget(self.tekst2)

        self.red3 = QHBoxLayout()
        self.gumb = QPushButton('Start')
        self.red3.addWidget(self.gumb, alignment=Qt.AlignCenter)

        self.stupac = QVBoxLayout()
        self.stupac.addLayout(self.red1)
        self.stupac.addLayout(self.red2)
        self.stupac.addLayout(self.red3)

        self.setLayout(self.stupac)

    def next_window(self):
        self.window2 = Window2()
        self.hide()

    def connect_button(self):
        self.gumb.clicked.connect(self.next_window)

class Window2(QWidget):

    def __init__(self):

        super().__init__()

        self.set_appearance()

        self.initUI()

        self.connect_button()

        self.show()
        
    def set_appearance(self):
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setWindowTitle('Health')
   
    def initUI(self):
        self.stup1 = QVBoxLayout()

        self.tekst1 = QLabel('Enter your full name:')
        self.input_name = QLineEdit()
        self.tekst2 = QLabel('Full years:')
        self.input_years = QLineEdit()
        self.tekst3 = QLabel('Lie on your back and take your pulse for 15 seconds. Click the "Start first test" button to start the timer.\n'
                        + 'Write down the result in the appropriate field.')
        self.gumb_first = QPushButton('Start the first test')
        self.input_first_test = QLineEdit()
        self.tekst4 = QLabel('Perform 30 squats in 45 seconds. To do this, click the "Start doing squats" button\n'
                        + 'to start the squat counter.')
        self.gumb_squats = QPushButton('Start doing squats')
        self.tekst5 = QLabel('Lie on your back and take your pulse for the first 15 seconds of the minute, then for the last 15 seconds of the minute.\n'
                        + 'Press the "Start final test" button to start the timer.\n'
                        + 'The seconds that should be measured are indicated in green and the minutes that should not be measured are indicated in black. Write down the results in the appropriate fields.')
        self.gumb_final = QPushButton('Start the final test')
        self.input_predzadnji = QLineEdit()
        self.input_zadnji = QLineEdit()
        self.gumb_posalji = QPushButton('Send the results')

        self.widgeti = []
        self.widgeti.append(self.tekst1)
        self.widgeti.append(self.input_name)
        self.widgeti.append(self.tekst2)
        self.widgeti.append(self.input_years)
        self.widgeti.append(self.tekst3)
        self.widgeti.append(self.gumb_first)
        self.widgeti.append(self.input_first_test)
        self.widgeti.append(self.tekst4)
        self.widgeti.append(self.gumb_squats)
        self.widgeti.append(self.tekst5)
        self.widgeti.append(self.gumb_final)
        self.widgeti.append(self.input_predzadnji)
        self.widgeti.append(self.input_zadnji)

        self.redci = []
        for i in self.widgeti:
            red = QHBoxLayout()
            red.addWidget(i, alignment=Qt.AlignLeft)
            self.redci.append(red)

        red = QHBoxLayout()
        red.addWidget(self.gumb_posalji, alignment=Qt.AlignCenter)
        self.redci.append(red)

        for i in self.redci:
            self.stup1.addLayout(i)

        self.stup2 = QVBoxLayout()
        self.timerLabel = QLabel('00:00:00')
        self.timerLabel.setFont(QFont('Arial', 30))
        self.stup2.addWidget(self.timerLabel, alignment=Qt.AlignRight)

        self.timer15 = Timer(15, self)
        self.timer45 = Timer(45, self)
        self.timer60 = TimerColor(60, self)
        self.gumb_first.clicked.connect(self.timer15.start_count)
        self.gumb_squats.clicked.connect(self.timer45.start_count)
        self.gumb_final.clicked.connect(self.timer60.start_count)

        self.redakGlavni = QHBoxLayout()
        self.redakGlavni.addLayout(self.stup1)
        self.redakGlavni.addLayout(self.stup2)

        self.setLayout(self.redakGlavni)

    def next_window(self):
        if self.input_years.text().isnumeric() and self.input_first_test.text().isnumeric() and self.input_predzadnji.text().isnumeric() and self.input_zadnji.text().isnumeric():
            self.hide()
            self.window3 = Window3()
            years = int(self.input_years.text())
            index = (4 * (int(self.input_first_test.text()) + int(self.input_predzadnji.text()) + int(self.input_zadnji.text())) - 200) / 10
            self.window3.tekst1.setText('Rufier index: ' + str(index))
            self.window3.tekst2.setText('Cardiac performance: ' + getCardiacPerformance(years, index))
    
    def connect_button(self):
        self.gumb_posalji.clicked.connect(self.next_window)

class Window3(QWidget):

    def __init__(self):

        super().__init__()

        self.set_appearance()

        self.initUI()

        self.show()

    def set_appearance(self):
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setWindowTitle('Health')

    def initUI(self):
        self.red1 = QHBoxLayout()
        self.tekst1 = QLabel('Rufier index: 0')
        self.red1.addWidget(self.tekst1, alignment=Qt.AlignCenter)

        self.red2 = QHBoxLayout()
        self.tekst2 = QLabel('Cardiac performance: ')
        self.red2.addWidget(self.tekst2, alignment=Qt.AlignCenter)

        self.stupac = QVBoxLayout()
        self.stupac.addLayout(self.red1)
        self.stupac.addLayout(self.red2)

        self.setLayout(self.stupac)
        
class Timer:

    def __init__(self, seconds, window):
        self.start = False
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.count)
        self.defaultSeconds = seconds
        self.counter = seconds
        self.window = window

    def start_count(self):
        self.start = True

    def count(self):
        if self.start:
            if self.counter > 9:
                self.window.timerLabel.setText('00:00:' + str(self.counter))
            else:
                self.window.timerLabel.setText('00:00:0' + str(self.counter))
            self.counter -= 1
            if self.counter < 0:
                self.start = False
                self.window.timerLabel.setText('00:00:00')
                self.counter = self.defaultSeconds

class TimerColor(Timer):

    def count(self):

        if self.start:

            if self.counter <= 60 and self.counter >= 45 or self.counter <= 15 and self.counter >= 0:

                self.window.timerLabel.setStyleSheet('color: lime')

                if self.counter > -1 and self.counter < 10:
                    self.window.timerLabel.setText('00:00:0' + str(self.counter))
                else:
                    self.window.timerLabel.setText('00:00:' + str(self.counter))

            else:
                self.window.timerLabel.setStyleSheet('color: black')
                self.window.timerLabel.setText('00:00:' + str(self.counter))

            self.counter -= 1

            if self.counter < 0:
                self.start = False
                self.window.timerLabel.setStyleSheet('color: black')
                self.window.timerLabel.setText('00:00:00')
                self.counter = self.defaultSeconds

def getCardiacPerformance(years, index):

    if years > 15:
        years = 15
    elif years < 7:
        years = 7

    keyList = list(table[years].keys())
    key = None
    
    for i in range(5):
        
        if i == 0:

            if index >= keyList[i]:
                key = keyList[i]
                break
            
        elif i == 4:

            if index <= keyList[i]:
                key = keyList[i]
                break
            
        else:

            if index < keyList[i - 1] and index >= keyList[i]:
                key = keyList[i]
                break

    return table[years][key]

table = {7: {21 : 'low', 17: 'satisfactory', 12: 'average', 6.5: 'above average', 6.4: 'high'},
           8: {21 : 'low', 17: 'satisfactory', 12: 'average', 6.5: 'above average', 6.4: 'high'},
           9: {19.5 : 'low', 15.5: 'satisfactory', 10.5: 'average', 5: 'above average', 4.9: 'high'},
           10: {19.5 : 'low', 15.5: 'satisfactory', 10.5: 'average', 5: 'above average', 4.9: 'high'},
           11: {18 : 'low', 14: 'satisfactory', 9: 'average', 3.5: 'above average', 3.4: 'high'},
           12: {18 : 'low', 14: 'satisfactory', 9: 'average', 3.5: 'above average', 3.4: 'high'},
           13: {16.5 : 'low', 12.5: 'satisfactory', 7.5: 'average', 2: 'above average', 1.9: 'high'},
           14: {16.5 : 'low', 12.5: 'satisfactory', 7.5: 'average', 2: 'above average', 1.9: 'high'},
           15: {15 : 'low', 11: 'satisfactory', 6: 'average', 0.5: 'above average', 0.4: 'high'}}

win_x, win_y = 200, 100

win_width, win_height = 1000, 600