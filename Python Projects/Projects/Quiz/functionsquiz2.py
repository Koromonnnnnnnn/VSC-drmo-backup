#1 ========
def simpleCalculator(x, y, z):
    if z == "add":
        print(x + y)
    elif z == "subtract":
        print(x - y)
    else:
        print("Invalid")
        
simpleCalculator(1, 2, "add")

#2 ========

def candyDispenser(num):
    target = 0
    mnm = "ok, here are some m&m"
    snicker = "ok, here are some snicker"
    while num != target:
        print("You have ", num, "pieces of candy left!" )
        selection = input("Would you like snickers or m&ms?")
        
        if selection == "m&ms":
            print(mnm)
            num -= 1
        elif selection == "snickers":
            print(snicker)
            num -= 1

candyDispenser(5)

#3 ========

def OobaAdder():
    selection = input("enter a word")
    print(selection+"ooba")
    
OobaAdder()