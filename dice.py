import random
choice = 'y'
while choice == 'y':
    number = random.randint(1, 6)
    if number == 1:
        print("-----------")
        print("|         |")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("|         |")
        print("-----------")
    if number == 2:
        print("-----------")
        print("|         |")
        print("|         |")
        print("| 0     0 |")
        print("|         |")
        print("|         |")
        print("-----------")

    if number == 3:
        print("-----------")
        print("|         |")
        print("|    0    |")
        print("|    0    |")
        print("|    0    |")
        print("|         |")
        print("-----------")

    if number == 4:
        print("-----------")
        print("| 0     0 |")
        print("|         |")
        print("|         |")
        print("|         |")
        print("| 0     0 |")
        print("-----------")
    if number == 5:
        print("-----------")
        print("| 0     0 |")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("| 0     0 |")
        print("-----------")

    if number == 6:
        print("-----------")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("-----------")
    choice = input("Press y to roll the dice: ")
