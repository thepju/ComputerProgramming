#elab 8

def writetext(s) :
	with open('Example.txt','w') as f :
		f.write(s)

def btof(numbers) :
	for i in range(len(numbers)):
		(numbers[i].sort(reverse = True))
	for i in range(len(numbers)):
		numbers[i].pop()
		numbers[i].pop(0)
	return numbers

s = '''Non 9 8 7 8 8
Prince 3 5 4 2 10
Khanun 7 7 9 9 6
Plapud 0 9 7 8 10
Queen 10 7 7 8 7'''
#writetext(s)

filename = input('File name: ')
#readtext
with open(filename,'r') as f :
	f_contents = f.readlines()
#print(f_contents)

#sperate data
alldata = []
for i in f_contents:
	if i.strip() != '' :
		tmp = []
		for j in i.strip().split() :
			tmp.append(j)
		alldata.append(tmp)   	
#print(alldata)
#name  
names = [i[0] for i in alldata ]
numbers = [ [int((alldata[i][j])) for j in range(1,len(alldata[0]))] for i in range(len(alldata))] 
numbers = (btof(numbers))
sumscore = [sum(numbers[i]) for i in range(len(numbers))]
maxscore = max(sumscore)
iscore = [(i) for i in range(len(sumscore)) if sumscore[i] == maxscore]
print(maxscore)
for i in iscore :
	print(names[i])
