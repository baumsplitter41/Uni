import matplotlib.pyplot as plt
import numpy as np

# Parameter der Gerade
m = 2  # Steigung
b = 1  # y-Achsenabschnitt

# Erstelle Werte für x
x = np.linspace(-10, 10, 400)  # Werte von x von -10 bis 10

# Berechne y-Werte basierend auf der Geradengleichung
y = m * x + b # Vektorfuntkion

# Erstelle das Plot
plt.plot(x, y, label=f'Gerade: y = {m}x + {b}')
plt.title("Verlauf einer Geraden")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black',linewidth=1)  # x-Achse
plt.axvline(0, color='black',linewidth=1)  # y-Achse
plt.grid(True)
plt.legend()

# Zeige das Plot
plt.show()