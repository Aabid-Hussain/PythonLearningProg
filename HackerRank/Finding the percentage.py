
value = 0
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    #scores = list(map(float, line))
    # for items in scores:
    #     value += float(items)
    #grade = value/len(scores)
    #student_marks[name] = grade
    #value = 0
    student_marks[name] = sum(map(float,line))/len(line)

query_name = input()
if query_name in student_marks.keys():
    print("{:.2f}".format(student_marks[query_name]))


