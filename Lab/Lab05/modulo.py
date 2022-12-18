#elab5 ep1 
n = int(input('N: '))
b = int(input('M: '))
c = []
newC = []

for line in range(1,n+1) :
	a = int(input(f'Input number {line}: '))
	c.append(a%b)
c = list(set(c))
print(len(c))