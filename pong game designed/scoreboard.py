from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 60, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 60, "bold"))
        self.draw_middle_line()

    def draw_middle_line(self):
        self.goto(0, 300)
        self.setheading(270)
        self.pendown()
        self.pensize(5)
        for _ in range(30):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()