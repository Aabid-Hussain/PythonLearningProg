# Count vowels in a given string using list.
'''
Input_String = "Count vowels in a given string using list"
Input_String_New = Input_String.lower()
count =0
for i in Input_String_New:
    if i in 'aeiou':
        count += 1

print count

'''

Input_String = "Count vowels in a given string using list"
Input_String_New = Input_String.lower()

d = {v: Input_String_New.count(v) for v in 'aeiou'}

print d

