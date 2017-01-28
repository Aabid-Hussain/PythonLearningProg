# uncomment the following lines to take input from the user

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
  # print num, "*"
   if num > 1:
       for i in range(2,num):
          # print i, "**"10

           if (num % i) == 0:
               break
       else:
           print (num)