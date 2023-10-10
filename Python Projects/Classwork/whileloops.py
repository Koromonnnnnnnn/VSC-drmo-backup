# ------------------------------------P1

choice = "duck"
while choice != "cookie":
    print(choice)
    choice = input("type cookie to quit: ")

print("no more cookies. goodbye.")

# ------------------------------------P2

num = 100
while num > 5:
    print(num, end=" ")
    num -= 7

# ------------------------------------P3

num = 0
while num <= 50:
    print(num, end=" ")
    num += 5

# ------------------------------------P4

counter = 0
num = 1

while num <= 50:
    print(counter, end=" ")
    num *= 2
    counter += 1
