from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.goto(0, 0)
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1
        self.trail = []

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.leave_trail()

    def leave_trail(self):
        trail_dot = Turtle()
        trail_dot.shape("circle")
        trail_dot.color("yellow")
        trail_dot.shapesize(0.3)
        trail_dot.penup()
        trail_dot.goto(self.xcor(), self.ycor())
        self.trail.append(trail_dot)
        if len(self.trail) > 5:
            old_dot = self.trail.pop(0)
            old_dot.clear()
            old_dot.hideturtle()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
        for dot in self.trail:
            dot.clear()
            dot.hideturtle()
        self.trail.clear()