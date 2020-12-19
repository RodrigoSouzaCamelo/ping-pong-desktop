from tkinter import Canvas
from Player import Player
from GameConfig import GameConfig
from GameBoard import GameBoard

class Game(GameBoard):
    def __init__(self):
        super().__init__()
        self.configure_game()
        self.speed = self.game_config.speed_default

    def configure_game(self):
        self.game_config.configure_canvas(self.canvas)
        self.game_config.set_bindings_keys(self.window)
        self.to_position_players()

    def check_players_movement(self):
        if(self.game_config.keys_press['Up']):
            self.playerOne.move_up()
        if(self.game_config.keys_press['Down']):
            self.playerOne.move_down()
        if(self.game_config.keys_press['w']):
            self.playerTwo.move_up()
        if(self.game_config.keys_press['s']):
            self.playerTwo.move_down()

    def check_scores(self):
        if(self.ball.x >= 797 and self.check_player_lost(self.playerOne)):
            self.playerTwo.score += 1
            self.restart_game()
        elif(self.ball.width <= 3 and self.check_player_lost(self.playerTwo)):
            self.playerOne.score += 1
            self.restart_game()
        elif(self.ball.x >= 797 or self.ball.width <= 3):
            self.set_game_speed(self.speed + 1)

    def set_game_speed(self, speed):
        self.speed = speed
        self.ball.speed = self.speed
        self.playerOne.speed = self.speed
        self.playerTwo.speed = self.speed

    def check_player_lost(self, player: Player):
        return (self.check_is_lower_than_ball(player) or self.check_is_taller_than_ball(player))

    def check_is_lower_than_ball(self, player: Player):
        return player.height > self.ball.height

    def check_is_taller_than_ball(self, player: Player):
        return player.y < self.ball.height

    def animate(self):
        self.check_scores()
        self.check_players_movement()
        self.ball.move(self.canvas)
        self.draw()
        self.window.root.after(10, self.animate)

    def start_game(self):
        self.animate()
        self.canvas.pack()
        self.window.build_window()

    def restart_game(self):
        self.center_game_pieces()
        self.set_game_speed(self.game_config.speed_default)