import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initWindow()


    def initWindow(self):
        lcd = QLCDNumber(self)  # 슬롯
        dial = QDial(self)  # 시그널
        btn1 = QPushButton('BIG', self)
        btn2 = QPushButton('SMALL', self)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)
        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeSmall)

        self.setGeometry(50, 50, 200, 200)
        self.show()

    def resizeBig(self):
        self.resize(400, 400)

    def resizeSmall(self):
        self.resize(150, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
