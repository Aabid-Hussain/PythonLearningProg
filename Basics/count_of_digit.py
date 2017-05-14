num=input("enter the number to find digits count:")
count=0
if num>=0 or num<0:
    count+=1

while (num>10 or num<-10):
    count+=1
    num=num/10

print count
