#Sort a list without using inbuild functions
range_limit = input("Enter the limit of the list:\n")

Num =[]
#New_List =[] #this is not required

for i in range (0,range_limit):
    Num.append(input("Enter the elements to be sorted:\n"))

for i in range(0,len(Num)):
    for j in range(i+1,len(Num)):
        if Num[i]>Num[j]:
            Num[i],Num[j] = Num[j], Num[i]

print Num
