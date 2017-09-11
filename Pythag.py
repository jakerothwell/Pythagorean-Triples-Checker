import time

def gcd(x, y):
	
	if x > y:
		smaller = int(y)
	else:
		smaller = int(x)
	for i in range(1, smaller+1):
		if((x % i == 0) and (y % i == 0)):
			g = i

	return g

def coprime(a, b, c):
	
	num = reduce(lambda x, y: gcd(x,y), [a, b, c])
	#print(num)
	if num == 1:
		print("Yes! This triangle is a Pythagorean Triple.")
	else:
		print("No. This traingle is not a Pythagorean Triple.")



def get_input():
	
	print("Please enter 3 positive integers, representing 3 sides of the triangle.")
	time.sleep(0.5)
	first = raw_input("Side 1: ")
	second = raw_input("Side 2: ")
	third = raw_input("Side 3: ")

	if first >= second and first >= third:
		c = int(first)
		b = int(second)
		a = int(third)
	if second >= first and second >= third:
		c = int(second)
		b = int(first)
		a = int(third)
	if third >= second and third >= first:
		c = int(third)
		b = int(second)
		a = int(first)

	
	coprime(a, b, c)

while(1):

	get_input()






