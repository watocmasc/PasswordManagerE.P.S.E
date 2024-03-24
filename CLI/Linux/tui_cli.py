from pytermgui import widgets, WindowManager
import pytermgui as ptg, time

code_words = "python" #test code words

def on_click(inx):
    if input_Field.value == code_words:
        label = ptg.Label("Access")
        window._add_widget(label)
    else:
        label = ptg.Label("Incorrect code words!")
        window.__add__(label)
        time.sleep(1)
        window.remove(label)
        window.height = 6

with ptg.WindowManager() as manager:

    label = ""
    step_local = ""
    input_Field = ptg.InputField(prompt="Code words: ")
    button = ptg.Button("Login", onclick=on_click)
    window = ptg.Window(
        input_Field,
        "",
        button,
        ""
    )
    window.center(0)
    window.height = 6
    window.min_width = 50
    window.set_title("Sign in")
    manager.add(window)