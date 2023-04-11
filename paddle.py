from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.cor = cor
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=0)
        self.color("white")
        self.penup()
        self.setposition(self.cor)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.cor[0], y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.cor[0], y=new_y)





