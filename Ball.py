from tkinter import Canvas

class Ball():
    def __init__(self):
        self.width = 395
        self.height = 195
        self.x = 405
        self.y = 205
        self.direction_x_right = False
        self.direction_x_left = False
        self.direction_y_top = False
        self.direction_y_bottom = False
        self.speed = 1

    def move(self, canvas=Canvas):
        self.set_direction_x(canvas)
        self.set_direction_y(canvas)
        self.move_x_axis()
        self.move_y_axis()

    def move_x_axis(self, canvas=Canvas):
        if(self.direction_x_left):
            self.width = self.width - self.speed
            self.x = self.x - self.speed
        else:
            self.width = self.width + self.speed
            self.x = self.x + self.speed

    def set_direction_x(self, canvas=Canvas):
        window_width = canvas.winfo_width()
        max_width = window_width - 5
        min_width = 5

        if(self.width <= min_width):
            self.direction_x_right = True
            self.direction_x_left = False
        elif(self.width >= max_width):
            self.direction_x_right = False
            self.direction_x_left = True

    def move_y_axis(self):
        if(self.direction_y_left):
            self.height = self.height - self.speed
            self.y = self.y - self.speed
        else:
            self.height = self.height + self.speed
            self.y = self.y + self.speed

    def set_direction_y(self, canvas=Canvas):        
        window_height = canvas.winfo_height()
        max_height = window_height - 5
        min_height = 5

        if(self.height <= min_height):
            self.direction_y_right = True
            self.direction_y_left = False
        elif(self.height >= max_height):
            self.direction_y_right = False
            self.direction_y_left = True