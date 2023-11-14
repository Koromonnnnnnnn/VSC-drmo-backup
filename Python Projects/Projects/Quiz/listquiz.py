ThanksGiving = [3, "Cake", True, 2.0]

print(ThanksGiving)

ThanksGiving.append("sushi")

if ThanksGiving[4] == "sushi":
    print(ThanksGiving[4])

print(ThanksGiving[0])
print(ThanksGiving[4])

ThanksGiving[0] = 17

size = len(ThanksGiving)
print("Size is: ")
print(size)

print("New list is: ")
print(ThanksGiving)