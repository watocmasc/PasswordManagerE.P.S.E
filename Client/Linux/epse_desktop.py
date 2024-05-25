import sys, json
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PyQt6.QtGui import *

class PasswordGeneration(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(200)
        self.setMinimumWidth(400)

        self.place_new_password = QLineEdit()
        self.place_new_password.setPlaceholderText(" "+"Password length")
        self.place_new_password.setMaximumHeight(50)
        self.place_new_password.setMinimumHeight(50)
        self.place_new_password.setObjectName('place_new_password')

        self.btn_generate = QPushButton("Generate")
        self.btn_generate.setMaximumWidth(100)
        self.btn_generate.setMinimumWidth(100)
        self.btn_generate.setMaximumHeight(50)
        self.btn_generate.setMinimumHeight(50)
        self.btn_generate.clicked.connect(self.generate_password)
        self.btn_generate.setObjectName('btn_generate')

        self.btn_cancel = QPushButton()
        self.btn_cancel.setMaximumWidth(100)
        self.btn_cancel.setMinimumWidth(100)
        self.btn_cancel.setMaximumHeight(50)
        self.btn_cancel.setMinimumHeight(50)
        self.btn_cancel.clicked.connect(self.close_window)
        self.btn_cancel.setObjectName('btn_Exit')

        self.place_btns = QHBoxLayout()
        self.place_field_password = QVBoxLayout()
        self.place = QVBoxLayout()

        self.part1_window = QWidget()
        self.part2_window = QWidget()

        self.place_btns.addWidget(self.btn_generate)
        self.place_btns.addWidget(self.btn_cancel)
        self.place_field_password.addWidget(self.place_new_password)

        self.part1_window.setLayout(self.place_field_password)
        self.part2_window.setLayout(self.place_btns)

        self.place.addWidget(self.part1_window)
        self.place.addWidget(self.part2_window)

        self.setLayout(self.place)

    def generate_password(self):
        import random as rt
        new_password = ""
        try:
            length_password = int(self.place_new_password.text().strip())
            symbols = '1234567890-=_+!@#$%^&*()`~[]{};:\'\\/|.,<>qazxswedcrfvtgbyhnujmiklopQWERTYUIOPASDFGHJKLZXCVBNM'
            for i in range(length_password):
                new_password += symbols[rt.randint(0,len(symbols)-1)]
            self.place_new_password.setText(f'{new_password}')
        except:
            pass

    def close_window(self):
        return self.close()

class ContentBlock(QWidget):
    def __init__(self, number_of_block, title_block, value_of_block):
        super().__init__()
            
        self.setWindowTitle("Block information")

        # Propertions of main window
        self.setMinimumHeight(200)
        self.setMinimumWidth(300)

        self.move(490, 290)

        self.number_of_block = number_of_block
        self.value_of_block = value_of_block

        self.title_block = QLineEdit(f' {title_block}')
        self.title_block.setMinimumHeight(50)
        self.title_block.setMinimumWidth(100)
        self.title_block.setObjectName('item_info')

        self.title_and_values_of_block = [] 

        # Creates a list of block 
        # values and also adds its name
        self.all_info = QVBoxLayout()
        self.all_info.setObjectName('all_info')
        self.title_and_values_of_block.append(self.title_block)
        for value in self.value_of_block:
            value = QLineEdit(f' {value}')
            value.setMinimumHeight(50)
            value.setMinimumWidth(100)
            value.setObjectName('item_info')
            self.title_and_values_of_block.append(value)
        for value in self.title_and_values_of_block:
            self.all_info.addWidget(value)

        # Buttons #######################################
        self.btn_save = QPushButton()
        self.btn_save.setMaximumWidth(60)
        self.btn_save.setMinimumWidth(60)
        self.btn_save.setMaximumHeight(60)
        self.btn_save.setMinimumHeight(60)
        self.btn_save.clicked.connect(self.save_changes)
        self.btn_save.setObjectName('btn_done')

        self.btn_cancel = QPushButton()
        self.btn_cancel.setMaximumWidth(60)
        self.btn_cancel.setMinimumWidth(60)
        self.btn_cancel.setMaximumHeight(60)
        self.btn_cancel.setMinimumHeight(60)
        self.btn_cancel.clicked.connect(self.close_window)
        self.btn_cancel.setObjectName('btn_Exit')
        # Buttons #######################################

        # Menu layout #######################################
        self.menu_btn = QHBoxLayout()
        self.menu_btn.addWidget(self.btn_save)
        self.menu_btn.addWidget(self.btn_cancel)

        self.part1_window = QWidget()
        self.part1_window.setLayout(self.all_info)
        
        self.part2_window = QWidget()
        self.part2_window.setLayout(self.menu_btn)

        self.main_window = QVBoxLayout()
        self.main_window.addWidget(self.part1_window)
        self.main_window.addWidget(self.part2_window)

        self.setLayout(self.main_window)
        # Menu layout #######################################
        
    def save_changes(self):

        with open('data.json', 'r') as file:
            base = json.load(file)

        # Finds the required data block, 
        # deletes the old value and writes a new one to it
        score_key = 0
        for key in list(base['datas'].keys()):
            if score_key == self.number_of_block: 
                del base['datas'][key] # old value
                # new value
                base['datas'][self.title_and_values_of_block[0].text().strip()] = [k.text().strip() for k in self.title_and_values_of_block[1:]]
            score_key += 1

        with open('data.json', 'w') as file:
            json.dump(base, file)

        self.close()

    def close_window(self):
        self.close()

class CreateBlock(QDialog):
    def __init__(self, parent=None):
        super().__init__()

        self.setWindowTitle("EPSE: Adding new data")
        self.setMinimumHeight(200)
        self.setMinimumWidth(400)

        # Buttons and Fields #######################################
        self.place_title = QLineEdit()
        self.place_title.setMinimumHeight(50)
        self.place_title.setPlaceholderText(" "+"Title")
        self.place_title.setObjectName('place_title')

        self.place_content = QLineEdit()
        self.place_content.setMinimumHeight(50)
        self.place_content.setPlaceholderText(" "+"Content")
        self.place_content.setObjectName('place_content')
        
        self.btn_cancel = QPushButton()
        self.btn_cancel.setMaximumWidth(60)
        self.btn_cancel.setMinimumWidth(60)
        self.btn_cancel.setMaximumHeight(60)
        self.btn_cancel.setMinimumHeight(60)
        self.btn_cancel.clicked.connect(self.close_window)
        self.btn_cancel.setObjectName('btn_Exit')

        self.btn_done = QPushButton()
        self.btn_done.setMaximumWidth(60)
        self.btn_done.setMinimumWidth(60)
        self.btn_done.setMaximumHeight(60)
        self.btn_done.setMinimumHeight(60)
        self.btn_done.clicked.connect(self.done_window)
        self.btn_done.setObjectName('btn_done')
        # Buttons and Fields #######################################

        # Menu layout #######################################
        self.place_titleLogPass = QVBoxLayout()
        self.place_titleLogPass.addWidget(self.place_title)
        self.place_titleLogPass.addWidget(self.place_content)

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
        # Menu layout #######################################

    def close_window(self):
        return self.close()

    def done_window(self):
        with open('data.json', 'r') as file:
            base = json.load(file)

        # new block in base
        if self.place_title.text() and self.place_content.text():
            base['datas'][self.place_title.text()] = self.place_content.text().split()

        with open('data.json', 'w') as file:
            json.dump(base, file)
        
        self.place_title.clear()
        self.place_content.clear()
        return self.close()

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Propertions of main window
        self.setWindowTitle("EPSE")
        self.setMinimumHeight(500)
        self.setMinimumWidth(400)
        self.move(790, 290)

        # Additional windows | Create block of data
        self.window_addBlock = CreateBlock()
        self.window_generatePassword = PasswordGeneration()

        # The contents of the main window #######################################

        # for all blocks of datas
        self.titles_blocks = []

        # A list of all data for further display
        self.blocks_of_data = QListWidget()
        self.blocks_of_data.itemDoubleClicked.connect(self.full_review_of_block)
        self.blocks_of_data.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.blocks_of_data.setObjectName('blocks_of_data')

        # content of main window
        with open('data.json', 'r') as file:
            base = json.load(file)
        queue_block = 1
        for title in base['datas'].keys():
            self.titles_blocks.append(f" {queue_block}. {title}")
            queue_block += 1

        for title_item in self.titles_blocks:
            self.blocks_of_data.addItem(title_item)
        # The contents of the main window #######################################

        # Buttons #######################################
        self.btn_Exit = QPushButton()
        self.btn_Exit.setMaximumWidth(60)
        self.btn_Exit.setMinimumWidth(60)
        self.btn_Exit.setMaximumHeight(60)
        self.btn_Exit.setMinimumHeight(60)
        self.btn_Exit.clicked.connect(self.exit_from_app)
        self.btn_Exit.setObjectName('btn_Exit')

        self.btn_updating = QPushButton()
        self.btn_updating.setMaximumWidth(60)
        self.btn_updating.setMinimumWidth(60)
        self.btn_updating.setMaximumHeight(60)
        self.btn_updating.setMinimumHeight(60)
        self.btn_updating.clicked.connect(self.updating)
        self.btn_updating.setObjectName('btn_updateBlocks')

        self.btn_delBlock = QPushButton()
        self.btn_delBlock.setMaximumWidth(60)
        self.btn_delBlock.setMinimumWidth(60)
        self.btn_delBlock.setMaximumHeight(60)
        self.btn_delBlock.setMinimumHeight(60)
        self.btn_delBlock.clicked.connect(self.del_block_of_data)
        self.btn_delBlock.setObjectName('btn_delBlock')

        self.btn_addBlock = QPushButton()
        self.btn_addBlock.setMaximumWidth(60)
        self.btn_addBlock.setMinimumWidth(60)
        self.btn_addBlock.setMaximumHeight(60)
        self.btn_addBlock.setMinimumHeight(60)
        self.btn_addBlock.clicked.connect(self.add_block_of_data)
        self.btn_addBlock.setObjectName('btn_addBlock')

        self.btn_passGeneration = QPushButton('Password generation')
        self.btn_passGeneration.setMaximumWidth(180)
        self.btn_passGeneration.setMinimumWidth(180)
        self.btn_passGeneration.setMaximumHeight(50)
        self.btn_passGeneration.setMinimumHeight(50)
        self.btn_passGeneration.clicked.connect(self.password_generate)
        self.btn_passGeneration.setObjectName('btn_passGenerate')
        # Buttons #######################################

        # Menu layout #######################################
        self.blocks_from_data = QVBoxLayout()
        self.blocks_from_data.addWidget(self.blocks_of_data)

        self.btn_panel_first = QHBoxLayout()
        self.btn_panel_first.addWidget(self.btn_addBlock)
        self.btn_panel_first.addWidget(self.btn_delBlock)
        self.btn_panel_first.addWidget(self.btn_updating)
        self.btn_panel_first.addWidget(self.btn_Exit)

        self.btn_panel_second = QHBoxLayout()
        self.btn_panel_second.addWidget(self.btn_passGeneration)
        
        self.table_of_blocks = QWidget()
        self.table_of_blocks.setLayout(self.blocks_from_data)

        self.main_btns = QWidget()
        self.main_btns.setLayout(self.btn_panel_first)

        self.second_btns = QWidget()
        self.second_btns.setLayout(self.btn_panel_second)

        self.main_window = QVBoxLayout()
        self.main_window.addWidget(self.table_of_blocks)
        self.main_window.addWidget(self.main_btns)
        self.main_window.addWidget(self.second_btns)

        self.setLayout(self.main_window)
        # Menu layout #######################################

    def password_generate(self):
        self.window_generatePassword.show()

    def add_block_of_data(self):
        self.window_addBlock.show()

    # Viewing the contents of the title
    def full_review_of_block(self):
        selectedBlock = self.blocks_of_data.currentItem()
        numberBlock = ""
        for num in selectedBlock.text():
            if num != '.':
                numberBlock += num
            else:
                break
        with open('data.json', 'r') as file:
            base = json.load(file)

        count = 0
        key_in_base = ""
        for key in base['datas']:
            if count == int(numberBlock)-1:
                key_in_base = key
                break
            count += 1
        items = base['datas'][key_in_base] # content of title to view
        self.window_content = ContentBlock(int(numberBlock)-1, key_in_base, items)
        self.window_content.show()

    # updating of content for main window
    def updating(self):
        self.blocks_of_data.clear()
        self.all_blocks = []
        with open('data.json', 'r') as file:
            base = json.load(file)
        queue_block = 1
        for i in base['datas'].keys():
            self.all_blocks.append(f" {queue_block}. {i}")
            queue_block += 1
        queue_block = 1
        for k in self.all_blocks:
            self.blocks_of_data.addItem(k)

    # deletes a block of data from the manager
    def del_block_of_data(self):

        # selected block of data
        try:
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
        except:
            pass
        self.updating() # update manager window

    def exit_from_app(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication()

    window = Window()
    window.show()

    with open("style.qss", 'r') as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())