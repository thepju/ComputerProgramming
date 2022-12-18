g = ['']
c = ['']
w = 0 
sum_credit = 0
sub = int(input('How many subject: '))
for i in range(1,sub+1) :
	credits = int(input(f'Subject {i} Credits: ' ))
	c.append(credits)
	grade = input(f'Subject {i} Grade: ' )
	if grade == 'A' :	g.append(4)
	if grade == 'B+' :	g.append(3.5)
	if grade == 'B'	:	g.append(3)
	if grade == 'C+' :	g.append(2.5)
	if grade == 'C' : g.append(2)
	if grade == 'D+' : g.append(1.5)
	if grade == 'D' :g.append(1)

for j in range(1,sub+1) :
	w += ( g[j]*c[j] )
	sum_credit += c[j]
	
gpa = w / sum_credit

print(f'Output: Total Credit = {sum_credit:.1f} ,GPA = {gpa:.2f}')

