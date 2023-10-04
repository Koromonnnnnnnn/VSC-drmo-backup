#1 Write a python while loop that continuously says "AH CHOO!" until the user types "bless you". 

password = ''

while password != 'bless you':
    print('AH CHOO!')
    password = input()

#2 Write a python while loop that prints out the numbers 20 through 200 counting by 10s. 

num = 20
while num <= 200:
    print(num, end = " ")
    num+=10

#3 Write a python while loop that prints out the number 80 and subtracts 5 until the number reaches 35, printing each number as it goes.

num = 80
while num > 35:
    print(num, end = " ")
    num-=5