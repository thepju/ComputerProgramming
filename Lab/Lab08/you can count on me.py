#elab 8
filename = input('File name: ')
#filename = 'input.txt'
with open(filename,'r') as f:
	f_contents = f.readlines() 

#len sent 
for i in f_contents :
	if i != '' :
		sent = i.strip().split('.')
lensent = 0 		
for i in sent :
	if i != '' :
		lensent += 1
#len word
for i in f_contents :
	if i != '' :
	   word = i.split()
lenword = 0 
for i in word :
	if i != '' :
		lenword += 1
print(f'There are {lensent} sentences and {lenword} words.')