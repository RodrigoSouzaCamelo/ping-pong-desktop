from tkinter import Canvas
from Window import Window
from Player import Player
from Ball import Ball

class Game():
    def __init__(self):
        self.window = Window()
        self.canvas = Canvas(self.window.root)
        self.playerOne = Player()
        self.playerTwo = Player()
        self.ball = Ball()
        self.keys_press = {}
        self.configure_game()

    def build_players(self):
        self.playerOne.width = 795
        self.playerOne.height = 160
        self.playerOne.x = 785
        self.playerOne.y = 240
        self.playerOne.speed = 1

        self.playerTwo.width = 5
        self.playerTwo.height = 160
        self.playerTwo.x = 15
        self.playerTwo.y = 240
        self.playerTwo.speed = 1

    def configure_canvas(self):
        self.canvas.configure(background='black', width='800', height='400', highlightthickness=0)

    def configure_game(self):
        self.configure_canvas()
        self.set_bindings_keys()
        self.build_players()

    def set_bindings_keys(self):
        for key in ["w","s","Up", "Down"]:
            self.window.root.bind_all(f'<KeyPress {key}>', self.key_pressed_handler)
            self.window.root.bind_all(f'<KeyRelease {key}>', self.key_released_handler)
            self.keys_press[key] = False

    def key_pressed_handler(self, event):
        self.keys_press[event.keysym] = True

    def key_released_handler(self, event):
        self.keys_press[event.keysym] = False

    def move_players(self):
        if(self.keys_press['Up']):
            self.playerOne.move_up()
        if(self.keys_press['Down']):
            self.playerOne.move_down()
        if(self.keys_press['w']):
            self.playerTwo.move_up()
        if(self.keys_press['s']):
            self.playerTwo.move_down()

    def animate(self):
        self.move_players()
        self.ball.move(self.canvas)
        self.draw()

    def draw(self):
        self.canvas.delete('all')
        self.draw_player(self.playerOne)
        self.draw_player(self.playerTwo)
        self.draw_ball()
        self.window.root.after(5, self.animate)

    def draw_player(self, player=Player):
        self.canvas.create_rectangle(player.width, player.height, player.x, player.y, fill='white')

    def draw_ball(self):
        self.canvas.create_rectangle(self.ball.width, self.ball.height, self.ball.x, self.ball.y, fill='white')

    def start_game(self):
        self.animate()
        self.canvas.pack()
        self.window.build_window()