import random
from tabulate import tabulate
import colorama
from colorama import Fore, Back, Style

quest = ["In welchem Jahr begann der erste Weltkrieg? ",
         "Was kauften die USA im Jahre 1867 vom Russischen Zarenreich? ", "Wann wurde Rom gegründet? ", "In welchem Jahr wurde die Berliner Mauer gebaut? ", " Wie nannte man die Armee der Sowjetunion im 20. Jahrhundert? ", "In welchem Jahr fand der Überfall auf Pearl Harbor statt? ", " Welches Ereignis begann mit dem Sturm auf die Bastille 1789? ", "Welche Stadt war die Hauptstadt des Oströmischen Reiches? ", "Wann begang der erste Kreuzzug? ", "An welchem Datum wurde Caesar ermordet? " ]
answers = ["1914", "Alaska", "753 v. Chr.", "1961", "Rote Armee", "1941", "Französische Revolution", "Konstantinopel", "1096", "15.3.44 v. Chr."]


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
            print(Fore.GREEN + "Richtig!")
            print(Style.RESET_ALL)
            points = points+1
            print("Zwischenpunkte: ", points)
            print("")
        else:
            print(Fore.RED + "Falsch! Die richtige Antwort wäre:", answers[n])
            print(Style.RESET_ALL)
            if points > 0:
                points = points-1
            print("Zwischenpunkte: ", points)
            print("")
    data.append([name, points])
    print("Deine Punkta: ", name, "->", points)


     
#Ausführung des Quiz
data = []
trigger = "ja"
while trigger == "ja":
    trigger = input("Willst du das Quiz starten? ja/nein ")
    if trigger == "ja":

#Variablen
        name = str(input("Gib deinen Namen ein: "))
        counter= []
        points = 0
        scoreboard = tabulate(data, tablefmt="grid", missingval = "N/A")
#Funktion
        #interface()
        print("Groß- und kleinschreibung muss beachtet werden! Erster Buchstabe immer groß. Bei vor Christus muss 'v. Chr.' geschrieben werden.")
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