yesno = input("Do you like PB Sandwiches? Y/N")

if yesno == 'Y':
    print("IT'S PEANUT BUTTER JELLY TIME!!!")

howcold = int(input("How cold is it today? (Farenheit)"))

if howcold <= 60:
    print("Please wear a jacket.")
else:
    print("A t-shirt is fine.")

catdogfish = input("Do you like (C)ats, (D)ogs or (F)ish more?")

if catdogfish == 'C':
    print("meow")
elif catdogfish == 'D':
    print("woof")
elif catdogfish == 'F':
    print("blub blub")
else:
    print("That's not a valid option")

