import turtle as t

screen = t.Screen()

# tim = t.Turtle()
# tim.shape("turtle")
# tim.color("dark violet")

# Code below creates an etch n sketch game thingy.
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def look_right():
#     tim.right(10)
#
#
# def look_left():
#     tim.left(10)
#
#
# def clear():
#     tim.home()
#     tim.penup()
#     tim.clear()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=look_left)
# screen.onkey(key="d", fun=look_right)
# screen.onkey(key="c", fun=clear)

# Code below creates a racing game between turtles.
# import random
#
# screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# all_turtles = []
#
# height = 0
# for turtle in range(0, 6):
#     new_turtle = t.Turtle("turtle")
#     new_turtle.penup()
#     new_turtle.speed(5)
#     new_turtle.color(colors[turtle])
#     new_turtle.goto(x=-200, y=-125 + height)
#     height += 50
#     all_turtles.append(new_turtle)
#
# if user_bet:
#     is_race_on = True
#
# while is_race_on:
#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winner = turtle.pencolor()
#             all_turtles = []
#             if winner == user_bet:
#                 print(f"You've won! The {winner} is the winner")
#             else:
#                 print(f"You've lost. The {winner} is the winner")
#         rand_num = random.randint(0, 10)
#         turtle.forward(rand_num)

screen.exitonclick()
