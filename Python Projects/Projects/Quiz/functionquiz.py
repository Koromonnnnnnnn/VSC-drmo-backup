import random
from winsound import Beep

def MultByFive(num):
    num = 5 * num
    print(num)

def Beeps():
    Beep(440, 500)
    Beep(440, 500)
    Beep(440, 500)
    Beep(349, 350)
    Beep(523, 150)
    Beep(440, 500)
    Beep(349, 350)
    Beep(523, 150)
    Beep(440, 1000)
    Beep(659, 500)
    Beep(659, 500)
    Beep(659, 500)
    Beep(698, 350)
    Beep(523, 150)
    Beep(415, 500)
    Beep(349, 350)
    Beep(523, 150)
    Beep(440, 1000)
    

def itemGen():
    num = random.randrange(0,100)
    if num < 20:
        print("Potion")
    elif num < 50:
        print("Cupcake")
    elif num < 75:
        print("Dirty Sock")
    else:
        print("Nothing Appeared")

while True:
    MultByFive(7)
    itemGen()
    Beeps()
    Beeps()

    break;
