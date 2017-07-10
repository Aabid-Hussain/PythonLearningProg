'''
grade_sheet_list = [[input(), float(input())] for _ in range(int(input()))]


# grade_sheet_list = [['a', 10.0], ['b', 20.0], ['c', 30.0],
#                     ['d', 40.0], ['e', 50.0]]
second_lowest = sorted(list(
                set([value for name, value in grade_sheet_list])))[1]

print('\n'.join([name for name, value in grade_sheet_list
                 if value==second_lowest]))

'''

list_store = [['a', 10.0], ['abc', 30.0], ['cde', 30.0],
                    ['defg', 40.0], ['efghi', 50.0]]

#take input as str and float and created 2-d list
Length = int(input())
# for _ in range(Length):
#     name = input()
#     score = float(input())
#     list_store.append([name,score])

#sort float value and store list_store[1]

sec_low = sorted(list(set([list_store[i][1] for i in range(Length)])))
sec_low = sec_low[1]

#compair each list with float value and if equal print it's name

temp = [list_store[i][0] for i in range(Length) if sec_low ==list_store[i][1]]

for nam in sorted(temp):
    print(nam)


'''
listlist_storage = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_storage.append([name, score])
        
    #[1] is used to get second lowest    
    second_low = sorted(list(set([s for n,s in list_storage])))[1] 
    #sorted returns list whereas list.sort() returns None
    
    list_storage = [n for n,s in list_storage if s == second_low]
    
    
    for _ in sorted(list_storage): #sorted() is used to sort names of student
        print (_)
'''
