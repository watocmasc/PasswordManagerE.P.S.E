import pytermgui as ptg
import config, time, json

# TODO place for crypto
######################################################################
# base of data
with open('data.json', 'r') as file:
    base = json.load(file)    
# base of data
######################################################################

class windowMenu():
    def __init__(self):

        self.loader = ptg.YamlLoader()
        self.namespace = self.loader.load(config.CONFIG_MENU)

        # - initialization of window
        self.menu_window = ptg.Window()

        if base['datas'] == {}:

            # - if the data list is empty
            self.menu_window.__add__("")
            self.status_data = ptg.Label("Tip: There is no data, try adding a new data block")
            for i in range(10):
                if i == 5:
                    self.menu_window.__add__(self.status_data)
                self.menu_window.__add__("")
        else:
            ######################################################################
            # display all data from the database

            self.listOfData = ptg.Container() # a place to store data
                # - properties 
            self.listOfData.height = 10
            self.listOfData.overflow = ptg.Overflow.SCROLL

            count = 1 # - start of count
            for key in base['datas']:
                
                self.listOfData.__add__(ptg.Label(f'{count}| {key}: {" ".join(base["datas"][key])}', parent_align=0)) # parent_align -- 1-(Center) 2-(Right) 3-(Left)
                self.listOfData.__add__(ptg.Label(""))
                count += 1
            self.menu_window.__add__(self.listOfData) 

            # display all data from the database
            ######################################################################

        ######################################################################
        # Buttons

        self.add_btn = ptg.Button(" Insert ", onclick=self.addBlockData)
        self.show_btn = ptg.Button("  Show  ")
        self.del_btn = ptg.Button(" Delete ")
        self.edit_btn = ptg.Button("  Edit  ")
        self.exit_btn = ptg.Button("    Exit    ", onclick=self.ExitFromProgram)

        # Buttons
        ######################################################################

        ######################################################################
        # Window properties

        # menu _______________________________________________________________

        self.menu = (self.add_btn, self.show_btn, self.del_btn, self.edit_btn)
        self.menu_window.__add__("")
        self.menu_window.__add__(self.menu)
        self.menu_window.__add__("")
        self.menu_window.__add__(self.exit_btn)

        # properties _________________________________________________________

        self.menu_window.center(0)
        self.menu_window.is_noresize = True 
        self.menu_window.set_title("[bold]Password Manager")
        self.menu_window.width = 70
        self.menu_window.height = 18
        self.menu_window.min_width = 70

        # Window properties
        ######################################################################

    ######################################################################
    # Functions

    # - finish the manager's work, exit the program
    def ExitFromProgram(self, inx):
        manager.stop()

    # - add a new data block to the database
    def addBlockData(self, inx):
        manager.remove(self.menu_window)
        manager.add(windowAddBlock().block_window, animate=True)
    
    # Functions
    ######################################################################

class windowAddBlock(windowMenu):
    def __init__(self):

        self.blockTitle = ptg.InputField(prompt="Name for the block: ")
        self.blockData = ptg.InputField(prompt="Data for this block name: ")
        self.btnOk = ptg.Button("Ok", onclick=self.on_ok)
        self.btnCancel = ptg.Button("Cancel", onclick=self.on_cancel)
        self.caution = ptg.Label('')

        self.block_window = ptg.Window(
            "",
            self.blockTitle,
            "",
            self.blockData,
            "","",self.caution,"",
            (self.btnOk, self.btnCancel)
        )
        self.block_window.center(0)
        self.block_window.set_title("[bold]New block")
        self.block_window.width = 70
        self.block_window.height = 12
        self.block_window.min_width = 70

    def on_ok(self, inx):
        if self.blockTitle.value == '' or self.blockData.value == '':
            self.caution.value = '[1 bold]The block name or/and block data cannot be empty'
        else:
            base['datas'][self.blockTitle.value] = []
            base['datas'][self.blockTitle.value] = self.blockData.value.strip().split()
            with open('data.json', 'w') as file:
                json.dump(base, file)
            manager.remove(self.block_window)
            manager.add(windowMenu().menu_window, animate=True)

    def on_cancel(self, inx):
        manager.remove(self.block_window)
        manager.add(windowMenu().menu_window, animate=True)

class windowRegister(windowMenu):
    def __init__(self):

        self.loader = ptg.YamlLoader()
        self.namespace = self.loader.load(config.CONFIG_REGLOGWINDOW)

        self.input_password = ptg.InputField(prompt="Come up with a password: ")
        self.btnReady = ptg.Button("   Ready   ", onclick=self.on_ready)
        self.reg_window = ptg.Window(
            "",
            self.input_password,
            "",
            self.btnReady,
            ""
        )
        self.reg_window.center(0)
        self.reg_window.set_title("Registration")
        self.reg_window.width = 60
        self.reg_window.min_width = 60
        self.reg_window.height = 7

    def on_ready(self, inx):
        if self.input_password.value:
            base['password'] = self.input_password.value.strip()
            with open('data.json', 'w') as file:
                json.dump(base, file)
            manager.remove(self.reg_window)
            manager.add(windowMenu().menu_window, animate=True)

        else:
            label = ptg.Label('[1]The password cannot be empty')
            self.reg_window.__add__(label)
            time.sleep(1.5)
            self.reg_window.remove(label)
            self.reg_window.height = 7 

class windowLogin(windowMenu):
    def __init__(self):

        self.attempt_to_log_in = 10
        self.loader = ptg.YamlLoader()
        self.namespace = self.loader.load(config.CONFIG_REGLOGWINDOW)

        self.inputPassword = ptg.InputField(prompt="Password: ")
        self.btn_log = ptg.Button("   Login   ", onclick=self.on_sigin)
        self.attempts = ptg.Label(f'[8]{self.attempt_to_log_in} Attempts before deletion')
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
        self.log_window.set_title("[bold]Sign in")
        self.log_window.width = 60
        self.log_window.min_width = 60
        self.log_window.height = 9

    def on_sigin(self, inx):
        # password correct
        if self.inputPassword.value.strip() == base['password']:
            manager.remove(self.log_window)
            manager.add(windowMenu().menu_window)
            
        # incorrect password
        else:
            self.attempts.value = "[@red black bold] Incorrect code words! "
            time.sleep(1.5)
            self.attempt_to_log_in -= 1
            self.attempts.value = f'[8]{self.attempt_to_log_in} Attempts before deletion'

with ptg.WindowManager() as manager:

    winLogin = windowLogin()
    winRegistration = windowRegister()

    if base['password'] == '':
        # - registration, password does not exist
        manager.add(winRegistration.reg_window, animate=True)
    else:
        # - login, password exists
        manager.add(winLogin.log_window, animate=True)

    
