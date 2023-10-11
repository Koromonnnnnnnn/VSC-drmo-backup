for i in range(6, 37, 3):
    print(i, end=" ")

minutesExcersize = int(
    input("How many minutes of excersize do you get every week?: "))

if minutesExcersize <= 20 and minutesExcersize < 100:
    print("Not enough exercize")
elif minutesExcersize >= 100 and minutesExcersize < 500:
    print("Perfect amount of exercize")
elif minutesExcersize > 500:
    print("That's alot of exercize, make sure to get enough water and protein!")
