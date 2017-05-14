num=input("enter the number to find digits count:")
sum=0

while (num>0):
    sum+=num%10
    num=num/10

print sum
