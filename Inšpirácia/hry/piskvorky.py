hra =  [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
tah = 0
hraci = ["X", "O"]
print("----------- PIŠKVORKY ----------- ")

while True:    
    # Nakresli aktuálnu hraciu plochu
    for x in range(3):
        print("\n---------------")
        for y in range(3):
            print("| {} |".format(hra[x][y]), end="")
    print("\n---------------\n")

    # Získaj miesto od uživateľa = miesto a over jeho obsadenie 
    while True:
        tahhrac = int(input("Tvoj ťah (1 - 9): "))
        if tahhrac >= 1 and tahhrac <= 9:
            x = (tahhrac - 1) // 3
            y = (tahhrac - 1) % 3 
            if hra[x][y] == " ":
                hra[x][y] = hraci[tah]
                tah = (tah + 1) % len(hraci)
                break
    
    # Vygeneruj ťah počítača - TODO
    # Brute Force/ Minimax  
    
    # Kto vyhral - Riadky, Stĺpce, Diagonály
    vyhra = " "
    remiza = True

    for i in range(3):
        for p in hraci:
            if hra[i][0] == p and hra[i][1] == p and hra[i][2] == p:
               vyhra = p
    
    for i in range(3):
        for p in hraci:
            if hra[0][i] == p and hra[1][i] == p and hra[2][i] == p:
               vyhra = p
    
    for p in hraci:
        if hra[0][0] == p and hra[1][1] == p and hra[2][2] == p:
            vyhra = p
    for p in hraci:
        if hra[0][2] == p and hra[1][1] == p and hra[2][0] == p:
            vyhra = p

    # Je Remíza
    for i in range(3):
        for j in range(3):
            if hra[i][j] == " ":
                remiza = False

    if remiza == True:
        print("Hra sa skončila remízou")
        break
    if vyhra == "O":
        print("Hru vyhrali: Krúžky [O]")
        break
    elif vyhra == "X":
        print("Hru vyhrali: Krížiky [X]")
        break
