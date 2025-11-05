# Import the tabulate module
from tabulate import tabulate


name = input("Name")
profession= input("Job")

# Sample data: list of lists
data = [
    [name, profession],
    ["Alice", "Engineer"],
    ["Bob","Data Scientist"],
    ["Charlie", "Teacher"]
]


data.append([name, profession])


# Creating a table with headers and a grid format
table = tabulate(
    data, 
    headers=["Name", "Profession"], 
    tablefmt="grid"
)



print(table)