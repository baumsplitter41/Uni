a = "a"
b = "b"
c = "c"

A = [a,b,c]
B = []
C = []

aloc = ""
bloc = ""
cloc = ""

def error():
    print("Error: You cant do this move.")


#--------------------a-----------------------------------------------------#
def a_location():
    global a
    global b
    global c
    global A
    global B
    global C
    global aloc
         
    if a in A:
        aloc = "A"
        return aloc
    elif a in B:
        aloc = "B"
        return aloc
    elif a in C:
        aloc = "C"
        return aloc



def a_bewegen():
    global a
    global b
    global c
    global A
    global B
    global C
    global aloc
    global bloc
    global cloc

    if aloc == bloc or aloc == cloc:
        error()
        return
    elif aloc == "A":
        move = input("Wohin möchtest du a bewegen? (B/C) ")
        if move == "A":
            error()
            return
    elif aloc == "B":
        move = input("Where do you want to move? (A/C) ")
        if move == "B":
            error()
            return
    elif aloc == "C":
        move = input("Where do you want to move? (A/B) ")
        if move == "C":
            error()
            return

    if move == "A":
        if cloc == "A" or bloc == "A":
            error()
            return
        else:
            A.append(a)
        if aloc == "B":
            B.remove(a)
        elif aloc == "C":
            C.remove(a)
    elif move == "B":
        if cloc == "B" or bloc == "B":
            error()
            return
        else:
            B.append(a)
        if aloc == "A":
            A.remove(a)
        elif aloc == "C":
            C.remove(a)
    elif move == "C":
        if cloc == "C" or bloc == "C":
            error()
            return
        else:
            C.append(a)
        if aloc == "A":
            A.remove(a)
        elif aloc == "B":
            B.remove(a)
        

#--------------------b-----------------------------------------------------#
def b_location():
    global a
    global b
    global c
    global A
    global B
    global C
    global bloc

    if b in A:
        bloc = "A"
        return bloc
    elif b in B:
        bloc = "B"
        return bloc
    elif b in C:
        bloc = "C"
        return bloc



def b_bewegen():
    global a
    global b
    global c
    global A
    global B
    global C
    global aloc
    global bloc
    global cloc

    if bloc == cloc :
        print("You can't move this.")
        return
    elif bloc == "A":
        move = input("Wohin möchtest du a bewegen? (B/C) ")
        if move == "A":
            error()
            return
    elif bloc == "B":
        move = input("Where do you want to move? (A/C) ")
        if move == "B":
            error()
            return
    elif bloc == "C":
        move = input("Where do you want to move? (A/B) ")
        if move == "C":
            error()
            return

    if move == "A":
        if cloc == "A":
            error()
            return
        else:
            A.append(b)
        if bloc == "B":
            B.remove(b)
        elif bloc == "C":
            C.remove(b)
    elif move == "B":
        if cloc == "B":
            error()
            return
        else:
            B.append(b)
        if bloc == "A":
            A.remove(b)
        elif bloc == "C":
            C.remove(b)
    elif move == "C":
        if cloc  == "C":
            error()
            return
        else:
            C.append(b)
        if bloc == "A":
            A.remove(b)
        elif bloc == "B":
            B.remove(b)


#--------------------c-----------------------------------------------------#

def c_location():
    global a
    global b
    global c
    global A
    global B
    global C
    global aloc
    global bloc
    global cloc

    if c in A:
        cloc = "A"
        return cloc
    elif c in B:
        cloc = "B"
        return cloc
    elif c in C:
        cloc = "C"
        return cloc



def c_bewegen():
    global a
    global b
    global c
    global A
    global B
    global C
    global cloc

    if cloc == "A":
        move = input("Wohin möchtest du a bewegen? (B/C) ")
        if move == "A":
            error()
    elif cloc == "B":
        move = input("Where do you want to move? (A/C) " )
        if move == "B":
            error()
    elif cloc == "C":
        move = input("Where do you want to move? (A/B) ")
        if move == "C":
            error()

    if move == "A":
        if cloc == "A":
            error()
            return
        else:
            A.append(c)
        if cloc == "B":
            B.remove(c)
        elif cloc == "C":
            C.remove(c)
    elif move == "B":
        if cloc == "B":
            error()
            return
        else:
            B.append(c)
        if cloc == "A":
            A.remove(c)
        elif cloc == "C":
            C.remove(c)
    elif move == "C":
        if cloc == "C":
            error()
            return
        else:
            C.append(c)
        if cloc == "A":
            A.remove(c)
        elif cloc == "B":
            B.remove(c)

#----------------------------------Schleife-------------------------------------------#

def game():
    while True:
        global a
        global b
        global c
        global A
        global B
        global C
        global aloc
        global bloc
        global cloc

        a_location()
        b_location()
        c_location()
        print("Plates:")
        print(" a -> large, b -> middle, c -> small")
        print(A)
        print(B)
        print(C)
        choose_move = input("Which plate do you want to move? (a/b/c) " )
        if choose_move == "a":
            a_bewegen()
        elif choose_move == "b":
            b_bewegen()
        elif choose_move == "c":
            c_bewegen()
        else:
            "unvalid input."

        #End of game
        if C == [a,b,c]:
            print("You solved the game! Congratulations!")
            trigger = input("Do you want to play again? (y/n) ")
            if trigger == "y":
                #Variabel reset
                A = [a,b,c]
                B = []
                C = []

                aloc = ""
                bloc = ""
                cloc = ""
                #Lauching game

                game()
            elif trigger == "n":
                break
            else:
                return

game()