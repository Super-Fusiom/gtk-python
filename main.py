import gi
# Force program to use gtk 3.0 insted of 4
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Window(Gtk.Window):
    def __init__(self):
        super().__init__(title="Bing + bong")

        self.button = Gtk.Button(label="Yo wat up")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Wat up")

win = Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

