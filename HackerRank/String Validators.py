s = "qA2"



print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))


'''
if __name__ == '__main__':
    s = input()
    list_verification = ["isalnum", "isalpha", "isdigit", 
                         "islower", "isupper"]
    
    for i in list_verification:
        print(any("c."+i+"()" for c in s))
'''



