import gi
# Force program to use gtk 3.0 insted of 4
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Window(Gtk.Window):
    def __init__(self):
        super().__init__(title="Bing + bong")
        # Create button
        self.button = Gtk.Button(label="Yo wat up")
        # Make the button do something
        self.button.connect("clicked", self.on_button_clicked)
        # Add the button to the window
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Wat up")
if __name__ == "__main__":
    # Creates window
    win = Window()
    # Connect the X button to quit the app.
    win.connect("destroy", Gtk.main_quit)
    # Shows the window
    win.show_all()
    # Start gtk
    Gtk.main()

