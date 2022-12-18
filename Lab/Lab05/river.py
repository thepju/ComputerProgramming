def river(list_river,n) :
	list_river.append(n) 
	a = str(n)
	b = int(a)
	for count in range(999) :
		for i in range(len(list(a))) : #2
			b += int( list(a)[i] )
		list_river.append(b)
		a = str(b)
	return list_river

list_river1 = []
list_river2 = []

n = input('N: ')
#n = '86' 	# 89       1        101
#print(river(list_river1,n))
for i in river(list_river1,n) : #101
	#print('i is ',i)
	for m in [1,3,9] : #1
		#print('m is ',m)
		for j in river(list_river2,m) : #101
			#print(list_river2,m)
			#print('j is ',j)
			if i == j : #101 = 101
				print(m,i)
				break
		if i == j :
			break
	if i == j :
		break






