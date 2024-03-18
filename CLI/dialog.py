from PyQt6 import QtWidgets, QtCore
import main

sum_ = []
action = ''

class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.MyWidget = main.MyWindow()
        self.MyWidget.vbox.setContentsMargins(10,0,10,0)
        self.but_start = QtWidgets.QPushButton('Start')
        mainBox = QtWidgets.QVBoxLayout()
        mainBox.addWidget(self.MyWidget)
        mainBox.addWidget(self.but_start)
        
        self.setLayout(mainBox)
        self.but_start.clicked.connect(self.add_str)
        
    
    def add_str(self):
        
        
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle('Dialog')
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec())