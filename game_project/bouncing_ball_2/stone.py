import random


class Stone:
    def __init__(self, canvas, clr):
        self.canvas = canvas
        self.id = canvas.create_oval(5, 5, 25, 25, fill=clr, width=2)

    @staticmethod
    def create_stone(canvas, color):
        return Stone(canvas, color)

    @staticmethod
    def set_stones(canvas, colors):
        stones = []
        for i in range(0, 5):
            b = []
            for j in range(0, 19):
                tmp = Stone(canvas, random.choice(colors))
                b.append(tmp)
            stones.append(b)

        for i in range(0, 5):
            for j in range(0, 19):
                canvas.move(stones[i][j].id, 25 * j, 25 * i)

        return stones
