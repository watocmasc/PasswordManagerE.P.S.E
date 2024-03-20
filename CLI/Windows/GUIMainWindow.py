from PyQt6 import QtWidgets, QtCore, QtGui
import time

class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText('Close window')
        self.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.resize(300, 70)
        self.setWindowTitle('Passwords manager')
    
    def load_data(self, sp):
        for i in range(1, 11):
            sp.showMessage(f'Loading of datas... {i*10}%',
                QtCore.Qt.AlignmentFlag.AlignHCenter |
                QtCore.Qt.AlignmentFlag.AlignBottom,
                QtCore.Qt.GlobalColor.black
                           )
            #QtWidgets.QApplication.instance().processEvents()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())