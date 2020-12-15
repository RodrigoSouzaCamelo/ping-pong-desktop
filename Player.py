class Player():
    def __init__(self):
        self.width = int
        self.height = int
        self.x = int
        self.y = int
        self.speed = int

    def move_up(self):
        if(self.height > 10):
            self.y = self.y - self.speed
            self.height = self.height - self.speed

    def move_down(self):
        if(self.y < 390):
            self.y = self.y + self.speed
            self.height = self.height + self.speed