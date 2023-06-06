import turtle as t
import random
color=["red","green","cyan","pink","purple","orange"]
screen=t.Screen()
screen.setup(width=500,height=400)
user_input=screen.textinput(title="Make a Bet",prompt="Which Turtle will win the race?")
y_pos=[-70,-40,-10,20,50,80]
turtles=[]
for i in range(0,6):
    tim=t.Turtle(shape="turtle")
    tim.penup()
    tim.color(color[i])
    tim.goto(x=-230,y=y_pos[i])
    turtles.append(tim)
if(user_input):
    game = True
while game:

       for turtle in turtles:
           if(turtle.xcor()>230):
               game=False
               if (user_input == turtle.pencolor()):
                   print(f"You have won the bet!")
               else:
                   print(f"You lost the bet the {turtle.pencolor()} turtle has won the race")
           turtle.forward(random.randint(0,10))
