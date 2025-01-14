from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT="center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level=0
        self.color("black")
        self.penup()
        self.goto(-230,260)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Level:{self.level}",align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER" ,align=ALIGNMENT ,font=FONT)

    def increment_score(self):
        self.level +=1
        self.clear()
        self.update_scoreboard()
