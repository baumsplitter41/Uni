#Schreibe ein Programm, das einen Satz vom Benutzer einliest und ausgibt:
#1. Wie viele Wörter der Satz enthält
#2. Wie viele Zeichen (ohne Leerzeichen) der Satz enthält
#3. Wie viele Vokale (a, e, i, o, u) im Satz vorkommen




input = input("Insert text. ")

def count_word():
    global input
    words = input.split(" ")
    print("Count Words:", len(words))

def count_chars():
    global input
    chars_raw= input.split(" ")
    chars = []
    for i in range(len(chars_raw)):
        j = chars_raw[i]
        j = str(j)
        char_prog = j.split(1)
    print(len(char_prog))

count_word()
count_chars()