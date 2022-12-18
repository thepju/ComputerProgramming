#elab5 ep2 
n = 1

list_yn = []
list_res = []

while n != 0 :
	n = int(input('Input: '))
	if n != 0 :
		n = str(n)
		for i in range(len(n)) :
			a = int(n[i]) ** (i+1)
			list_res.append(a)
		if (sum(list_res) == int(n)) :
			list_yn.append('Y')
		if (sum(list_res) != int(n)) :
			list_yn.append('N')
	#print(list_res)
	#print(list_yn)
	list_res = []

	n = int(n)
else :
	for i in range(len(list_yn)) :
		print(list_yn[i],end='')
	