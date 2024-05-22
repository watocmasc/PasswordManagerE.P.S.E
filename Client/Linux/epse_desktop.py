import sys, json
from PySide6.QtCore import *
from PySide6.QtWidgets import *

class CreateBlock(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setMinimumHeight(200)
        self.setMinimumWidth(400)
        #self.setWindowTitle("Add block of data")

        self.place_title = QLineEdit()
        self.place_title.setObjectName('place_title')

        self.place_login = QLineEdit()
        self.place_login.setObjectName('place_login')
        
        self.place_password = QLineEdit()
        self.place_password.setObjectName('place_password')
        
        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.setMaximumWidth(80)
        self.btn_cancel.setMinimumWidth(80)
        self.btn_cancel.setMaximumHeight(50)
        self.btn_cancel.setMinimumHeight(50)
        self.btn_cancel.clicked.connect(self.close_window)
        self.btn_cancel.setObjectName('btn_cancel')

        self.btn_done = QPushButton("Done")
        self.btn_done.setMaximumWidth(80)
        self.btn_done.setMinimumWidth(80)
        self.btn_done.setMaximumHeight(50)
        self.btn_done.setMinimumHeight(50)
        self.btn_done.clicked.connect(self.done_window)
        self.btn_done.setObjectName('btn_done')

        self.place_titleLogPass = QVBoxLayout()
        self.place_titleLogPass.addWidget(self.place_title)
        self.place_titleLogPass.addWidget(self.place_login)
        self.place_titleLogPass.addWidget(self.place_password)

        self.place_menuOfBtns = QHBoxLayout()
        self.place_menuOfBtns.addWidget(self.btn_done)
        self.place_menuOfBtns.addWidget(self.btn_cancel)
        
        self.field_titleLogPass = QWidget()
        self.field_titleLogPass.setLayout(self.place_titleLogPass)

        self.field_btns = QWidget()
        self.field_btns.setLayout(self.place_menuOfBtns)

        self.dialog_window = QVBoxLayout()
        self.dialog_window.addWidget(self.field_titleLogPass)
        self.dialog_window.addWidget(self.field_btns)

        self.setLayout(self.dialog_window)

    def close_window(self):
        return self.close()

    def done_window(self):
        with open('data.json', 'r') as file:
            base = json.load(file)

        # new block in base
        if self.place_title.text() and (self.place_login.text() or self.place_password.text()):
            base['datas'][self.place_title.text()] = [self.place_login.text(), self.place_password.text()]

        with open('data.json', 'w') as file:
            json.dump(base, file)
        
        self.place_title.clear()
        self.place_login.clear()
        self.place_password.clear()
        return self.close()

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # Window Dialog
        self.window_addBlock = CreateBlock()

        # Propertions of main window
        self.setMinimumHeight(500)
        self.setMinimumWidth(400)

        # for all blocks of datas
        self.all_blocks = []

        self.blocks_of_data = QListWidget()
        self.blocks_of_data.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.blocks_of_data.setObjectName('blocks_of_data')

        # content of main window
        with open('data.json', 'r') as file:
            base = json.load(file)
        queue_block = 1
        for i in base['datas'].keys():
            self.all_blocks.append(f" {queue_block}. {i} | {" ".join(base['datas'][i])}")
            queue_block += 1
        queue_block = 1
        for k in self.all_blocks:
            self.blocks_of_data.addItem(k)

        self.btn_Exit = QPushButton("Exit")
        self.btn_Exit.setMaximumWidth(80)
        self.btn_Exit.setMinimumWidth(80)
        self.btn_Exit.setMaximumHeight(50)
        self.btn_Exit.setMinimumHeight(50)
        self.btn_Exit.clicked.connect(self.exit_from_app)
        self.btn_Exit.setObjectName('btn_Exit')

        self.btn_updating = QPushButton("Update")
        self.btn_updating.setMaximumWidth(80)
        self.btn_updating.setMinimumWidth(80)
        self.btn_updating.setMaximumHeight(50)
        self.btn_updating.setMinimumHeight(50)
        self.btn_updating.clicked.connect(self.updating)
        self.btn_updating.setObjectName('btn_updating')

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
        self.btn_panel.addWidget(self.btn_updating)
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

    # updating of content for main window
    def updating(self):
        self.blocks_of_data.clear()
        self.all_blocks = []
        with open('data.json', 'r') as file:
            base = json.load(file)
        queue_block = 1
        for i in base['datas'].keys():
            self.all_blocks.append(f" {queue_block}. {i} | {" ".join(base['datas'][i])}")
            queue_block += 1
        queue_block = 1
        for k in self.all_blocks:
            self.blocks_of_data.addItem(k)

    # deletes a block of data from the manager
    def del_block_of_data(self):

        # selected block of data
        selectedBlock = self.blocks_of_data.currentItem()
        numberBlock = ""
        for num in selectedBlock.text():
            if num != '.':
                numberBlock += num
            else:
                break
        
        ####################################
        #
        with open('data.json', 'r') as file:
            base = json.load(file)

        # find the necessary element to delete
        # and delete it
        count = 0
        key_in_base = ""
        for key in base['datas']:
            if count == int(numberBlock)-1:
                key_in_base = key
                break
            count += 1
        del base['datas'][key_in_base]

        with open('data.json', 'w') as file:
            json.dump(base, file)
        #
        ####################################

        self.updating() # update manager window

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