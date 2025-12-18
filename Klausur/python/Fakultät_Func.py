def falcutaet(num: int):
    if num == 1:
        return 1
    else:
        return falcutaet(num-1)*num


num_in = input("Insert a Number ")

if num_in is int:
    num = int(num_in)


    solution = falcutaet(num)


    with open("falcutaet.txt", "a") as file:
        file.write(f"faculaet of {num} if {solution} \n")
    with open("falcutaet.txt", "r") as file:
        print(file.read())
else:
    print("Error: input a Number!")