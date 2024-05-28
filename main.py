from turtle import Screen, Turtle
import random
is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
screen.title("turtle race")
user_bet= screen.textinput(title="make your bet", prompt="which turtle will win the race enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_positions = [(-230, 0), (-230, -30), (-230, -60), (-230, 30), (-230, 60), (-230, 90)]
all_turtles= []
for position in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[position])
    new_turtle.goto(starting_positions[position])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won the {winning_color} turtle is the winner")
            else:
                print(f"you've lost the {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)





# def move_right():
#     tim.setheading(0)
#     tim.forward(10)
#
#
# def move_left():
#     tim.setheading(180)
#     tim.fd(10)
#
# def move_up():
#     tim.setheading(90)
#     tim.forward(10)
#
#
# def move_down():
#     tim.setheading(270)
#     tim.forward(10)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="Up", fun=move_up)
# screen.onkey(key="Down", fun= move_down)
# screen.onkey(key="Left", fun= move_left)
# screen.onkey(key="Right", fun= move_right)
# screen.onkey(key="C", fun=clear)
screen.exitonclick()
