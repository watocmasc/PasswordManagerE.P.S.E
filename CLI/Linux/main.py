import pytermgui as ptg, actions
import json, config

# base of data
with open('data.json', 'r') as file:
    base = json.load(file)    
# base of data

def addBlock(inx):
    global show_btn
    global del_btn

    window.remove(status_data)
    window.remove(show_btn)

    blockTitle = ptg.InputField(prompt="Name for the block: ")
    blockData = ptg.InputField(prompt="Data for this block name: ")
    btnOk = ptg.Button("Ok")
    btnCancel = ptg.Button("Cancel")

    window.__add__(blockTitle)
    window.__add__(blockData)
    window.__add__((btnOk, btnCancel))

with ptg.WindowManager() as manager:
    loader = ptg.YamlLoader()
    namespace = loader.load(config.CONFIG_MENU)

    status_data = ptg.Label("")
    if base['datas'] == {}:
        status_data.value = "Tip: There is no data, try adding a new data block"    

    add_btn = ptg.Button(" Insert ", onclick=addBlock)
    show_btn = ptg.Button("  Show  ")
    del_btn = ptg.Button(" Delete ")
    edit_btn = ptg.Button("  Edit  ")
    menu = (show_btn,del_btn,edit_btn)
    window = ptg.Window(
        "","",status_data,add_btn,"","","","","",
        menu
    )
    window.center(0)
    window.set_title("Password Manager")
    window.width = 70
    window.height = 12
    window.min_width = 70
    manager.add(window)

if base['datas'] == {}:
    status_data.value = "There is no data, try adding a new data block"