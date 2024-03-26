import pytermgui as ptg
import json, config, time
import windows as ws

# base of data
with open('data.json', 'r') as file:
    base = json.load(file)    
# base of data

class windowLogin():
    def __init__(self):
        self.attempt = 10
        self.loader = ptg.YamlLoader()
        self.namespace = self.loader.load(config.CONFIG_REGLOGWINDOW)

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
        self.log_window.set_title("[bold]Sign in")
        self.log_window.width = 60
        self.log_window.min_width = 60
        self.log_window.height = 9

    def on_sigin(self, inx):
        from entry import manager
        # password correct
        if self.inputPassword.value.strip() == base['password']:
            self.log_window.close()
            manager.add(ws.windowMenu().menu_window)
            
        # incorrect password
        else:
            self.attempts.value = "[@red black bold] Incorrect code words! "
            time.sleep(1.5)
            self.attempt -= 1
            self.attempts.value = f'[8]{self.attempt} Attempts before deletion'