n = int(input("N: "))
price = 0
#print(n)
while n != 0 :
	if n >= 15 : 
		price += 3000
		n -= 15
	elif n >= 14 : 
		price += 3000
		n -= 14
	elif n >= 13 : 
		price += 3000
		n -= 13
	elif n >= 12 : 
		price += 3000
		n -= 12
	elif n >= 11 : 
		price += 3000
		n -= 11
	elif n >= 5 :
		price += 1500
		n -= 5
	elif n ==4 :
		price += 1500
		n -= 4
	elif n >= 2 :
		price += 800
		n -= 2
	elif n == 1 :
		price += 500
		n -= 1

print(price)  