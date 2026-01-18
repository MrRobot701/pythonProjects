class Pole:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 485)
        self.x = 0
        self.is_paused = False
        self.cvs_width = canvas.winfo_width()
        self.canvas.bind_all("<Left>", self.turn_left)
        self.canvas.bind_all("<Right>", self.turn_right)
        self.canvas.bind_all("<space>", self.pause)

    def draw(self):
        push = self.canvas.coords(self.id)
        # print(pos)
        if push[0] + self.x <= 0:
            self.x = 0
        if push[2] + self.x >= self.cvs_width:
            self.x = 0
        self.canvas.move(self.id, self.x, 0)

    def turn_left(self, event):
        self.x = -3.5

    def turn_right(self, event):
        self.x = 3.5

    def pause(self, event):
        self.is_paused = not self.is_paused
