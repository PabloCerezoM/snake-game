from turtle import Turtle

FONT = ("ArcherPro", 24, "bold")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(x=0, y=260)
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.current_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", False, align=ALIGN, font=FONT)

    def add_a_point(self):
        self.current_score += 1
        self.update_scoreboard()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.current_score = 0
        self.update_scoreboard()
