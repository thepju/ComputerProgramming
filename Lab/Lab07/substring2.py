def isornot(n,m) :
	a = []
	for i in range(len(m)) :
		if n[i] == m[i] :
			a.append(1)
		else :
			a.append(0)
	return a
tx = input('Text: ')
sub = input('Substring: ')
final = ''
if tx.find(sub) == -1 :
	while len(tx) >= len(sub) :
		b = isornot(tx[0:len(sub)],sub)
		if b.count(0) <2 :
			c = ''
			for i in range(len(sub)) :
				if b[i] == 1:
					c += sub[i] 
				elif b[i] == 0 :
					c += '?'
			final = final + '[' + c + ']'
			tx = tx[len(sub):] 
		else: 
			final += tx[0]
			tx = tx[1:]
		if len(tx) < len(sub) :
			final += tx
else : 
	while len(tx) >= len(sub) :
		if tx[0:len(sub)] == sub :
			final = final + '['+ sub + ']'
			tx =tx[len(sub):]
		else :
			final += tx[0]
			tx = tx[1:]
		if len(tx) < len(sub) :
			final += tx
print(final)