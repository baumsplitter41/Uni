text_raw = input("Fügen Sie den Text ein, welcher geprüft werden soll. ")

das = []
der = []
die = []


text = text_raw.split(" ")

def der_counter():
    global text
    global der
    j= 1
    for i in range(len(text)):
        if "der" == text[i]:
            der.append(j)
            j = j+1
    print("Anzahl der:", len(der))

def das_counter():
    global text
    global das
    j= 1
    for i in range(len(text)):
        if "das" == text[i]:
            das.append(j)
            j = j+1
    print("Anzahl das:", len(das))


def die_counter():
    global text
    global die
    j= 1
    for i in range(len(text)):
        if "die" == text[i]:
            die.append(j)
            j = j+1
    print("Anzahl die:", len(die))



das_counter()
der_counter()
die_counter()