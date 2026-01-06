import random


class Ball:
    def __init__(self, canvas, clr, pole, stones, score):
        self.stones = stones
        self.canvas = canvas
        self.pole = pole
        self.score = score
        self.bottom_hit = False
        self.hit = 0
        self.id = canvas.create_oval(10, 10, 25, 25, fill=clr, width=1)
        self.canvas.move(self.id, 230, 461)
        start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)

        self.a = start[0]
        self.b = -start[0]
        self.canvas.move(self.id, self.a, self.b)
        self.cvs_height = canvas.winfo_height()
        self.cvs_width = canvas.winfo_width()

    def stone_strike(self, push):
        for stone_line in self.stones:
            for stone in stone_line:
                stone_push = self.canvas.coords(stone.id)

                try:
                    if push[2] >= stone_push[0] and push[0] <= stone_push[2]:
                        if push[3] >= stone_push[1] and push[1] <= stone_push[3]:
                            #canvas.bell()
                            self.hit += 1
                            self.score.configure(text="Score: " + str(self.hit))
                            self.canvas.delete(stone.id)
                            return True
                except:
                    continue
        return False

    def pole_strike(self, push):
        pole_push = self.canvas.coords(self.pole.id)
        if push[2] >= pole_push[0] and push[0] <= pole_push[2]:
            if push[3] >= pole_push[1] and push[1] <= pole_push[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.a, self.b)
        push = self.canvas.coords(self.id)
        # print(pos)
        start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)
        if self.stone_strike(push):
            self.b = start[0]
        if push[1] <= 0:
            self.b = start[0]
        if push[3] >= self.cvs_height:
            self.bottom_hit = True
        if push[0] <= 0:
            self.a = start[0]
        if push[2] >= self.cvs_width:
            self.a = -start[0]
        if self.pole_strike(push):
            self.b = -start[0]