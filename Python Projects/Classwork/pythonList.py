myStuff = ["Game", "15", "Silly", 5.8, True]

print(myStuff[0])
print(myStuff[4])

myStuff[2] = "banana"

if myStuff[2] == "banana":
    print(myStuff[2])

myStuff.append("cheesecake")

if myStuff[5] == "cheesecake":
    print(myStuff[5])

size = len(myStuff)
print(size)

print(myStuff)
