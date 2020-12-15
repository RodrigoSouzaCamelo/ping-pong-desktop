class Ball():
    def __init__(self):
        self.width = int
        self.height = int
        self.x = int
        self.y = int
        self.speed = int

    def move(self):
        if(self.height == self.speed):
            self.height = self.height + self.speed
            self.y = self.y + self.speed
        else:
            self.height = self.height - self.speed
            self.y = self.y - self.speed

        if(self.width )