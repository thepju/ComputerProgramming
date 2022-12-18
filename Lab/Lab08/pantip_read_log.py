filename = input('File name: ')
#filename = 'pantip-read-20181015-20181222.csv'
with open(filename,'r') as f :
	f_content = f.readlines()
number = int(input('enter number: '))
#number = 7
nf = []

for i in f_content :
	tmp = []
	if i != '':
		for j in i.strip().split(',') :
			tmp.append(j)
		nf.append(tmp)

if number == 1 : 
	print(len(nf))

if number == 2 :
	allroom =[]
	for i in range(len(nf[0])-1) : #แถว
		ns = 0
		for j in range(1,len(nf)):
			ns += int(nf[j][i])
		allroom.append(ns)
	for i in range(len(allroom)) :
		if allroom[i] == max(allroom) :
			print(nf[0][i])
			break

if number == 3 :
	blue = []
	for i in range(len(nf[0])) :
		if nf[0][i] == 'blueplanet':
			for j in range(1,len(nf)):
				blue.append(int(nf[j][i]))
			blue.sort(reverse = True)
			blue = blue[0:3]
			for i in blue :
				print(i,end=' ')
			break 

if number == 4 :
	user = []
	resmax = -1
	for i in range(1,len(nf)):
		res = 0
		for j in range(len(nf[0])-1):
			res += int(nf[i][j])
		if res > resmax :
			resmax = res
			c = i
		user.append(res)
	print(nf[c][-1],max(user)) 

if number == 5 :
	tvshow = []
	resmax2 = -1
	for j in range(1,len(nf)):
		tvshow.append(int(nf[j][0]))
		if int(nf[j][0]) > resmax2 :
			resmax2 = int(nf[j][0])
			c = j
	print(nf[c][-1],resmax2 )
#ห้อง korea มี user ที่กดอ่านมากกว่า 500 กระทู้ทั้งหมดกี่คน
if number == 6 :
	for i in range(len(nf[0])) :
		if str(nf[0][i]) == 'korea' :
			c = i
	korea = []
	for i in range(1,len(nf)):
		if int(nf[i][c]) > 500 :
			korea.append(int(nf[i][c]))
	print(len(korea))

sumuser = [ ]
for i in range(1,len(nf)):
	sumuse = 0
	for j in range(len(nf[0])-1):
		sumuse += int(nf[i][j])
	sumuser.append(sumuse)

if number == 7 :
	for i in range(len(nf[0])) : #nf คือ listของแต่ละบรรทัดครับ
		if str(nf[0][i]) == 'siam' :
			c = i
			#print(c)
		if str(nf[0][i]) == 'food' :
			x = i
			#print(x)
	countS = 0
	for i in range(1,len(nf)): 
		if int(nf[i][c]) > int(nf[i][x]) :
			countS +=1
	#print(countS)
	#print(countF)		
	res = (countS)
	print(res)

if number == 8 :
	for i in range(len(nf[0])) :
		if str(nf[0][i]) == 'rajdumnern' :
			c = i
			break
	resmax = -1
	for i in range(1,len(nf)):
			res = (int(nf[i][c]))/sumuser[i-1]
			if res > resmax :
				resmax = res
				user = (nf[i][-1])
	print(user)

if number == 9 :
	a = [ ]
	for i in range(1,len(nf)):
		tmp = []
		for j in range(len(nf[0])-1):
			tmp.append(int(nf[i][j]))
		tmp.sort(reverse =True)
		a.append(sum(tmp[0:2]))
	c= 0
	for i in range(len(nf)-1) :
		if a[i]/sumuser[i] * 100 > 70 :
			c += 1
	print(c)
if number == 10 :
	for i in range(len(nf[0])) :
		if str(nf[0][i]) == 'pantip' :
			c = i
			break
	user = []
	for i in range(1,len(nf)) :
		if int(nf[i][c]) == 0 :
			user.append(nf[i][-1])
	print(len(user))