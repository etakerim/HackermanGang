import tkinter


fps = 30

def game_draw():
    # Nakresli loptu
    global ball, ball_dir, sc0, sc1, paddle1, paddle2

    # Pozri kolíziu s raketami a reaguj
    b = canvas.coords(ball)
    p1 = canvas.coords(paddle1)
    p2 = canvas.coords(paddle2)

    if (b[0] <= p1[2]
        and b[1] >= p1[1]
        and b[1] <= p1[3]):
        ball_dir[0] = 1

    elif (b[2] >= p2[0]
        and b[1] >= p2[1]
        and b[1] <= p2[3]):
        ball_dir[0] = -1


    # Odraz loptu
    if b[1] <= 0 or b[3] >= height:
        ball_dir[1] *= -1

    # Započítaj skóre a resetuj
    if b[0] <= 0:
        score[1] += 1
        canvas.coords(ball, width // 2, height // 2, width // 2 + 12, height // 2 + 12)
        canvas.itemconfig(sc1, text=str(score[1]))
        ball_dir = [1, 1]

    elif b[2] >= width:
        score[0] += 1
        canvas.coords(ball, width // 2, height // 2, width // 2 + 12, height // 2 + 12)
        canvas.itemconfig(sc0, text=str(score[0]))
        ball_dir = [-1, 1]

    canvas.move(ball, ball_dir[0] * ball_speed, ball_dir[1] * ball_speed)
    canvas.update()
    canvas.after(1000 // fps, game_draw)

def move_up_1(e):
    global paddle1
    if canvas.coords(paddle1)[1] > 0:
        canvas.move(paddle1, 0, -paddle_speed)

def move_down_1(e):
    global paddle1
    if canvas.coords(paddle1)[3] < height:
        canvas.move(paddle1, 0, paddle_speed)

def move_up_2(e):
    global paddle2
    if canvas.coords(paddle2)[1] > 0:
        canvas.move(paddle2, 0, -paddle_speed)

def move_down_2(e):
    global paddle2
    if canvas.coords(paddle1)[3] < height:
        canvas.move(paddle2, 0, paddle_speed)


width, height = 700, 500
canvas = tkinter.Canvas(width=width, height=height, bg='black')
canvas.pack()

score = [0, 0]
ball_speed = 7
ball_dir = [1, 1]

paddle_w = 10
paddle_h = 100
paddle1_x = 20
paddle1_y = height // 2
paddle2_x = width - paddle_w - paddle1_x
paddle2_y = height // 2
paddle_speed = 20

canvas.bind_all('s', move_up_1)
canvas.bind_all('x', move_down_1)
canvas.bind_all('k', move_up_2)
canvas.bind_all('m', move_down_2)

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
sc0 = canvas.create_text(width // 4, 30, text=str(score[0]),
                         font=('Inconsolata', '30'), fill='white')
sc1 = canvas.create_text(width // 4 * 3, 30, text=str(score[1]), 
                         font=('Inconsolata', '30'), fill='white')

paddle1 = canvas.create_rectangle(paddle1_x, paddle1_y,
                        paddle1_x + paddle_w, paddle1_y + paddle_h,
                        fill='white', outline='white')
paddle2 = canvas.create_rectangle(paddle2_x, paddle2_y,
                        paddle2_x + paddle_w, paddle2_y + paddle_h,
                        fill='white', outline='white')

ball = canvas.create_rectangle(width // 2, height // 2,
                               width // 2 + 12, height // 2 + 12,
                               fill='white', outline='white')
game_draw()
canvas.mainloop()
