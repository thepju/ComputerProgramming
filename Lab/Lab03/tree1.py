h = int(input('h: '))
c = input('Character: ')
tree_invert = input('Is the tree invert?(y/n): ')
s = h*2 - 1
if tree_invert == 'y' :
	for i in range(h//2) :
		for i in range(1,s//2 +1):
			print(' ',end='')
		for i in range(1) :
			print(c,end='')
		for i in range(1,s//2 +1):
			print(' ',end='')
		print()
	for i in range(s,0,-2) :
		x = s- i
		a = x//2
		if a == 0 :
			print(c*i)
		else :
			print(' '*(a),end='')
			print(c*i,end='')
			print(' '*(a))

else :
	for i in range(1,s+1,2) :
		x = s-i
		a = x//2
		if a != 0 :
			print(' '*a,end='')
			print(c*i,end='')
			print(' '*a,end='')
			print()
		else :
			print(c*i)
	for i in range(h//2):
		print(' '*(s//2),end='')
		print(c,end='')
		print( ' '*(s//2))



	