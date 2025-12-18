class calender:
    def __init__(self, date, time, name, location):
        self.date = date
        self.time = time
        self.name = name
        self.location = location
    def appointment(self):
        with open("calendar.txt", "a") as f:
            f.write(f"Termin: Name: {self.name} | ")
            f.write(f"Date: {self.date} | ")
            f.write (f"Time: {self.time} | ")
            f.write(f"Location: {self.location}\n")
            f.writable()
        with open("calendar.txt", "r") as f:
            print(f.read())




while True:
    
    option = input("What do you want to do? (check [1], add appointment [2], update appointment [3], exit): ")
    if option == "1":
        f = open("calendar.txt")
        print(f.read())
    elif option == "2":
        name = input("Insert the Name ")
        date = input("Insert Date ")
        time = input("Insert Time ")
        location = input("Insert Location ")

        new_appointment = calender(date, time, name, location)
        new_appointment.appointment()
    elif option == "3":
        print("WiP")
    elif option == "exit":
        print("exiting...")
        break
    else:
        print("Unvalid input. ")
