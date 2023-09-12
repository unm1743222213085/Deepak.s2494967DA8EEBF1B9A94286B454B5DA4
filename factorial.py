
def factorial(n):
	
	
	if (n==1 or n==0):
		
		return 1
	
	else:
		
		return (n * factorial(n - 1))

num = int(input("enter a num : "))

res=factorial(num)
print(f'The factorial of number {num} is {res}')
