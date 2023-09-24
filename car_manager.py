from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# # Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen.
# # No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). 

class CarManager(Turtle):
    def __init__(self):
        self.cars=[]
        self.start_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        rand_chance = random.randint(1,7)
        if rand_chance == 3:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.goto(280, random.randint(-230,230))
            car.setheading(180)
            self.cars.append(car)
    
    def move_car(self):
        for self.car in self.cars:
            self.car.forward(self.start_speed)
    
    # def collides(self, player):
    #     for car in self.cars:
    #         if player.distance(car) < 20 :
    #             return True
    
    def level_up(self):
        self.start_speed += MOVE_INCREMENT