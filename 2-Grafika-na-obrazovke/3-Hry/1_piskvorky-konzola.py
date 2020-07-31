board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
onturn = "X"
won = False

while True:
    # Nakresli hernú dosku
    for row in board:
        print("+---" * len(row) + '+')
        print("|", end="")
        for cell in row:
            print(" " + cell + " |", end="")
        print()
    print("+---" * len(row) + '+')

    if won:
        break

    # Ťah aktuálneho hráča
    while True:
        turn = input(f"Ťah {onturn}: ")
        r, s = turn.split(",")
        r, s = int(r), int(s)

        if 0 <= r < 3 and 0 <= s < 3 and board[r][s] == " ":
            board[r][s] = onturn
            break

    # Pozri či hráč nevyhral
    for i in range(len(board)):
        if board[i][0] == onturn and board[i][1] == onturn and board[i][2] == onturn:
            won = True

    for i in range(len(board)):
        if board[0][i] == onturn and board[1][i] == onturn and board[2][i] == onturn:
            won = True

    if board[0][0] == onturn and board[1][1] == onturn and board[2][2] == onturn:
        won = True

    if board[0][2] == onturn and board[1][1] == onturn and board[2][0] == onturn:
        won = True

    # Vymeň hráča na ťahu
    onturn = "O" if onturn == "X" else "X"

if won:
    print(f"Vyhrali: {onturn}")