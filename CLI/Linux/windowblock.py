import pytermgui as ptg
import json, config, time
import windows as ws

# base of data
with open('data.json', 'r') as file:
    base = json.load(file)    
# base of data

class windowBlock():
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
        import entry

        if self.blockTitle.value == '' or self.blockData.value == '':
            self.caution.value = '[1 bold]The block name or/and block data cannot be empty'
            time.sleep(2)
            self.caution.value = ''
        else:
            base['datas'][self.blockTitle.value] = []
            base['datas'][self.blockTitle.value] = self.blockData.value.split()
            with open('data.json', 'w') as file:
                json.dump(base, file)
            self.block_window.close()
            entry.manager.add(ws.windowMenu().menu_window)

    def on_cancel(self, inx):
        import entry

        self.block_window.close()
        entry.manager.add(ws.windowMenu().menu_window)