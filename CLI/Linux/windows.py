import pytermgui as ptg
import json, config, time

# base of data
with open('data.json', 'r') as file:
    base = json.load(file)    
# base of data

class windowMenu():
    def __init__(self):
        self.windowBlock = windowBlock()
        self.loader = ptg.YamlLoader()
        self.namespace = self.loader.load(config.CONFIG_MENU)

        self.status_data = ptg.Label("")
        if base['datas'] == {}:
            self.status_data.value = "Tip: There is no data, try adding a new data block"    

        # ---- Buttons ----
        self.add_btn = ptg.Button(" Insert ", onclick=self.addBlock)
        self.show_btn = ptg.Button("  Show  ")
        self.del_btn = ptg.Button(" Delete ")
        self.edit_btn = ptg.Button("  Edit  ")
        # ---- Buttons ----

        self.menu = (self.add_btn,self.show_btn,self.del_btn,self.edit_btn)
        self.window = ptg.Window(
            "","",self.status_data,"","","","","",
            self.menu
        )
        self.window.center(0)
        self.window.set_title("Password Manager")
        self.window.width = 70
        self.window.height = 12
        self.window.min_width = 70

    def addBlock(self, inx):
        log_manager.remove(self.window)
        log_manager.add(self.windowBlock)

class windowBlock(windowMenu):
    def __init__(self):
        self.blockTitle = ptg.InputField(prompt="Name for the block: ")
        self.blockData = ptg.InputField(prompt="Data for this block name: ")
        self.btnOk = ptg.Button("Ok", onclick=self.on_ok)
        self.btnCancel = ptg.Button("Cancel", onclick=self.on_cancel)

        self.window = ptg.Window(
            self.blockTitle,
            self.blockData,
            "","","","","","",
            (self.btnOk, self.btnCancel)
        )
        self.window.center(0)
        self.window.set_title("New block")
        self.window.width = 70
        self.window.height = 12
        self.window.min_width = 70

    def on_ok(self):
        pass

    def on_cancel(self):
        log_manager(self.window)
        log_manager(windowMenu.window)

class windowRegister(windowMenu):
    def __init__(self):
        self.loader = ptg.YamlLoader()
        self.namespace = loader.load(config.CONFIG_REGLOGWINDOW)

        self.input_password = ptg.InputField(prompt="Come up with a password: ")
        self.btnReady = ptg.Button("   Ready   ", onclick=self.on_ready)
        self.reg_window = ptg.Window(
            "",
            input_password,
            "",
            btnReady,
            ""
        )
        self.reg_window.center(0)
        self.reg_window.set_title("Registration")
        self.reg_window.width = 60
        self.reg_window.min_width = 60
        self.reg_window.height = 7

    def on_ready(self):
        if self.input_password.value:
            base['password'] = self.input_password.value.strip()
            with open('data.json', 'w') as file:
                json.dump(base, file)
            reg_manager.stop()
        else:
            label = ptg.Label('[1]The password cannot be empty')
            self.reg_window.__add__(label)
            time.sleep(1.5)
            self.reg_window.remove(label)
            self.reg_window.height = 7 

class windowLogin(windowMenu):
    def __init__(self):
        self.attempt = 10
        self.loader = ptg.YamlLoader()
        self.namespace = loader.load(config.CONFIG_REGLOGWINDOW)

        self.inputPassword = ptg.InputField(prompt="Password: ")
        self.btn_log = ptg.Button("   Login   ", onclick=self.on_sigin)
        self.attempts = ptg.Label(f'[8]{self.attempt} Attempts before deletion')
        self.log_window = ptg.Window(
            "",
            self.inputPassword,
            "",
            self.attempts,
            "",
            self.btn_log,
            ""
        )
        self.log_window.center(0)
        self.log_window.is_noresize = True
        self.log_window.set_title("Sign in")
        self.log_window.width = 60
        self.log_window.min_width = 60
        self.log_window.height = 9

    def on_sigin(self):
        # password correct
        if self.inputPassword.value == base['password']:
            log_manager.remove(login_window) # deleting the login window
            log_manager.add(windowMenu().window) # launching the main window

        # incorrect password
        else:
            self.attempts.value = "[@red black bold] Incorrect code words! "
            time.sleep(1.5)
            self.attempt -= 1
            self.attempts.value = f'[8]{self.attempt} Attempts before deletion'

        