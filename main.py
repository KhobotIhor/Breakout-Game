import turtle as tr
import random
import time

turtles = []
tr.listen()



def set_squares():

    x = -330
    y = 325

    colors = ['red', 'blue', 'green', 'purple', 'yellow', 'indigo']
    for i in range(45):
        t = tr.Turtle()
        turtles.append(t)

    for t in turtles:
        t.color(random.choice(colors))
        t.penup()
        t.shape('square')
        t.shapesize(2, 1)
        t.setheading(90)
        if x > 330:
            x = -330
            y -= 30
        t.teleport(x, y)
        x += 46

def paddle_collision(ball, paddle):

    if ball.distance(paddle) < 30 and ball.ycor() < -290:
        return True
    else:
        return False

def box_collision(ball):

    for box in turtles:
        if ball.distance(box) < 30:
            turtles.remove(box)
            box.teleport(10000000, 10000000)
            tr.update()
            return True

def replay(arg):
    tr.clearscreen()
    turtles.clear()
    writing = tr.Turtle()
    writing.teleport(-150, 0)
    if arg == 'win':
        message = 'Congratulations! You won! Press ENTER to start over.'
    elif arg == 'lose':
        message = 'You lost(  Press Enter to start over.'

    writing.write(message, font=('Calibri', 20, 'bold'))
    writing.hideturtle()
    tr.update()

def check_win(ball):
    if len(turtles) == 0:
        replay('win')
        return True
    elif ball.ycor() < -320:
        replay('lose')
        return True

def ball_move(ball, paddle):
    heading = ball.heading()
    if ball.xcor() < -330 or ball.xcor() > 330:
        new_heading = heading + (90 - heading) * 2
        ball.setheading(new_heading)
    elif paddle_collision(ball, paddle) or ball.ycor() >= 325 or box_collision(ball):
        new_heading = heading * -1
        ball.setheading(new_heading)


def set_paddle(paddle):

    paddle.color('grey')
    paddle.shapesize(0.5, 3)
    paddle.teleport(0, -310)
    paddle.penup()



def game():
    tr.clearscreen()
    tr.tracer(12, 50)
    def move_left():
        if paddle.xcor() > -330:
            paddle.backward(40)
            tr.update()

    def move_right():
        if paddle.xcor() < 330:
            paddle.forward(40)
            tr.update()
    set_squares()
    paddle = tr.Turtle(shape='square')
    set_paddle(paddle)

    ball = tr.Turtle(shape='circle')
    ball.setheading(210)
    ball.penup()

    ball.turtlesize(0.8, 0.8)
    tr.update()

    tr.onkeypress(move_left, 'Left')
    tr.onkeypress(move_right, 'Right')

    while True:
        if check_win(ball):
            break
        time.sleep(0.02)
        ball.forward(20)
        ball_move(ball, paddle)
        tr.update()

    tr.onkey(game, 'Return')

game()


tr.onkey(game, 'Return')
tr.mainloop()

