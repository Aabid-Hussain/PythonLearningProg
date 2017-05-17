#E:\ME\PythonLearningProg\textfile\DUT.txt
import re


def ReadFile(filepath):

    fob = open(filepath,'r')
    divStore = {}
    for line in fob.readlines():
        match = re.search(r'(.*)=.*\"(.*)\"',line)
        if not match:
            print("File syntax is incorrect")
            return 0
        else:
            key = match.group(1)
            value = match.group(2)
            divStore[key.strip()] = value.strip()
    fob.close()
    return divStore

filepath = ReadFile("E:\\ME\\PythonLearningProg\\textfile\\DUT.txt")

for key in filepath.keys():
    print(key)
    print()

for value in filepath.values():
    print(value)
    print()








