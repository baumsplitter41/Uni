import random
#import tkinter as tk
#from tkinter import Tk
from tabulate import tabulate

quest = ["In welchem Jahr begann der erste Weltkrieg? ",
         "Was kauften die USA im Jahre 1867 vom Russischen Zarenreich? ", "Wann wurde Rom gegründet? ", "In welchem Jar wurde die Berliner Mauer gebaut? ", " Wie nannte man die Armee der Sowjetunion im 20. Jahrhundert? ", "In welchem Jahr fand der Überfall auf Pearl Harbor statt? ", " Welches Ereignis begann mit dem Sturm auf die Bastille 1789? ", "Welche Stadt war die Hauptstadt des Oströmischen Reiches? ", "Wann begang der erster Kreuzzug? ", "An welchem Datum wurde Caesar ermordet? " ]
answers = ["1914", "Alaska", "753 v. Chr.", "1961", "Rote Armee", "1941", "Französische Revolution", "Konstantinopel", "1095", "15.3.44 v. Chr."]


#Funktion Quiz
def quiz():
    #Variablen
    global points, name, data, scoreboard, counter
    counter.clear()
    data.clear()
    points = 0



    #Funktion
    for i in range(len(quest)):
        n = random.randint(0, len(quest)-1)
        counter.append(n)
        if n in counter[0:len(counter)-1]:
                #print("n1:",n)
                while n in counter[0:len(counter)-1]:
                    #print(counter)
                    n = random.randint(0, len(quest)-1)
                    #print("n2:",n)
                    counter.append(n)
        a= str(input(quest[n]))
        if a == answers[n]:
            print("Richtig!")
            points = points+1
            print("Zwischenpunkte: ", points)
        else:
            print("Falsch! Die richtige Antwort wäre:", answers[n])
            if points > 0:
                points = points-1
            print("Zwischenpunkte: ", points)
    data.append([name, points])
    print("Deine Punktzahl: ", name, "->", points)

    

    

"""def interface():
    root = Tk()
    root.title("Willkommen zum Quiz!")

    main_frame = tk.Frame(root)
    main_frame.pack(padx=400, pady=200)
    main_frame.configure(borderwidth=2, relief="solid")

    label = tk.Label(main_frame, text="Willkommen zum Quiz! Drücke OK um zu starten.", font=("Arial", 16))
    label.pack(pady=20)
    Text(master, options)
    button = tk.Button(main_frame, text="OK", font=("Arial", 14), command=quiz)
    button.pack(pady=30)


    root.mainloop()"""

     
#Ausführung des Quiz
data = []
trigger = "j"
while trigger == "j":
    trigger = input("Willst du das Quiz starten? j/n ")
    if trigger == "j":

#Variablen
        name = str(input("Gib deinen Namen ein: "))
        counter= []
        points = 0
        scoreboard = tabulate(data, tablefmt="grid", missingval = "N/A")
#Funktion
        #interface()
        quiz()
#Scoreboard
        
        #print(scoreboard)
        scoreboard = tabulate(data, tablefmt="grid", missingval = "N/A")
        with open("scoreboard.txt", "a") as f:
            f.write(scoreboard)
        with open("scoreboard.txt") as f:
            print(f.read())
    else:
        break