import pytermgui as ptg
import config, time, json, windows
  
attempt = 10

# base of data
with open('data.json', 'r') as file:
    base = json.load(file)    
# base of data

def on_sigin(inx):
    global attempt
    # password correct
    if inputPassword.value.strip() == base['password']:
        manager.remove(log_window)
        manager.add(windows.windowMenu().menu_window)
                
    # incorrect password
    else:
        attempts.value = "[@red black bold] Incorrect code words! "
        time.sleep(1.5)
        attempt -= 1
        attempts.value = f'[8]{attempt} Attempts before deletion'

with ptg.WindowManager() as manager:

    loader = ptg.YamlLoader()
    namespace = loader.load(config.CONFIG_REGLOGWINDOW)

    inputPassword = ptg.InputField(prompt="Password: ")
    btn_log = ptg.Button("   Login   ", onclick=on_sigin)
    attempts = ptg.Label(f'[8]{attempt} Attempts before deletion')
    log_window = ptg.Window(
        "",
        inputPassword,
        "",
        attempts,
        "",
        btn_log,
        ""
    )
    log_window.center(0)
    log_window.is_noresize = True
    log_window.set_title("[bold]Sign in")
    log_window.width = 60
    log_window.min_width = 60
    log_window.height = 9
    
    if base['password'] == '':
        pass
    manager.add(log_window)

    
