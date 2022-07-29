import turtle

# Screen initiation
wnd = turtle.Screen()
wnd.title('Pong')
wnd.bgcolor('black')
wnd.setup(height=600, width=800)
wnd.tracer(0)

difficulty = 0
winner = ''


def init_menu_screen():
    global difficulty, winner
    turtle.resetscreen()

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write(f'Choose difficulty(1-3): 0\n\n'
              f'Press Space to start or pause', align='center', font=('Courier', 24, 'normal'))

    pen_b = turtle.Turtle()
    pen_b.speed(0)
    pen_b.color('white')
    pen_b.penup()
    pen_b.hideturtle()
    pen_b.goto(0, 260)
    pen_b.write(f'{winner}', align='center', font=('Courier', 24, 'normal'))

    def choose_difficulty_1():
        global difficulty
        difficulty = 2
        pen.clear()
        pen.write(f'Choose difficulty(1-3): 1\n\n'
                  f'Press Space to start or pause', align='center', font=('Courier', 24, 'bold'))

    def choose_difficulty_2():
        global difficulty
        difficulty = 4
        pen.clear()
        pen.write(f'Choose difficulty(1-3): 2\n\n'
                  f'Press Space to start or pause', align='center', font=('Courier', 24, 'bold'))

    def choose_difficulty_3():
        global difficulty
        difficulty = 6
        pen.clear()
        pen.write(f'Choose difficulty(1-3): 3\n\n'
                  f'Press Space to start or pause', align='center', font=('Courier', 24, 'bold'))

    wnd.listen()
    wnd.onkeypress(choose_difficulty_1, '1')
    wnd.onkeypress(choose_difficulty_2, '2')
    wnd.onkeypress(choose_difficulty_3, '3')
    wnd.onkeypress(init_game_screen, 'space')

    while True:
        wnd.update()


def init_game_screen():
    global difficulty, winner
    turtle.resetscreen()

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape('square')
    paddle_a.color('white')
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape('square')
    paddle_b.color('white')
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball

    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape('circle')
    ball.color('white')
    ball.shapesize(stretch_wid=1, stretch_len=1)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = difficulty
    ball.dy = difficulty

    # Score
    score_a = 0
    score_b = 0

    # Pen

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(f'Player A: {score_a} | Player B: {score_b}', align='center', font=('Courier', 24, 'bold'))

    def paddle_a_up():
        y = paddle_a.ycor()
        if y <= 230:
            y += 20
            paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        if y >= -210:
            y -= 20
            paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        if y <= 230:
            y += 20
            paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        if y >= -210:
            y -= 20
            paddle_b.sety(y)

    # Keyboard binding
    wnd.listen()
    wnd.onkeypress(paddle_a_up, 'w')
    wnd.onkeypress(paddle_a_down, 's')
    wnd.onkeypress(paddle_b_up, 'Up')
    wnd.onkeypress(paddle_b_down, 'Down')
    wnd.onkeypress(init_menu_screen, 'space')

    while True:
        wnd.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 10
            pen.clear()
            pen.write(f'Player A: {score_a} | Player B: {score_b}', align='center', font=('Courier', 24, 'bold'))

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 10
            pen.clear()
            pen.write(f'Player A: {score_a} | Player B: {score_b}', align='center', font=('Courier', 24, 'bold'))

        # Bounce from paddle B
        if 350 > ball.xcor() > 330 and paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50:
            ball.setx(330)
            ball.dx *= -1

        # Bounce from paddle A
        if -350 < ball.xcor() < -330 and paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50:
            ball.setx(-330)
            ball.dx *= -1

        if score_a == 100:
            winner = 'Player A won'
            init_menu_screen()

        if score_b == 100:
            winner = 'Player B won'
            init_menu_screen()


while True:
    wnd.update()
    init_menu_screen()
