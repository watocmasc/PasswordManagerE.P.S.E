import sys, json
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import cipher as cr

class ChangePassword(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(QPixmap("img/icon_main_window.png")))
        self.setWindowTitle("Changing the password")
        self.setMinimumHeight(200)
        self.setMinimumWidth(400)

        # Buttons and Fields #######################################
        self.place_old_password = QLineEdit()
        self.place_old_password.setClearButtonEnabled(True)
        self.place_old_password.setMinimumHeight(50)
        self.place_old_password.setPlaceholderText(" "+"Old password")
        self.place_old_password.setObjectName('place_title')

        self.place_new_password = QLineEdit()
        self.place_new_password.setClearButtonEnabled(True)
        self.place_new_password.setMinimumHeight(50)
        self.place_new_password.setPlaceholderText(" "+"New password")
        self.place_new_password.setObjectName('place_content')
        
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
        self.place_titleLogPass.addWidget(self.place_old_password)
        self.place_titleLogPass.addWidget(self.place_new_password)

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
        self.place_old_password.clear()
        self.place_new_password.clear()
        self.close()

    def done_window(self):
        cr.decrypt('data.json', cr.load_key())
        with open('data.json', 'r') as file:
            base = json.load(file)

        # new block in base
        if self.place_old_password.text().strip() == base['password']:
            if self.place_new_password.text().strip():
                base['password'] = self.place_new_password.text().strip()

                with open('data.json', 'w') as file:
                    json.dump(base, file)
                        
                self.place_old_password.clear()
                self.place_new_password.clear()
                self.close()
        cr.encrypt('data.json', cr.load_key())

class PasswordGeneration(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumHeight(200)
        self.setMinimumWidth(400)
        self.setWindowIcon(QIcon(QPixmap("img/icon_main_window.png")))
        self.setWindowTitle("Password generation")

        self.place_new_password = QLineEdit()
        self.place_new_password.setClearButtonEnabled(True)
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
        import pyperclip as pp
        new_password = ""
        try:
            length_password = int(self.place_new_password.text().strip())
            symbols = '1234567890-=_+!@#$%^&*()`~[]{};:\'\\/|.,<>qazxswedcrfvtgbyhnujmiklopQWERTYUIOPASDFGHJKLZXCVBNM'
            for i in range(length_password):
                new_password += symbols[rt.randint(0,len(symbols)-1)]
            self.place_new_password.setText(f'{new_password}')
            pp.copy(new_password)
        except:
            pass

    def close_window(self):
        self.place_new_password.clear()
        self.close()

class ContentBlock(QWidget):
    def __init__(self, number_of_block, title_block, value_of_block):
        super().__init__()
            
        self.setWindowIcon(QIcon(QPixmap("img/icon_main_window.png")))    
        self.setWindowTitle("Block Data")

        # Propertions of main window
        self.setMinimumHeight(200)
        self.setMinimumWidth(300)

        self.move(490, 290)

        self.number_of_block = number_of_block
        self.value_of_block = value_of_block

        self.title_block = QLineEdit(f' {title_block}')
        self.title_block.setClearButtonEnabled(True)
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
            value.setClearButtonEnabled(True)
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
        cr.decrypt('data.json', cr.load_key())
        with open('data.json', 'r') as file:
            base = json.load(file)

        # Finds the required data block, 
        # deletes the old value and writes a new one to it
        score_key = 0
        for key in list(base['datas'].keys()):
            if score_key == self.number_of_block: 
                del base['datas'][key] # old value
                # new value
                if self.title_and_values_of_block[0].text().strip():
                    base['datas'][self.title_and_values_of_block[0].text().strip()] = [k.text().strip() for k in self.title_and_values_of_block[1:] if k.text().strip() != ""]
                else:
                    base['datas'][key] = [k.text().strip() for k in self.title_and_values_of_block[1:] if k.text().strip() != ""]

            score_key += 1

        with open('data.json', 'w') as file:
            json.dump(base, file)
        cr.encrypt('data.json', cr.load_key())

        self.close()

    def close_window(self):
        self.close()

class CreateBlock(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(QPixmap("img/icon_main_window.png")))
        self.setWindowTitle("Adding new data")
        self.setMinimumHeight(200)
        self.setMinimumWidth(400)

        # Buttons and Fields #######################################
        self.place_title = QLineEdit()
        self.place_title.setClearButtonEnabled(True)
        self.place_title.setMinimumHeight(50)
        self.place_title.setPlaceholderText(" "+"Title")
        self.place_title.setObjectName('place_title')

        self.place_content = QLineEdit()
        self.place_content.setClearButtonEnabled(True)
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
        cr.decrypt('data.json', cr.load_key())
        with open('data.json', 'r') as file:
            base = json.load(file)

        # new block in base
        if self.place_title.text() and self.place_content.text():
            base['datas'][self.place_title.text()] = self.place_content.text().split()

        with open('data.json', 'w') as file:
            json.dump(base, file)
        cr.encrypt('data.json', cr.load_key())
        
        self.place_title.clear()
        self.place_content.clear()
        return self.close()

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(QPixmap("img/icon_main_window.png")))

        # Propertions of main window
        self.setWindowTitle("EPSE")
        self.setMinimumHeight(500)
        self.setMinimumWidth(400)
        self.move(790, 290)

        # Additional windows | Create block of data
        self.window_addBlock = CreateBlock()
        self.window_generatePassword = PasswordGeneration()
        self.window_changePassword = ChangePassword()

        # The contents of the main window #######################################

        # for all blocks of datas
        self.titles_blocks = []

        # A list of all data for further display
        self.blocks_of_data = QListWidget()
        self.blocks_of_data.itemDoubleClicked.connect(self.full_review_of_block)
        self.blocks_of_data.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.blocks_of_data.setObjectName('blocks_of_data')

        # content of main windowf
        cr.decrypt('data.json', cr.load_key())

        with open('data.json', 'r') as file:
            base = json.load(file)
        queue_block = 1
        for title in base['datas'].keys():
            self.titles_blocks.append(f" {queue_block}. {title}")
            queue_block += 1

        for title_item in self.titles_blocks:
            self.blocks_of_data.addItem(title_item)

        cr.encrypt('data.json', cr.load_key())
        # The contents of the main window #######################################

        # Buttons #######################################
        self.btn_changePassword = QPushButton()
        self.btn_changePassword.setMaximumWidth(60)
        self.btn_changePassword.setMinimumWidth(60)
        self.btn_changePassword.setMaximumHeight(60)
        self.btn_changePassword.setMinimumHeight(60)
        self.btn_changePassword.clicked.connect(self.change_password)
        self.btn_changePassword.setObjectName('btn_changepassword')

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

        self.btn_passGeneration = QPushButton()
        self.btn_passGeneration.setMaximumWidth(60)
        self.btn_passGeneration.setMinimumWidth(60)
        self.btn_passGeneration.setMaximumHeight(60)
        self.btn_passGeneration.setMinimumHeight(60)
        self.btn_passGeneration.clicked.connect(self.password_generate)
        self.btn_passGeneration.setObjectName('btn_passGenerate')

        self.btn_googleDriveDownload = QPushButton()
        self.btn_googleDriveDownload.setMaximumWidth(60)
        self.btn_googleDriveDownload.setMinimumWidth(60)
        self.btn_googleDriveDownload.setMaximumHeight(60)
        self.btn_googleDriveDownload.setMinimumHeight(60)
        self.btn_googleDriveDownload.clicked.connect(self.downloadData_googleDrive)
        self.btn_googleDriveDownload.setObjectName('btn_googleDriveDownload')

        self.btn_googleDriveDischarge = QPushButton()
        self.btn_googleDriveDischarge.setMaximumWidth(60)
        self.btn_googleDriveDischarge.setMinimumWidth(60)
        self.btn_googleDriveDischarge.setMaximumHeight(60)
        self.btn_googleDriveDischarge.setMinimumHeight(60)
        self.btn_googleDriveDischarge.clicked.connect(self.dischargeData_googleDrive)
        self.btn_googleDriveDischarge.setObjectName('btn_googleDriveDischarge')
        # Buttons #######################################

        # Menu layout #######################################
        self.blocks_from_data = QVBoxLayout()
        self.blocks_from_data.addWidget(self.blocks_of_data)

        self.btn_panel_first = QHBoxLayout()
        self.btn_panel_first.addWidget(self.btn_addBlock)
        self.btn_panel_first.addWidget(self.btn_delBlock)
        self.btn_panel_first.addWidget(self.btn_updating)
        self.btn_panel_first.addWidget(self.btn_changePassword)
        self.btn_panel_first.addWidget(self.btn_passGeneration)
        self.btn_panel_first.addWidget(self.btn_googleDriveDownload)
        self.btn_panel_first.addWidget(self.btn_googleDriveDischarge)
        
        self.table_of_blocks = QWidget()
        self.table_of_blocks.setLayout(self.blocks_from_data)

        self.main_btns = QWidget()
        self.main_btns.setLayout(self.btn_panel_first)

        self.main_window = QVBoxLayout()
        self.main_window.addWidget(self.table_of_blocks)
        self.main_window.addWidget(self.main_btns)

        self.setLayout(self.main_window)
        # Menu layout #######################################

    def change_password(self):
        self.window_changePassword.show()

    def dischargeData_googleDrive(self):
        """
        Creating a backup copy, if one has not been created, 
        otherwise updating the backup copy
        """

        # authentication of user
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        fileDataFound = True # If the files are found, they do not need to be created again.

        for file_current in file_list:
            # Updating the backup copy by deleting the 
            #old version and downloading the new version
            print(file_list['title'])
            if 'data.json' == file_current['title']:
                file_old_data = drive.CreateFile({'id':file_current['id']})
                file_old_data.Delete() # delete of old version
                file_new_data = drive.CreateFile({'title': 'data.json'})
                file_new_data.SetContentFile('data.json')
                file_new_data.Upload() # upload of new version
                fileDataFound = False
            if 'crypto.key' == file_current['title']:
                file_old_crypto = drive.CreateFile({'id':file_current['id']})
                file_old_crypto.Delete()
                file_new_crypto = drive.CreateFile({'title': 'crypto.key'})
                file_new_crypto.SetContentFile('crypto.key')
                file_new_crypto.Upload()

        if fileDataFound:
        # If the files are not found, we make a backup copy
            file_new_data = drive.CreateFile({'title': 'data.json'})
            file_new_data.SetContentFile('data.json')
            file_new_data.Upload()
            file_new_crypto = drive.CreateFile({'title': 'crypto.key'})
            file_new_crypto.SetContentFile('crypto.key')
            file_new_crypto.Upload()

    def downloadData_googleDrive(self):
        """
        Downloading the current version of the database
        """
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

        for file_current in file_list:
            # Obtaining a database and a cryptographic key
            if 'data.json' == file_current['title']:
                donwload_file_data = drive.CreateFile({'id':file_current['id']})
                donwload_file_data.GetContentFile("data.json")
            elif 'crypto.key' == file_current['title']:
                donwload_file = drive.CreateFile({'id':file_current['id']})
                donwload_file.GetContentFile("crypto.key")

    def password_generate(self):
        self.window_generatePassword.show()

    def add_block_of_data(self):
        self.window_addBlock.show()

    # Viewing the contents of the title
    def full_review_of_block(self):
        cr.decrypt('data.json', cr.load_key())

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

        cr.encrypt('data.json', cr.load_key())

    # updating of content for main window
    def updating(self):
        cr.decrypt('data.json', cr.load_key())

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

        cr.encrypt('data.json', cr.load_key())

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
            cr.decrypt('data.json', cr.load_key())
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

            cr.encrypt('data.json', cr.load_key())
            #
            ####################################
        except:
            pass
        self.updating() # update manager window

    def exit_from_app(self):
        sys.exit()

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumHeight(300)
        self.setMinimumWidth(400)
        self.setMaximumHeight(300)
        self.setMaximumWidth(400)
        self.setWindowIcon(QIcon(QPixmap("img/icon_main_window.png")))
        self.setWindowTitle("Sign up")

        self.window = Window()

        # password entry format and style
        #
        # completely hidden
        self.hidden_password = QCheckBox("Hide")
        self.hidden_password.setStyleSheet("padding-left: 5px;")
        self.hidden_password.setMaximumWidth(100)
        self.hidden_password.setMaximumHeight(60)

        # hidden by asterisks
        self.stars_password = QCheckBox("123")
        self.stars_password.setMaximumWidth(100)
        self.stars_password.setMaximumHeight(60)
        
        self.hidden_password.setObjectName("style_password")
        self.stars_password.setObjectName("style_password")

        self.hidden_password.stateChanged.connect(self.on_hidden_password)
        self.stars_password.stateChanged.connect(self.on_stars_password)
        ##################################

        self.title_signup = QLabel("Sign up")
        self.title_signup.setMaximumHeight(50)
        self.title_signup.setMinimumHeight(50)
        self.title_signup.setObjectName("title_start_window")

        self.place_password = QLineEdit()
        self.place_password.setClearButtonEnabled(True)
        self.place_password.setPlaceholderText(" "+"Password")
        self.place_password.setMaximumHeight(50)
        self.place_password.setMinimumHeight(50)
        self.place_password.setObjectName('place_new_password')

        self.btn_done = QPushButton()
        self.btn_done.setMaximumWidth(100)
        self.btn_done.setMinimumWidth(100)
        self.btn_done.setMaximumHeight(50)
        self.btn_done.setMinimumHeight(50)
        self.btn_done.clicked.connect(self.done_window)
        self.btn_done.setObjectName('btn_done')

        self.btn_cancel = QPushButton()
        self.btn_cancel.setMaximumWidth(100)
        self.btn_cancel.setMinimumWidth(100)
        self.btn_cancel.setMaximumHeight(50)
        self.btn_cancel.setMinimumHeight(50)
        self.btn_cancel.clicked.connect(self.close_window)
        self.btn_cancel.setObjectName('btn_Exit')

        self.place_btns = QHBoxLayout()
        self.place_flags = QHBoxLayout()
        self.place_field_password = QVBoxLayout()
        self.place = QVBoxLayout()

        self.part1_window = QWidget()
        self.part2_window = QWidget()
        self.part3_window = QWidget()

        self.place_flags.addWidget(self.hidden_password)
        self.place_flags.addWidget(self.stars_password)

        self.place_btns.addWidget(self.btn_done)
        self.place_btns.addWidget(self.btn_cancel)

        self.place_field_password.addWidget(self.title_signup)
        self.place_field_password.addWidget(self.place_password)

        self.part1_window.setLayout(self.place_field_password)
        self.part2_window.setLayout(self.place_flags)
        self.part3_window.setLayout(self.place_btns)

        self.place.addWidget(self.part1_window)
        self.place.addWidget(self.part2_window)
        self.place.addWidget(self.part3_window)

        self.setLayout(self.place)

    def on_hidden_password(self,state):
        if state == 2:
            self.place_password.setStyleSheet("color: transparent;")
            self.hidden_password.setText("Hide")
        else:
            self.place_password.setStyleSheet("color: white;")
            self.hidden_password.setText("Show")

    def on_stars_password(self, state):
        if state == 2:
            self.place_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.stars_password.setText("***")
        else:
            self.place_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.stars_password.setText("123")

    def done_window(self):
        cr.decrypt('data.json', cr.load_key())

        with open('data.json', 'r') as file:
            base = json.load(file)

        if(self.place_password.text()):
            base['password'] = self.place_password.text().strip()

            with open('data.json', 'w') as file:
                json.dump(base, file)
                
            self.window.show()

            self.close()
        cr.encrypt('data.json', cr.load_key())

    def close_window(self):
        self.close()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumHeight(300)
        self.setMinimumWidth(400)
        self.setMaximumHeight(300)
        self.setMaximumWidth(400)
        self.setWindowIcon(QIcon(QPixmap("img/icon_main_window.png")))
        self.setWindowTitle("Sign in")

        self.window = Window()

        self.hidden_password = QCheckBox("Hide")
        self.hidden_password.setStyleSheet("padding-left: 5px;")
        self.hidden_password.setMaximumWidth(100)
        self.hidden_password.setMaximumHeight(60)

        self.stars_password = QCheckBox("123")
        self.stars_password.setMaximumWidth(100)
        self.stars_password.setMaximumHeight(60)
        
        self.hidden_password.setObjectName("style_password")
        self.stars_password.setObjectName("style_password")

        self.hidden_password.stateChanged.connect(self.on_hidden_password)
        self.stars_password.stateChanged.connect(self.on_stars_password)

        self.title_signin = QLabel("Sign in")
        self.title_signin.setMaximumHeight(50)
        self.title_signin.setMinimumHeight(50)
        self.title_signin.setObjectName("title_start_window")

        self.place_password = QLineEdit()
        self.place_password.setClearButtonEnabled(True)
        self.place_password.setPlaceholderText(" "+"Password")
        self.place_password.setMaximumHeight(50)
        self.place_password.setMinimumHeight(50)
        self.place_password.setObjectName('place_new_password')

        self.btn_done = QPushButton()
        self.btn_done.setMaximumWidth(100)
        self.btn_done.setMinimumWidth(100)
        self.btn_done.setMaximumHeight(50)
        self.btn_done.setMinimumHeight(50)
        self.btn_done.clicked.connect(self.done_window)
        self.btn_done.setObjectName('btn_done')

        self.place_btns = QHBoxLayout()
        self.place_flags = QHBoxLayout()
        self.place_field_password = QVBoxLayout()
        self.place = QVBoxLayout()

        self.part1_window = QWidget()
        self.part2_window = QWidget()
        self.part3_window = QWidget()

        self.place_flags.addWidget(self.hidden_password)
        self.place_flags.addWidget(self.stars_password)

        self.place_btns.addWidget(self.btn_done)

        self.place_field_password.addWidget(self.title_signin)
        self.place_field_password.addWidget(self.place_password)

        self.part1_window.setLayout(self.place_field_password)
        self.part2_window.setLayout(self.place_flags)
        self.part3_window.setLayout(self.place_btns)

        self.place.addWidget(self.part1_window)
        self.place.addWidget(self.part2_window)
        self.place.addWidget(self.part3_window)

        self.setLayout(self.place)

    def on_hidden_password(self,state):
        if state == 2:
            self.place_password.setStyleSheet("color: transparent;")
            self.hidden_password.setText("Hide")
        else:
            self.place_password.setStyleSheet("color: white;")
            self.hidden_password.setText("Show")

    def on_stars_password(self, state):
        if state == 2:
            self.place_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.stars_password.setText("***")
        else:
            self.place_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.stars_password.setText("123")

    def done_window(self):
        cr.decrypt('data.json', cr.load_key())

        with open('data.json', 'r') as file:
            base = json.load(file)

        if(self.place_password.text().strip() == base['password']):
            self.window.show()
            self.close()

        cr.encrypt('data.json', cr.load_key())

    def close_window(self):
        self.close()

if __name__ == '__main__':
    try:
        cr.decrypt('data.json', cr.load_key())
        with open('data.json', 'r') as file:
            base = json.load(file)
    except Exception:
        try:
            with open('data.json', 'r') as file:
                base = json.load(file)
        except FileNotFoundError:
            data = {"datas": {}, "password": ""}
            with open('data.json', 'w') as file:
                json.dump(data, file)
            with open('data.json', 'r') as file:
                base = json.load(file)

    app = QApplication()

    if(base['password']):
        cr.encrypt('data.json', cr.load_key())
        loginWindow = LoginWindow()
        loginWindow.show()
    else:
        cr.write_key()
        cr.encrypt('data.json', cr.load_key())
        registerWindow = RegisterWindow()
        registerWindow.show()

    with open("style.qss", 'r') as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())