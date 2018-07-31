
"""
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                num = int("{}2{}0{}1{}6".format(i, j, k, l))
                if num % 2016 == 0:
                    print(num)
"""
neparne = [1, 3, 5, 7, 9]
for i in neparne:
    for j in neparne:
        for k in neparne:
            for l in neparne:
                num = int("{}2{}0{}1{}6".format(i, j, k, l))
                if num % 2016 == 0:
                    print(num)
