import random


def MonsterGen():
    num = random.randrange(0, 100)
    if num < 20:
        print("A skeleton has appeared")
    elif num < 50:
        print("A zombie chases you")
    elif num < 80:
        print("A spider attacks")
    else:
        print("Nothing Appeared")


while True:
    MonsterGen()
    choice = input("Enter any key to continue...")
