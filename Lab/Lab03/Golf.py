sum_score = 0 
par = input()
list_par =  par.split(' ') # คือ การใส่คะแนนที่ได้
score = input()
list_score = score.split(' ') # คือการใส่คะแนนของสนาม
for i in range(9) :
	if list_score[i] == 'Ea' :	sum_score += int(list_par[i])-2
	if list_score[i] == 'Bi' :	sum_score += int(list_par[i])-1
	if list_score[i] == 'Pa' :	sum_score += int(list_par[i])
	if list_score[i] == 'Bo' :	sum_score += int(list_par[i])+1
	if list_score[i] == 'DB' :	sum_score += int(list_par[i])+2	
print(sum_score)

