"""
	In this code a recursive function is developed to 
	generate the first n numbers of the Fibonacci series
"""

def  fibonacci(n):

	if n == 1  or n == 0:

		return n;

	else:

		return fibonacci(n-2) + fibonacci(n - 1)


num = int(input(" enter  positive num: "))

if num < 0:
	print("Num is  not valid")

i = 0

print(" fibonacci series: ")

for i in range(0, num):
	print(fibonacci(i))
