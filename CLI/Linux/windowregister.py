import pytermgui as ptg
import json, config, time
import windows as ws

# base of data
with open('data.json', 'r') as file:
    base = json.load(file)    
# base of data

class windowRegister():
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
        import entry

        if self.input_password.value:
            base['password'] = self.input_password.value.strip()
            with open('data.json', 'w') as file:
                json.dump(base, file)
            self.reg_window.close()
            entry.manager.add(ws.windowMenu().menu_window)

        else:
            label = ptg.Label('[1]The password cannot be empty')
            self.reg_window.__add__(label)
            time.sleep(1.5)
            self.reg_window.remove(label)
            self.reg_window.height = 7 