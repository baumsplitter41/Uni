letters = ["a","b","c"]

for i in range(len(letters)-1):
    print(letters)
    letters.append(letters[0])
    letters.remove(letters[0])
for i in range(len(letters)):
    letters.append(letters[1])
    letters.remove(letters[1])
    print(letters)
