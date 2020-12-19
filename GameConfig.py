from tkinter import Canvas
from Window import Window

class GameConfig():
    def __init__(self):
        self.speed_default = 1
        self.keys_press = {}

    def configure_canvas(self, canvas: Canvas):
        canvas.configure(background='black', width='800', height='400', highlightthickness=0)

    def set_bindings_keys(self, window):
        for key in ["w","s","Up", "Down"]:
            window.root.bind_all(f'<KeyPress {key}>', self.key_pressed_handler)
            window.root.bind_all(f'<KeyRelease {key}>', self.key_released_handler)
            self.keys_press[key] = False

    def key_pressed_handler(self, event):
        self.keys_press[event.keysym] = True

    def key_released_handler(self, event):
        self.keys_press[event.keysym] = False