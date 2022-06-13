import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Signal(QObject):
    signal = pyqtSignal()

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.sig = Signal()
        self.sig.signal.connect(self.close)

        self.setGeometry(50, 50, 300, 300)
        self.show()

    def mousePressEvent(self, QMouseEvent):
        self.sig.signal.emit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())