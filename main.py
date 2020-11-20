from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

turtle_colors = ["red", "blue", "green", "orange", "yellow", "purple"]
starting_line = [-125, -75, -25, 25, 75, 125]
list_of_turtles = []
# init turtles
for num_of_turtles in range(0, 6):
    n_turtles = Turtle(shape="turtle")
    n_turtles.color(turtle_colors[num_of_turtles])
    n_turtles.penup()
    n_turtles.goto(x=-225, y=starting_line[num_of_turtles])
    list_of_turtles.append(n_turtles)

# user input
user_input = screen.textinput(title="Place your bet!", prompt="Select the winning turtle!  Enter a color:  ")


if user_input:
    race = True

while race:

    for turtle in list_of_turtles:
        if turtle.xcor() > 215:
            race = False
            winner = turtle.pencolor()
            if winner == user_input:
    
                print(f"Winner! The {winner} turtle wins!")
            else:
                print(f"Loser! The {winner} turtle wins!")


        run = random.randint(0, 10)
        turtle.forward(run)























screen.exitonclick()