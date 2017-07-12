""" 
    Skript vypisujúci všetky kombinácie označenia
    cestovného lístka ak je dier 9 a označené vždy 4.
    Autor: Miroslav Hájek

    Vysvetlenie - každá kombinácia (nCk) je súbor stromov -> napr. 5C3
        (spojenia v strome, ktoré nedávajú celú k-ticu sú vynechané) 
        
                                        Vetvy obsahujú prvky:
          1           2            3      (1 .. n)
       /  |  \       / \          / 
      2   3   4     3   4        4        (2 .. n)
     /|\  |\  |    / \   \      /
    3 4 5 4 5 5   4   5   5    5          (3 .. n)

---------------------------------------------------------------

    Všeobecné riešenie pre Python (cez zoznamovú komprihenziu):
    (Viac na: https://docs.python.org/3/library/itertools.html)

    import itertools

    zoznam = ["".join(x) for x in itertools.combinations("123456789", 4)]
    print(zoznam)
"""

limit = 10
n = 0

for i in range(1, limit):
    for j in range(i + 1, limit):
        for k in range(j + 1, limit):
            for l in range(k + 1, limit):
                n += 1
                print("{:3} - {}{}{}{}".format(n, i, j, k, l))
