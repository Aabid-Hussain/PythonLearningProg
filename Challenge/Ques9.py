'''Write a program that accepts sequence of SampleVars as input and prints the SampleVars after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT'''


SampleVars= []

while True:
    InputData = raw_input()
    if InputData:
        SampleVars.append(InputData.upper())
    else:
        break

for line in SampleVars:
    print line