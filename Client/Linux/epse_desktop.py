import sys, json
from PySide6.QtCore import *
from PySide6.QtWidgets import *

class CreateBlock(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setMinimumHeight(200)
        self.setMinimumWidth(400)
        #self.setWindowTitle("Add block of data")

        self.place_title = QLineEdit("Title")
        self.place_title.setObjectName('place_title')

        self.place_login = QLineEdit("Login")
        self.place_login.setObjectName('place_login')
        
        self.place_password = QLineEdit("Password")
        self.place_password.setObjectName('place_password')
        
        self.btn_cancel = QPushButton("Done")
        self.btn_cancel.setMaximumWidth(80)
        self.btn_cancel.setMinimumWidth(80)
        self.btn_cancel.setMaximumHeight(50)
        self.btn_cancel.setMinimumHeight(50)
        self.btn_cancel.clicked.connect(lambda: self.close())
        self.btn_cancel.setObjectName('btn_done')

        self.btn_done = QPushButton("Cancel")
        self.btn_done.setMaximumWidth(80)
        self.btn_done.setMinimumWidth(80)
        self.btn_done.setMaximumHeight(50)
        self.btn_done.setMinimumHeight(50)
        self.btn_done.clicked.connect(self.done)
        self.btn_done.setObjectName('btn_cancel')

        self.place_titleLogPass = QVBoxLayout()
        self.place_titleLogPass.addWidget(self.place_title)
        self.place_titleLogPass.addWidget(self.place_login)
        self.place_titleLogPass.addWidget(self.place_password)

        self.place_menuOfBtns = QHBoxLayout()
        self.place_menuOfBtns.addWidget(self.btn_cancel)
        self.place_menuOfBtns.addWidget(self.btn_done)

        self.field_titleLogPass = QWidget()
        self.field_titleLogPass.setLayout(self.place_titleLogPass)

        self.field_btns = QWidget()
        self.field_btns.setLayout(self.place_menuOfBtns)

        self.dialog_window = QVBoxLayout()
        self.dialog_window.addWidget(self.field_titleLogPass)
        self.dialog_window.addWidget(self.field_btns)

        self.setLayout(self.dialog_window)

    def done(self):
        with open('data.json', 'r') as file:
            data = json.load(file)

        # добавляем новое значение в JSON данные
        data['datas']['новый_ключ'] = 'новое_значение'

        # открываем JSON файл для записи
        with open('data.json', 'w') as file:
            json.dump(data, file)

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # Window Dialog
        self.window_addBlock = CreateBlock()

        # Propertions of main window
        self.setMinimumHeight(500)
        self.setMinimumWidth(400)

        self.blocks_of_data = QListWidget()
        self.blocks_of_data.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.blocks_of_data.setObjectName('blocks_of_data')

        with open('data.json', 'r') as file:
            data = json.load(file)
        queue_block = 1
        for i in data['datas'].keys():
            item = QListWidgetItem(f" {queue_block} {i} | {" ".join(data['datas'][i])}")
            ##item.setTextAlignment(Qt.AlignCenter)
            self.blocks_of_data.addItem(item)
            queue_block += 1

        self.btn_Exit = QPushButton("Exit")
        self.btn_Exit.setMaximumWidth(80)
        self.btn_Exit.setMinimumWidth(80)
        self.btn_Exit.setMaximumHeight(50)
        self.btn_Exit.setMinimumHeight(50)
        self.btn_Exit.clicked.connect(self.exit_from_app)
        self.btn_Exit.setObjectName('btn_Exit')

        self.btn_delBlock = QPushButton("Delete")
        self.btn_delBlock.setMaximumWidth(80)
        self.btn_delBlock.setMinimumWidth(80)
        self.btn_delBlock.setMaximumHeight(50)
        self.btn_delBlock.setMinimumHeight(50)
        self.btn_delBlock.clicked.connect(self.del_block_of_data)
        self.btn_delBlock.setObjectName('btn_delBlock')

        self.btn_addBlock = QPushButton("Add")
        self.btn_addBlock.setMaximumWidth(80)
        self.btn_addBlock.setMinimumWidth(80)
        self.btn_addBlock.setMaximumHeight(50)
        self.btn_addBlock.setMinimumHeight(50)
        self.btn_addBlock.clicked.connect(self.add_block_of_data)
        self.btn_addBlock.setObjectName('btn_addBlock')

        self.content = QVBoxLayout()
        self.content.addWidget(self.blocks_of_data)

        self.btn_panel = QHBoxLayout()
        self.btn_panel.addWidget(self.btn_addBlock)
        self.btn_panel.addWidget(self.btn_delBlock)
        self.btn_panel.addWidget(self.btn_Exit)

        self.table_of_blocks = QWidget()
        self.table_of_blocks.setLayout(self.content)

        self.main_btns = QWidget()
        self.main_btns.setLayout(self.btn_panel)

        self.main_window = QVBoxLayout()
        self.main_window.addWidget(self.table_of_blocks)
        self.main_window.addWidget(self.main_btns)

        self.setLayout(self.main_window)

    def add_block_of_data(self):
        self.window_addBlock.show()

    def del_block_of_data(self):
        pass

    def exit_from_app(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication()

    w = Widget()
    w.show()

    with open("style.qss", 'r') as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())