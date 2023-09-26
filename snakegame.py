import turtle
import time
import random
from tkinter import messagebox

win=turtle.Screen()
win.title("SnakeGame")
win.bgcolor("black")
win.setup(height=600,width=600)
win.tracer(0)

# For the snakes head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction ="stop"

delay=0.1
#score
score=0
high_score=0


# Now for food
food=turtle.Turtle()
food.shape("circle")
food.speed(0)
food.color("blue")
food.penup()
food.goto(0,100)


segments=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("Score : 0   HighScore :0",align="center",font=("Arial",25,"normal"))


#Function for movement

def go_up():
    if head.direction !="down":
        head.direction="up"

def go_down():
    if head.direction !="up":
        head.direction="down"

def go_left():
    if head.direction !="right":
        head.direction="left"

def go_right():
    if head.direction!="left":
        head.direction="right"


def movement():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)


#Setting the keyboard keys for bind
win.listen()
win.onkeypress(go_up,"Up")
win.onkeypress(go_down,"Down")
win.onkeypress(go_left,"Left")
win.onkeypress(go_right,"Right")

while(True):
    win.update()
    
    #check for a collision based on border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor() <-290:
        time.sleep(1)
        messagebox.showerror("Game Over","Click OK to continue")
        head.goto(0,0)
        head.direction="stop"

        for segment in segments:
            segment.goto(1000,1000)

            
        segments.clear()
        score=0
        pen.clear()
        pen.write("Score : {}   HighScore :{}".format(score,high_score),align="center",font=("Arial",25,"normal"))

        


    #checking for collision with food
    if head.distance(food)< 20: #*****
        #Placing food at random
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #adding the new segment 
        new_seg=turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("red")
        new_seg.penup()
        segments.append(new_seg)

        #shorten the delay
        # delay -=0.01

        #Increasing the score
        score+=10
        if score>high_score:
            high_score=score

        pen.clear()
        pen.write("Score : {}   HighScore :{}".format(score,high_score),align="center",font=("Arial",25,"normal"))

    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
 

    movement()

#body collision

    for segment in segments:
       
        if segment.distance(head)< 20:
            time.sleep(1)
            messagebox.showerror("Game Over","Click OK to Restart the game")

            head.goto(0,0)
            head.directon="stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            
            score=0
            pen.clear()
            pen.write("Score : {}   HighScore :{}".format(score,high_score),align="center",font=("Arial",25,"normal"))

            # messagebox.showerror("Game Over","Click OK to Restart the game")






    time.sleep(delay)


win.mainloop()