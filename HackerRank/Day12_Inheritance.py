class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name: {}, {}".format(self.lastName, self.firstName))
        print("ID: {}".format(self.idNumber))

class Student(Person):
    sum_value = 0
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName,lastName, idNumber)
        self.scores = scores

    def calculate(self):
        sum_value = int(sum(self.scores) / len(self.scores))
        # print(sum_value)
        if sum_value >= 90 and sum_value <= 100:
            return 'O'

        elif sum_value >= 80 and sum_value < 90:
            return 'E'
        elif sum_value >= 70 and sum_value < 80:
            return 'A'
        elif sum_value >= 55 and sum_value < 70:
            return 'P'
        elif sum_value >= 40 and sum_value < 55:
            return 'D'
        else:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list(map(int, input().split()))
s = Student(firstName,lastName,idNum,scores)
s.printPerson()
print("Grade:", s.calculate())

'''
David Park 6735139
8
100 100 100 100 100 100 100 100
Name: Park, David
ID: 6735139
Grade: O
'''