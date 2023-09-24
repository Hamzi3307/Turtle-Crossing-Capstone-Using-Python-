import time
from turtle import Screen
from player import Player# , STARTING_POSITION, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north
player = Player()

screen.listen()
screen.onkey(player.up, "Up")

# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen.
# No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). 
car_manager = CarManager()

# Create a scoreboard that keeps track of which level the user is on. 
# Every time the turtle player does a successful crossing, the level should increase. 
# When the turtle hits a car, GAME OVER should be displayed in the centre
board = Scoreboard()

game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move_car()
    time.sleep(0.1)
    screen.update()
    
    # Detect when the turtle player collides with a car and stop the game if this happens.
    # if car_manager.collides(player):
    #     time.sleep(5)
    #     game_is_on =False
    
    for car in car_manager.cars:
        if car.distance(player) < 20:
            board.goto(0,0)
            board.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
            game_is_on = False
    
    # Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
    # When this happens, return the turtle to the starting position and increase the speed of the cars. 
    # Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed.
    # if player.ycor() >= FINISH_LINE_Y:
    #     player.goto(STARTING_POSITION)
    if player.crossed_road():
        board.level += 1
        board.update_board()
        car_manager.level_up()
    

screen.exitonclick()