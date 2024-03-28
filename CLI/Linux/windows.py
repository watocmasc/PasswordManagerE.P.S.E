import pytermgui as ptg
import time, json

# TODO place for crypto
## Base of data ######################################################
# 
with open('data.json', 'r') as file:
    base = json.load(file)    
# 
######################################################################

class windowMenu():
    def __init__(self):

        # - initialization of window
        self.menu_window = ptg.Window()

        self.title = "[@#dec14e black bold] Password Manager"

        if base['datas'] == {}:
            # - if the data list is empty
            self.status_data = ptg.Label(" Tip: There is no data, try adding a new data block ")
            self.status_data.set_style("value", "[@lightblue black bold]{item}")

            for i in range(10):
                if i == 5:
                    self.menu_window.__add__(self.status_data)
                self.menu_window.__add__("")
        else:
            ## Display all data from the database ################################
            # 
            self.menu_window.__add__("")
            self.menu_window.__add__(ptg.Label("[@white black bold] Number " + "[@0] " + "[@#34507d white bold] Title " + "[@0] " + "[@#7d3434 white bold] Data ", parent_align=0))
            self.listOfData = ptg.Container() # a place to store data
            self.listOfData.set_style('border', '[#dec14e]{item}')
            self.listOfData.set_style('corner', '[#dec14e]{item}')
            self.listOfData.set_char("corner", ['╭─','─╮', '─╯', '╰─'])
            self.listOfData.height = 10
            self.listOfData.overflow = ptg.Overflow.SCROLL

            count = 1 # - start of count
            for key in base['datas']:
                self.listOfData.__add__(ptg.Label(f'[@white black bold] {count} ' + "[@0] " + f'[@#34507d white bold] {key} ' + "[@0] " + f'[@#7d3434 white bold] {" ".join(base["datas"][key])} ', parent_align=0)) # parent_align -- 1-(Center) 2-(Right) 3-(Left)
                self.listOfData.__add__(ptg.Label(""))
                count += 1
            self.menu_window.__add__(self.listOfData) 
            # 
            ######################################################################

        ## Buttons ###########################################################
        # 
        self.add_btn = ptg.Button(" Insert ", onclick=self.addBlockData)
        self.add_btn.set_style("label",'[@#32ba52 white]{item}')
        self.add_btn.set_style("highlight",'[@#45ff70 white bold]{item}')
        self.add_btn.on_release(self.add_btn)

        self.show_btn = ptg.Button("  Show  ")

        self.del_btn = ptg.Button(" Delete ", onclick=self.delBlockData)
        self.del_btn.set_style("label",'[@#ba3232 white]{item}')
        self.del_btn.set_style("highlight",'[@#ff4545 white bold]{item}')
        self.del_btn.on_release(self.del_btn)

        self.edit_btn = ptg.Button("  Edit  ")
        self.edit_btn.set_style("label", '[@#c26932 white]{item}')
        self.edit_btn.set_style("highlight", '[@#ff8c45 white bold]{item}')
        self.edit_btn.on_release(self.edit_btn)

        self.exit_btn = ptg.Button("        Exit        ", onclick=self.ExitFromProgram)
        self.exit_btn.set_style("label", '[@#c23232 white]{item}')
        self.exit_btn.set_style("highlight", '[@#ff4545 white bold]{item}')
        self.exit_btn.on_release(self.exit_btn)
        # 
        ######################################################################

        ## Window properties #################################################
        # 
        # menu _______________________________________________________________

        self.menu = (self.add_btn, self.show_btn, self.del_btn, self.edit_btn)
        self.menu_window.__add__("")
        self.menu_window.__add__(self.menu)
        self.menu_window.__add__("")
        self.menu_window.__add__(self.exit_btn)

        # properties _________________________________________________________

        self.menu_window.center(0)
        self.menu_window.is_noresize = True 
        self.menu_window.is_dirty = True
        self.menu_window.set_title(self.title)
        self.menu_window.width = 70
        self.menu_window.height = 18
        self.menu_window.min_width = 70
        # 
        ######################################################################

    ## Functions #########################################################
    # 
    # - finish the manager's work, exit the program
    def ExitFromProgram(self, inx):
        manager.stop()

    # - add a new data block to the database
    def addBlockData(self, inx):
        manager.remove(self.menu_window)
        manager.add(windowAddBlock().block_window)

    # - deleting a block of data from the database
    def delBlockData(self, inx):
        def btnOk(inx):
            manager.remove(dialogWindow)

        # - if there is no data, a dialog box with help
        if base['datas'] == {}:
            dialogWindow = ptg.Window()
            dialogWindow.center(0)

            btnOk = ptg.Button("    OK    ", onclick=btnOk)
            reference = ptg.Label("There is no data to delete.")

            dialogWindow.__add__(reference)
            dialogWindow.__add__("")
            dialogWindow.__add__(btnOk)
            manager.add(dialogWindow)

        # - if the data is available
        else:
            manager.remove(self.menu_window)
            manager.add(windowDelBlock().del_window)
    # 
    ######################################################################

class windowDelBlock(windowMenu):
    def __init__(self):
        # - initialization of window
        self.del_window = ptg.Window()

        ## Display all data from the database ################################
        # 
        self.data_to_delete = ptg.Container() # a place to store data
        # - properties 
        self.data_to_delete.height = 10
        self.data_to_delete.overflow = ptg.Overflow.SCROLL
        count = 1 # - start of count
        for key in base['datas']:
            self.data_to_delete.__add__(ptg.Label(f'{count}| {key}: {" ".join(base["datas"][key])}', parent_align=0)) # parent_align -- 1-(Center) 2-(Right) 3-(Left)
            self.data_to_delete.__add__(ptg.Label(""))
            count += 1
        # 
        ######################################################################
        ## Attributes ########################################################
        # 
        self.NumOfDataToDelete = ptg.InputField(prompt="The number of data to delete: ")
        self.btnDelete = ptg.Button("    Delete    ", onclick=self.on_delete)
        self.btnLeave = ptg.Button("    Cancel    ", onclick=self.on_leave)
        self.NameHint = ptg.Label("Write down the data number to delete.",parent_align=1)
        #
        ######################################################################
        ## Window properties #################################################
        # 
        # menu _______________________________________________________________
        self.del_window.__add__(self.data_to_delete) 
        self.del_window.__add__("")
        self.del_window.__add__(self.NameHint)
        self.del_window.__add__("")
        self.del_window.__add__(self.NumOfDataToDelete)
        self.del_window.__add__("")
        self.del_window.__add__((self.btnDelete, self.btnLeave))
        # properties _________________________________________________________
        self.del_window.center(0)
        self.del_window.is_noresize = True 
        self.del_window.set_title("[bold]Deleting a data block")
        self.del_window.width = 70
        self.del_window.height = 18
        self.del_window.min_width = 70
        # 
        ######################################################################

    ## Functions #########################################################
    # 
    def on_delete(self, inx):
        try:
            if self.NumOfDataToDelete.value:
                count = 1 # - start of count
                blockStatus = False
                for key in base['datas']:
                    if int(self.NumOfDataToDelete.value) == count:
                        del base['datas'][key]
                        blockStatus = True
                        break
                    count += 1
                if blockStatus:
                    self.del_window.__add__(self.data_to_delete) 
                    with open('data.json', 'w') as file:
                        json.dump(base, file)
                    manager.remove(self.del_window)
                    manager.add(windowMenu().menu_window)
                else:
                    self.NameHint.value = "Unavailable values for the block number"
            else:
                self.NameHint.value = "Unavailable values for the block number"
        except:
            self.NameHint.value = "Unavailable values for the block number"

    def on_leave(self, inx):
        manager.remove(self.del_window)
        manager.add(windowMenu().menu_window)
    # 
    ######################################################################

class windowAddBlock(windowMenu):
    def __init__(self):

        ## Attributes ########################################################
        # 
        # - title 
        self.blockTitleContainer = ptg.Container()
        self.blockTitleContainer.height = 3
        self.blockTitleContainer.set_style('border', '[#dec14e]{item}')
        self.blockTitleContainer.set_style('corner', '[#dec14e]{item}')
        self.blockTitleContainer.set_char("corner", ['╭─','─╮', '─╯', '╰─'])
        self.blockTitleContainer.set_char('border', ['│ ', '─', ' │', '─'])
        self.blockTitleContainer.overflow = ptg.Overflow.SCROLL
        self.blockTitle = ptg.InputField(prompt=" Name for the data block: ")
        self.blockTitleContainer._add_widget(self.blockTitle)
        self.blockTitle.set_style("prompt", "[white bold]{item}")
        self.blockTitle.set_style("value", "[white]{item}")

        # - data
        self.blockDataContainer = ptg.Container()
        self.blockDataContainer.height = 3
        self.blockDataContainer.set_style('border', '[#dec14e]{item}')
        self.blockDataContainer.set_style('corner', '[#dec14e]{item}')
        self.blockDataContainer.set_char("corner", ['╭─','─╮', '─╯', '╰─'])
        self.blockDataContainer.set_char('border', ['│ ', '─', ' │', '─'])
        self.blockDataContainer.overflow = ptg.Overflow.SCROLL
        self.blockData = ptg.InputField(prompt=" Data for this block name: ")
        self.blockDataContainer._add_widget(self.blockData)
        self.blockData.set_style("prompt", "[white bold]{item}")
        self.blockData.set_style("value", "[white]{item}")

        self.btnOk = ptg.Button("    Ok    ", onclick=self.on_ok)


        self.btnCancel = ptg.Button("  Cancel  ", onclick=self.on_cancel)


        self.caution = ptg.Label('')
        #
        ######################################################################

        ## Window properties #################################################
        # 
        self.block_window = ptg.Window(
            self.blockTitleContainer,
            self.blockDataContainer,
            self.caution,"",
            (self.btnOk, self.btnCancel)
        )
        self.block_window.center(0)
        self.block_window.overflow = ptg.Overflow.SCROLL
        self.block_window.set_title("[@white black bold] New block")
        self.block_window.width = 70
        self.block_window.height = 12
        self.block_window.is_noresize = True
        self.block_window.min_width = 70
        # 
        ######################################################################

    ## Functions #########################################################
    # 
    def on_ok(self, inx):
        if self.blockTitle.value == '' or self.blockData.value == '':
            self.caution.value = '[@1 white bold] The block name or/and block data cannot be empty '
        else:
            base['datas'][self.blockTitle.value] = []
            base['datas'][self.blockTitle.value] = self.blockData.value.strip().split()
            with open('data.json', 'w') as file:
                json.dump(base, file)
            manager.remove(self.block_window)
            manager.add(windowMenu().menu_window)

    def on_cancel(self, inx):
        manager.remove(self.block_window)
        manager.add(windowMenu().menu_window)
    # 
    ######################################################################

class windowRegister(windowMenu):
    def __init__(self):
        ## Attributes ########################################################
        # 
        self.title = "[@white black bold] Registration"

        self.inputPassword = ptg.InputField(prompt="Come up with a password: ")
        self.inputPassword.set_style("prompt", "[white bold]{item}")
        self.inputPassword.set_style("value", "[white]{item}")

        self.btnReady = ptg.Button("   Ready   ", onclick=self.on_ready)
        self.btnReady.set_style('label', '[@white black]{item}')
        self.btnReady.set_style('highlight', '[@#90ee90 white bold]{item}')
        self.btnReady.on_release(self.btnReady)
        # 
        ######################################################################
        
        ## Window properties #################################################
        # 
        self.reg_window = ptg.Window(
            "",
            self.inputPassword,
            "",
            self.btnReady,
            ""
        )
        self.reg_window.center(0)
        self.reg_window.set_title(self.title)
        self.reg_window.width = 60
        self.reg_window.min_width = 60
        self.reg_window.height = 7
        # 
        ######################################################################

    ## Functions #########################################################
    # 
    # - registration - create a password to log in
    def on_ready(self, inx):
        if self.inputPassword.value:
            base['password'] = self.inputPassword.value.strip()
            with open('data.json', 'w') as file:
                json.dump(base, file)
            manager.remove(self.reg_window)
            manager.add(windowMenu().menu_window)
        else:
            label = ptg.Label('[1]The password cannot be empty')
            self.reg_window.__add__(label)
            time.sleep(1.5)
            self.reg_window.remove(label)
            self.reg_window.height = 7 
    # 
    ######################################################################

class windowLogin(windowMenu):
    def __init__(self):
        self.log_window = ptg.Window()
        ## Attributes ########################################################
        # 
        self.attempt_to_log_in = 10
        self.title = "[@white black bold] Sign in"

        self.inputPassword = ptg.InputField(prompt="Password: ")
        self.inputPassword.set_style("prompt", "[white bold]{item}")
        self.inputPassword.set_style("value", "[white]{item}")

        self.btn_log = ptg.Button("   Login   ", onclick=self.on_sigin)
        self.btn_log.set_style('label', '[@white black]{item}')
        self.btn_log.set_style('highlight', '[@#90ee90 white bold]{item}')
        self.btn_log.on_release(self.btn_log)

        self.attempts = ptg.Label(f'[8]{self.attempt_to_log_in} Attempts before deletion')
        # 
        ######################################################################

        ## Window properties #################################################
        # 
        
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
        self.log_window.set_title(self.title)
        self.log_window.width = 60
        self.log_window.min_width = 60
        self.log_window.height = 9
        #
        ######################################################################

    ## Functions #########################################################
    # 
    def on_sigin(self, inx):
        # password correct
        if self.inputPassword.value.strip() == base['password']:
            manager.remove(self.log_window)
            manager.add(windowMenu().menu_window)    
        # incorrect password
        else:
            self.attempts.value = "[@1 white bold] Incorrect code words! "
            time.sleep(1.5)
            self.attempt_to_log_in -= 1
            self.attempts.value = f'[8]{self.attempt_to_log_in} Attempts before deletion'
    # 
    ######################################################################
            
## Start window ######################################################
#
with ptg.WindowManager() as manager:

    winLogin = windowLogin()
    winRegistration = windowRegister()

    if base['password'] == '':
        # - registration, password does not exist
        manager.add(winRegistration.reg_window)
    else:
        # - login, password exists
        manager.add(winLogin.log_window)
# 
######################################################################