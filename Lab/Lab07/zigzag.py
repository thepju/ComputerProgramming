s = input('Input sentence: ')
#s = 'WeAreTheChampion'
row = int(input('Input row: '))
#row = 5
n = []
for i in range(len(s)) :
	m = []
	for j in range(row) :
		if(len(s) == 0) :	
			m.append('')
		elif(i%(row-1) == 0) :	
			m.append(s[0])	
			s = s[1:]
		elif((i+j)%(row-1) == 0) :	
			m.append(s[0])	
			s = s[1:]
		else :	
			m.append('')
	n.append(m)
	if(len(s) == 0):	break
for i in range(len(n[0])) :
	for j in range(len(n)) :
		print(n[j][i],end='')

