'''
A robot moves in a plane starting from the original point (0,0). The robot can 
move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot 
movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
  
The numbers after the direction are steps. Please write a program to compute 
the distance from current position after a sequence of movement and original 
point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''

from math import sqrt, pow

position = [0,0]

while True:

    InputData = input()

    if not InputData:
        break

    s = InputData.split(" ")
    moves = s[0]
    steps = int(s[1])

    if moves == "UP":
        position[0] += steps

    elif moves == "DOWN":
        position[0] -= steps

    elif moves == "LEFT":
        position[1] -= steps

    elif moves == "RIGHT":
        position[1] += steps

    else:
        pass

print(int(round(sqrt(pow(position[0],2) + pow(position[1],2)))))


