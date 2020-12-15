from tkinter import Tk, Canvas

class Window():
    def __init__(self):
        self.root = Tk()
        self.configure_window()

    def set_title(self, title='Ping Pong'):
        self.root.wm_title(title)

    def set_rezisable(self, isResizable):
        self.root.resizable(isResizable, isResizable)

    def set_size_window(self, size='800x400'):
        self.root.geometry(size)

    def set_background_color(self, background='black'):
        self.root.configure(background=background)

    def configure_window(self):
        self.set_title()
        self.set_rezisable(False)
        self.set_size_window()
        self.set_background_color()

    def build_window(self):
        self.root.mainloop()

    