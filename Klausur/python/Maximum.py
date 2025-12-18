import random


Liste = [random.sample(range(1, 100),5)]
Max=0

for i in range(len(Liste)):
    if Liste[i] == 6:
        if Liste[i]>Max:
            Max=Liste[i]
print("Die größte a ist: ", Max)