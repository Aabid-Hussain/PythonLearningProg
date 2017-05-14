# writing program to understand list functions

List_1 = ['apple', 'mango','banana','papaya']
List_2 = ['Man','Woman','Boy','Girl']
print List_1
#append of list items
List_1.append('papaya')
print "The number of payaya is ", List_1.count('papaya')
#extend list: used to add List_1 and List_2
List_1.extend(List_2)
#insert list: used to insert values at defined index
List_1.insert(3,'strawberry')
#POP list: to delete values at defined index
List_1.pop(3)
#remove list: to delete list value which is given in remove function as argument
List_1.remove('mango')
#reverse list: to reverse a list
List_1.reverse()
#sort list: to sort the list
List_1.sort() #Upper case char has lower values than lower Case
print List_1
for i in List_1:
    print i

'''
Extend: takes a list as an argument
append: takes a singleton as an argument'''
List_3 = [1,3,5,6,7]
List_3.extend([11,22,33])
print List_3
List_3.append([44,55,66])
print List_3
