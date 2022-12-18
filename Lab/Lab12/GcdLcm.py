def create_list():
	a = [int(input('a : '))]
	b = [int(input('b : '))]
	return a+b

def list_is_prime() :
	a = []
	for c in range(999) :
		if is_prime(c):	a.append(c)
	return a

def is_prime(n) :
	if n <= 1 : return False
	for i in range(2,n) :
		if n%i == 0 : return False
	return True

def GCD_LCM(n) :
	c= 1
	A = list_is_prime()
	for r in range(999):
		for i in A :
			x,y = n[0]%i,n[1]%i
			if x == 0 and y==0 :
				n[0],n[1] = n[0]//i,n[1]//i  
				c *= i
				break
	return c , c*n[0]*n[1]

#====================main=================
n = create_list()
x,y= GCD_LCM(n)
print('GCD :',x)
print('LCM :',y)