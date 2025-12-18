import matplotlib.pyplot as plt
import numpy as np
import csv

datei = "diode.csv"

U = []
I = []

with open(datei, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # Header überspringen
    next(reader)
    for row in reader:
        U.append(float(row[0]))
        I.append(float(row[1]))

U = np.array(U)
I = np.array(I)


# Erstelle das Plot
plt.plot(U, I, label='Kennline Si-Diode')
plt.scatter(U, I, color='blue', s=50, marker='o', label='Messpunkte')
plt.title("U-I Kennlinie")
plt.xlabel("U in V")
plt.ylabel("I in mA")
plt.axhline(0, color='black',linewidth=1)  # x-Achse
plt.axvline(0, color='black',linewidth=1)  # y-Achse
plt.grid(True)
plt.legend()

# Zeige das Plot
plt.show()
