# Vierecke zählen
pic = [[0,0,1,1,0,0],
       [0,1,1,1,1,0],
       [1,1,1,1,1,1],
       [1,1,1,1,1,1],
       [0,1,1,1,1,0],
       [0,0,1,1,0,0]]

counter = 0
"""
for zeile in range(len(pic)):
    k = pic[zeile]
    for spalte in range(len(k)):
        if pic[zeile][spalte] == 1:
            counter = counter + 1
print("Anzahl der 1er-Blöcke: " + str(counter))"""




for zeile in range(len(pic)):
    k = pic[zeile]
    for spalte in range(len(k)-1):
        if k[spalte] == 1 and k[spalte+1] == 1 and  or k[spalte] ==1 and k[spalte]+1 == 1:
            counter += 1
print("Anzahl der 2er-Blöcke: " + str(counter))


    
        





