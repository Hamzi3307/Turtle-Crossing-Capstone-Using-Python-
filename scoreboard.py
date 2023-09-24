from turtle import Turtle
FONT = ("Courier", 24, "normal")

# Create a scoreboard that keeps track of which level the user is on. 
# Every time the turtle player does a successful crossing, the level should increase. 
# When the turtle hits a car, GAME OVER should be displayed in the centre

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_board()
    
    def update_board(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)