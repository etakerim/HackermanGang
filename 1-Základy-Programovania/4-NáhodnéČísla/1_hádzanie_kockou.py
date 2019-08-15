import random

while True:
    input("HOĎ")
    kocka = random.randint(1, 6)

    if kocka == 1:
        print("+-------+\n"
              "|       |\n"
              "|   #   |\n"
              "|       |\n"
              "+-------+")
    elif kocka == 2:
        print("+-------+\n"
              "| #     |\n"
              "|       |\n"
              "|     # |\n"
              "+-------+")
    elif kocka == 3:
        print("+-------+\n"
              "| #     |\n"
              "|   #   |\n"
              "|     # |\n"
              "+-------+")
    elif kocka == 4:
        print("+-------+\n"
              "| #   # |\n"
              "|       |\n"
              "| #   # |\n"
              "+-------+")
    elif kocka == 5:
        print("+-------+\n"
              "| #   # |\n"
              "|   #   |\n"
              "| #   # |\n"
              "+-------+")
    elif kocka == 6:
        print("+-------+\n"
              "| #   # |\n"
              "| #   # |\n"
              "| #   # |\n"
              "+-------+")
