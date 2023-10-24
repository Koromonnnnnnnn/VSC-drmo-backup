def frog_jump(num):
    for i in range(num):
        print("Jump #", i, "Ribbit")

frog_jump(5)

#-------------

def guess_number(target):
    guess_numberz = -1
    while target != guess_numberz:
        guess_numberz = int(
            input("guess a number!")
        )
        if guess_numberz == target:
            print("you guessed right!")
        elif guess_numberz > target:
            print("too high")
        else: 
            print("too low")
            
guess_number(42)

#-------------

def isVampire(x, y):
    if x > 1000 and y == False:
        print("Vampire!")
    else: 
        print("Not Vampire")

isVampire(40000, False)

#-------------

def rocketLaunch(fuel, astronauts):
    equation = astronauts * 100
    if fuel < equation:
        print("Insufficient fuel!")
        return "Insufficient fuel!"
    elif fuel >= equation:
        print("Launch succesful!")
        return "Launch succesful!"
        
rocketLaunch(600,3)