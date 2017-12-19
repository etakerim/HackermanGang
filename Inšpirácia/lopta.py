import tkinter

def game_draw():
    canvas.delete('all')
    # Nakresli loptu
    global ball_x, ball_y
    canvas.create_oval(ball_x - ball_r, ball_y - ball_r,
                       ball_x + ball_r, ball_y + ball_r,
                       fill='white', outline='white')

    # Pohni loptu
    ball_x += ball_speed * ball_dir[0]
    ball_y += ball_speed * ball_dir[1]

    # Odraz loptu
    if ball_x - ball_r <= 0 or ball_x + ball_r >= width:
        ball_dir[0] *= -1
    if ball_y - ball_r <= 0 or ball_y + ball_r >= height:
        ball_dir[1] *= -1

    canvas.update()
    canvas.after(1000 // 60, game_draw)

width, height = 800, 500
canvas = tkinter.Canvas(width=width, height=height, bg='black')
canvas.pack()

ball_x, ball_y = width // 2, height // 2
ball_r = 10
ball_speed = 5
ball_dir = [1, 1]

game_draw()
canvas.mainloop()
