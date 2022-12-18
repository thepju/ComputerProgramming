tmp = int(input())
last_tmp = 0 
count = 0

if tmp == 0 : 
	print('No positive input!')

while tmp != 0 :
	if tmp > 0 :
		count += 1
		tmp = int(input())
	if tmp < 0 :
		tmp = int(input())
	if tmp == 0 :
		if count == 0 :
			print('No positive input!')
		else :
			print(f'I found {count} positive integer(s).')	
		break
