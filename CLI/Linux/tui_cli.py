from subprocess import run

from argparse import ArgumentParser, Namespace
import pytermgui as ptg

class MyTextInput(ptg.InputField):
    def __init__(self, x, y, on_submit=None):
        super().__init__(x, y, on_submit=on_submit)

class TUI(ptg.Window):
    def __init__(self, title, width, height):
        super().__init__(self, title, width, height)
        self.text_input = MyTextInput(10, 10)
        self._add_widget(self.text_input)

if __name__ == "__main__":
   window = TUI('Hello', 50, 50)
   window.run()

'''

def main() -> None:
    """Main method"""
   
    with ptg.WindowManager() as manager:
        loader = ptg.YamlLoader()
        #namespace = loader.load(CONFIG_YAML)
        def on_tap(window):
            nowuser = ptg.InputField.value
            print(nowuser)
        window = (
            ptg.Window(width=70)
            + "[210 bold]Kitty Remote"
            + "[210 bold]------------"
            + ""
            + ptg.Label(
                "[240 italic]> Press RETURN to run each command", parent_align=0
            )
            + ptg.InputField("Code words: ")
            + ""
            + ""
        ).center()
        window._add_widget(ptg.Button("Sign in", on_tap(window)))

        window.box = "DOUBLE"
        
        manager.add(window)

        manager.run()


if __name__ == "__main__":
    main()
'''
