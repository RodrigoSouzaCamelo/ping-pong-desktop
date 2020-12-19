from tkinter import Canvas
from Window import Window
from Player import Player
from GameConfig import GameConfig
from Ball import Ball

class GameBoard():
    def __init__(self):
        self.window = Window()
        self.canvas = Canvas(self.window.root)
        self.playerOne = Player()
        self.playerTwo = Player()
        self.ball = Ball()
        self.game_config = GameConfig()

    def to_position_players(self):
        self.playerOne.width = 795
        self.playerOne.height = 160
        self.playerOne.x = 785
        self.playerOne.y = 240
        self.playerOne.speed = self.game_config.speed_default

        self.playerTwo.width = 5
        self.playerTwo.height = 160
        self.playerTwo.x = 15
        self.playerTwo.y = 240
        self.playerTwo.speed = self.game_config.speed_default

    def center_game_pieces(self):
        self.to_position_players()
        self.to_position_ball()

    def to_position_ball(self):
        self.ball.position()

    def draw(self):
        self.canvas.delete('all')
        self.draw_player(self.playerOne)
        self.draw_player(self.playerTwo)
        self.draw_ball()
        self.draw_scores()

    def draw_player(self, player=Player):
        self.canvas.create_rectangle(player.width, player.height, player.x, player.y, fill='white')

    def draw_ball(self):
        self.canvas.create_rectangle(self.ball.width, self.ball.height, self.ball.x, self.ball.y, fill='white')

    def draw_scores(self):
        self.canvas.create_text(600, 50, fill='white', font="Arial 24 normal bold", text=self.playerOne.score)
        self.canvas.create_text(200, 50, fill='white', font="Arial 24 normal bold", text=self.playerTwo.score)