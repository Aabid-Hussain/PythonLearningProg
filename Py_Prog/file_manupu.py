import os

file_name = 'example.txt'

with open(file_name, 'w') as example_file:
    lines = ['Happy whale on parade!\n',
             "Red Bee dancing \n",
             'the great gig in the sky!\n']

    example_file.writelines(lines)

with open(file_name, 'r') as reading_file:
    for line in reading_file.readlines():
        print line

counter = 0
file_content = ' '
with open(file_name,'r') as reading_content:
    file_content = reading_content.read()

new_content = []
for character in file_content:
    if counter %2 ==0:
        new_content.append(character.upper())
    else:
        new_content.append(character.lower())

    counter = counter +1

new_content =''.join(new_content)

with open(file_name,'w') as writeable_file:
    writeable_file.write(new_content)


with open(file_name,'a') as appending_file:
    for char in new_content:
        appending_file.write(char)


print new_content



