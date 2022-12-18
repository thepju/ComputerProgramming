n = int(input('n = '))
m = int(input('m = '))

#n = 5
#m = 4

scores = []
names = [] #a 
a = []

def findmax(a,n,m) : # a is list
	a = []
	lastsumscores = 0
	count = 1 
	x = 0

	for i in range(0,n,1): #รอบ 			for Round in range(n):
		scores = []
		k = input().split()
		#k = 'happy 9 8 7 8'.split()
		#print(k)
		for j in range(1,m+1) : #คะแนน
			x = k[j]
			scores.append( int(x) ) #คะแนน 

		scores.sort()
		scores.pop(0)
	
		if sum(scores) > lastsumscores :
			lastsumscores = sum(scores)
			a.clear()

		if sum(scores) == lastsumscores :
			count +=1
			a.append(k[0])

		else :
			continue
		#print(lastsumscores,a)

	return lastsumscores,a
#findmax(names,n,m)

def printans(maxi,name): 
	print(maxi)
	for i in name :
		print(i)

maxi,name = findmax(a,n,m)

printans(maxi,name)



	


