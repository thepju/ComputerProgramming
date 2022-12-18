def chartoint(num) :
	for i in range(len(num)) :
		num[i] = int(num[i])
	return num

def mintomax(num) :
	num.sort()
	return num

def cut(num) :
	num = list(set(num))
	return num

num = input().split()
num = chartoint(num)
num = cut(num)
num = mintomax(num)

for i in num :
	print(i,end=' ')
