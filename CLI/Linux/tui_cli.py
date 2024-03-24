from pytermgui import widgets, WindowManager
import pytermgui as ptg

label = ptg.Label("Now get")
input_Field = ptg.InputField("Code words")
def on_click():
    global label
    label.value = input_Field.value

button = ptg.Button("Click", on_click())


def on_click():
    label = ptg.Label(input_Field)

with ptg.WindowManager() as manager:
    window = ptg.Window(
        "",
        input_Field,
        "",
        label,
        "",
        button,
        ""
    )
    manager.add(window)
