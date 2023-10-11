from winsound import Beep

# 1

for i in range(6, 37, 3):
    print(i, end=" ")


# 1 Function Version

def CountByThrees():
    for i in range(6, 37, 3):
        print(i, end=" ")
        print(i, end=" ")

CountByThrees()

# 2

minutesExcersize = int(
    input("How many minutes of excersize do you get every week?: "))

if minutesExcersize <= 20 and minutesExcersize < 100:
    print("Not enough exercize")
elif minutesExcersize >= 100 and minutesExcersize < 500:
    print("Perfect amount of exercize")
elif minutesExcersize > 500:
    print("That's alot of exercize, make sure to get enough water and protein!")


# 2 Function Version


def exerciseCheck():
    minutesExcersize = int(
        input("How many minutes of excersize do you get every week?: "))

    if minutesExcersize <= 20 and minutesExcersize < 100:
        print("Not enough exercize")
    elif minutesExcersize >= 100 and minutesExcersize < 500:
        print("Perfect amount of exercize")
    elif minutesExcersize > 500:
        print("That's alot of exercize, make sure to get enough water and protein!")

exerciseCheck()

# 3

num = int(
    input("How many times would you like to beep?")
)

numCount = 1

while numCount <= num:
    Beep(440, 500)
    numCount+=1


# 3 Function Version


def UserBeeps(num):
    numCounter = 1
    while numCounter <= num:
        Beep(440, 500)
        numCounter += 1


UserBeeps(int(
    input("How many times would you like to beep?")
))
