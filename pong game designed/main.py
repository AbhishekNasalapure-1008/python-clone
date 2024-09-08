import turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

class PongGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.setup_screen()
        self.scoreboard = Scoreboard()
        self.paddle1 = Paddle((350, 0))
        self.paddle2 = Paddle((-350, 0))
        self.ball = Ball()
        self.setup_controls()
        self.game_state = "start"
        self.start_text = None
        self.setup_start_screen()

    def setup_screen(self):
        self.screen.bgcolor('black')
        self.screen.setup(width=800, height=600)
        self.screen.title('Enhanced Pong')
        self.screen.tracer(0)
        self.screen.bgpic("starry_background.png")  # Make sure this file exists

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.paddle1.go_up, "Up")
        self.screen.onkey(self.paddle1.go_down, "Down")
        self.screen.onkey(self.paddle2.go_up, "w")
        self.screen.onkey(self.paddle2.go_down, "s")
        self.screen.onkey(self.start_game, "space")

    def setup_start_screen(self):
        self.start_text = turtle.Turtle()
        self.start_text.color("white")
        self.start_text.penup()
        self.start_text.hideturtle()
        self.start_text.goto(0, 50)
        self.start_text.write("PONG", align="center", font=("Arial", 60, "bold"))
        self.start_text.goto(0, -50)
        self.start_text.write("Press SPACE to start", align="center", font=("Arial", 24, "normal"))

    def start_game(self):
        if self.game_state == "start":
            self.game_state = "playing"
            self.remove_start_screen()
            self.game_loop()

    def remove_start_screen(self):
        if self.start_text:
            self.start_text.clear()
            self.start_text = None

    def game_loop(self):
        while self.game_state == "playing":
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.ball.move()

            self.check_collision()
            self.check_scoring()

    def check_collision(self):
        if self.ball.ycor() > 290 or self.ball.ycor() < -290:
            self.ball.bounce_y()
        
        if (self.ball.distance(self.paddle1) < 50 and self.ball.xcor() > 320) or \
           (self.ball.distance(self.paddle2) < 50 and self.ball.xcor() < -320):
            self.ball.bounce_x()

    def check_scoring(self):
        if self.ball.xcor() > 380:
            self.ball.reset_position()
            self.scoreboard.l_point()
        
        if self.ball.xcor() < -380:
            self.ball.reset_position()
            self.scoreboard.r_point()

    def run(self):
        self.screen.mainloop()

if __name__ == "__main__":
    game = PongGame()
    game.run()