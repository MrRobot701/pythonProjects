class Stone:
    def __init__(self, canvas, clr):
        self.canvas = canvas
        self.id = canvas.create_oval(5, 5, 25, 25, fill=clr, width=2)
