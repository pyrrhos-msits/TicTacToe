import math
money = int(input())

chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

def how_many():
    sheepc = 0
    cowc = 0
    goatc = 0
    pigc = 0
    chickenc = 0
    if money / sheep > 1:
        sheepc = math.floor(money / sheep)
        if sheepc == 1:
            print(sheepc, "sheep")
        else:
            print(sheepc, "sheep")
    elif money / cow > 1:
        cowc = math.floor(money / cow)
        if cowc == 1:
            print(cowc, "cow")
        else:
            print(cowc, "cows")
    elif money / pig > 1:
        pigc = math.floor(money / pig)
        if pigc == 1:
            print(pigc, "pig")
        else:
            print(pigc, "pigs")
    elif money / goat > 1:
        goatc = math.floor(money / pig)
        if goatc == 1:
            print(goatc, "goat")
        else:
            print(goatc, "goats")
    elif money / chicken > 1:
        chickenc = math.floor(money / chicken)
        if chickenc == 1:
            print(chickenc, "chicken")
        else:
            print(chickenc, "chickens")
    else:
        print("None")

how_many()
