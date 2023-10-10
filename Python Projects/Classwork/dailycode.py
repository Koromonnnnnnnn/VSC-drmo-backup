# 9/14/23

# 1
catmeter = input("Do you like cats? Y/N")
if catmeter == 'Y':
    print("meow")
else:
    print("bye")

# 2
height = int(input("Enter your height in inches:"))

if height < 48:
    print("That's not enough inches")
else:
    print("That's tall enough")

# 2
pokemonpreference = input(
    "Favorite pokemon between (P)ikachu, (B)ulbasaur or (C)harizard")

if pokemonpreference == 'P':
    print("pikachu")
elif pokemonpreference == 'B':
    print("bulbasaur")
elif pokemonpreference == 'C':
    print("charizard")
else:
    print("that is not a valid answer!")
