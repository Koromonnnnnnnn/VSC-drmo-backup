def rocketLaunch():
    start = 10
    end = 0
    counter = start
    while counter != end:
        print(counter)
        counter -= 1
    print("Blast off!")


rocketLaunch()


def elevatorCheck(x):
    if x > 1000:
        print("overloaded!")
    elif x <= 1000:
        print("not overloaded!")


elevatorCheck(166)


def trafficLight(x):
    if x == "Green":
        print("go")
    elif x == "Red":
        print("Stop")
    elif x == "Yellow":
        print("Slow down")


trafficLight("Red")


def calculatePrice(x):
    kidsPrice = 10
    teenPrice = 20
    seniorPrice = 15
    if x > 12 and x > 19 and x > 65:
        print("old")
        return seniorPrice
    if x > 12 and x <= 19:
        print("teen")
        return teenPrice
    if x <= 12:
        print("kid")
        return kidsPrice


calculatePrice(12)


def validatePassword():
    password = ''

    while password != 'Metroid110':
        print('Wrong passoword, try again')
        password = input()
    print("Im in!")


validatePassword()
