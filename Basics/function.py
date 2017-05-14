'''
# fun defined for sum and product
def sum_prod(n1,n2):
	print "{} and {} sum ={}".format(n1,n2,n1+n2)
	print "{} and {} product ={}".format(n1,n2,n1*n2)
	return

sum_prod(input("Enter the first number:\n"),input("Enter the second number:"))

def range1(x):
	list1=[]
	i=0
	while i<x:
		list1.append(i)
		i +=1
	return list1

print range1(input("Enter the range limit\n"))
'''
