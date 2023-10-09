import sys

cases = int(sys.stdin.readline().rstrip()) #get the first number of cases

for i in range(cases): #go through the other lines

    line = sys.stdin.readline().rstrip() 

    line = line.split(" ") #split up the line by spaces

    print(int(line[0])+int(line[1]), int(line[0])*int(line[1]))