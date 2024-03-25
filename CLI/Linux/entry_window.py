import pytermgui as ptg
import config, time, json, main

attempt = 10

# base of data
with open('data.json', 'r') as file:
    base = json.load(file)    
# base of data

# ------------ Actions for buttons ------------

def on_ready(inx):
    if input_password.value:
        base['password'] = input_password.value.strip()
        with open('data.json', 'w') as file:
            json.dump(base, file)
        reg_manager.stop()
    else:
        label = ptg.Label('[1]The password cannot be empty')
        register_window.__add__(label)
        time.sleep(1.5)
        register_window.remove(label)
        register_window.height = 7 

def on_sigin(inx):
    global attempt
    
    # password correct
    if input_Field.value == base['password']:
        log_manager.remove(login_window) # deleting the login window
        log_manager.add(main.window) # launching the main window

    # incorrect password
    else:
        attempts.value = "[@red black bold] Incorrect code words! "
        time.sleep(1.5)
        attempt -= 1
        attempts.value = f'[8]{attempt} Attempts before deletion'

# ------------ Actions for buttons ------------

# if the password does not exist
if base['password'] == '':
    with ptg.WindowManager() as reg_manager:

        loader = ptg.YamlLoader()
        namespace = loader.load(config.CONFIG_REGLOGWINDOW)

        input_password = ptg.InputField(prompt="Come up with a password: ")
        btnReady = ptg.Button("   Ready   ", onclick=on_ready)
        register_window = ptg.Window(
            "",
            input_password,
            "",
            btnReady,
            ""
        )
        register_window.center(0)
        register_window.set_title("Registration")
        register_window.width = 60
        register_window.min_width = 60
        register_window.height = 7
        reg_manager.add(register_window)

# if the password exists
else:
    with ptg.WindowManager() as log_manager:

        loader = ptg.YamlLoader()
        namespace = loader.load(config.CONFIG_REGLOGWINDOW)

        input_Field = ptg.InputField(prompt="Password: ")
        button = ptg.Button("   Login   ", onclick=on_sigin)
        attempts = ptg.Label(f'[8]{attempt} Attempts before deletion')
        login_window = ptg.Window(
            "",
            input_Field,
            "",
            attempts,
            "",
            button,
            ""
        )
        login_window.center(0)
        login_window.is_noresize = True
        login_window.set_title("Sign in")
        login_window.width = 60
        login_window.min_width = 60
        login_window.height = 9
        log_manager.add(login_window)
        