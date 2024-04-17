import sys, gi, json

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

UI_INFO = """

"""

class AppWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.title = "EPSE"
        self.move(960, 540)
        self.set_size_request(700, 200)

        self.entryPassword = Gtk.Entry()
        # self.entryPassword.set_visibility() - for hide passwordbtnRegister
        self.entryPassword.set_text("Password")

        self.check_visible = Gtk.CheckButton(label="Visible")
        self.check_visible.connect("toggled", self.on_visible_toggled)
        self.check_visible.set_active(True)

        self.btnRegister = Gtk.Button(label="Registration")
        self.btnRegister.connect("clicked", self.on_registration)

        self.add(self.entryPassword)
        self.add(self.check_visible)
        self.add(self.btnRegister)

    def on_registration(self, widget):
        with open('data.json', 'r') as file:
            base = json.load(file) 
        base['password'] = self.entryPassword.get_text().strip()
        with open('data.json', 'w') as file:
            json.dump(base, file)

    def on_visible_toggled(self, button):
        value = button.get_active()
        self.entryPassword.set_visibility(value)

if __name__ == "__main__":
    app = AppWindow()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()