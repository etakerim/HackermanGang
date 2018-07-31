import tkinter


fps = 30

def game_draw():
    canvas.delete('all')
    # Nakresli loptu
    global ball_x, ball_y, ball_dir
    # Sieť
    i = 0
    for y in range(0, height, height // 21):
        if i % 2:
            color = 'black'
        else:
            color = 'white'
        i += 1
        canvas.create_rectangle(width // 2 - 5, y,
                                width // 2 + 5, y + height // 2,
                                fill=color, outline=color)
    # Skóre
    canvas.create_text(width // 4, 20, text=str(score[0]), fill='white')
    canvas.create_text(width // 4 * 3, 20, text=str(score[1]), fill='white')

    # Paddle
    canvas.create_rectangle(paddle1_x, paddle1_y,
                            paddle1_x + paddle_w, paddle1_y + paddle_h,
                            fill='white', outline='white')
    canvas.create_rectangle(paddle2_x, paddle2_y,
                            paddle2_x + paddle_w, paddle2_y + paddle_h,
                            fill='white', outline='white')

    # Lopta
    canvas.create_rectangle(ball_x, ball_y,
                            ball_x + ball_a, ball_y + ball_a,
                            fill='white', outline='white')

    # Pozri kolíziu s raketami a reaguj
    if (ball_x <= paddle1_x + paddle_w
        and ball_y >= paddle1_y
        and ball_y <= paddle1_y + paddle_h):
        ball_dir[0] = 1

    elif (ball_x + ball_a >= paddle2_x
        and ball_y >= paddle2_y
        and ball_y <= paddle2_y + paddle_h):
        ball_dir[0] = -1

    # Pohni loptu
    ball_x += ball_speed * ball_dir[0]
    ball_y += ball_speed * ball_dir[1]

    # Odraz loptu
    if ball_y <= 0 or ball_y + ball_a >= height:
        ball_dir[1] *= -1

    # Započítaj skóre a resetuj
    if ball_x <= 0:
        score[1] += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_dir = [1, 1]

    elif ball_x + ball_a >= width:
        score[0] += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_dir = [-1, 1]

    canvas.update()
    canvas.after(1000 // fps, game_draw)

def move_up_1(e):
    global paddle1_y
    paddle1_y -= paddle_speed
    if paddle1_y <= 0:
        paddle1_y = 0

def move_down_1(e):
    global paddle1_y
    paddle1_y += paddle_speed
    if paddle1_y + paddle_h >= height:
        paddle1_y = height - paddle_h


def move_up_2(e):
    global paddle2_y
    paddle2_y -= paddle_speed
    if paddle2_y <= 0:
        paddle2_y = 0


def move_down_2(e):
    global paddle2_y
    paddle2_y += paddle_speed
    if paddle2_y + paddle_h >= height:
        paddle2_y = height - paddle_h


width, height = 700, 500
canvas = tkinter.Canvas(width=width, height=height, bg='black')
canvas.pack()

score = [0, 0]
ball_a = 12
ball_speed = 10
ball_x = width // 2
ball_y = height // 2
ball_dir = [1, 1]


paddle_w = 10
paddle_h = 100
paddle1_x = 20
paddle1_y = height // 2
paddle2_x = width - paddle_w - paddle1_x
paddle2_y = height // 2
paddle_speed = 60

canvas.bind_all('s', move_up_1)
canvas.bind_all('x', move_down_1)
canvas.bind_all('k', move_up_2)
canvas.bind_all('m', move_down_2)

game_draw()

canvas.mainloop()
