a= input("Input a Number: ")
quersumme = 0
probe_array = []

def neunerprobe(a):
    global quersumme
    global probe_array
    

    if int(a) >= 10:
        quersumme = sum(int(position) for position in a if position.isdigit())
        probe = sum(int(position) for position in str(quersumme) if position.isdigit())
        probe_array.append(probe)
        while int(quersumme) >= 10:
            quersumme = sum(int(position) for position in str(quersumme) if position.isdigit())
            if int(quersumme) >= 10:
                probe = sum(int(position) for position in str(quersumme) if position.isdigit())
                probe_array.append(probe)
    else:
        print("Number to short.")
    if quersumme == 9:
        quersumme = 0
    probe_var = sum(probe_array[0:len(probe_array)])
    print("Neunerrest:", quersumme)
    print("Neunerprobe:", probe_var)

neunerprobe(a)