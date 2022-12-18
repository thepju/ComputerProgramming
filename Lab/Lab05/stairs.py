#elab5 ep5

word = '2 0 7'
word = word.split()

def draw(m) : # m is list 
	for i in range(0,len(m)):
			print(m[i]*(i+1))
			 
while word != ['0'] :
	word = input()
	word = word.split()
	if word != ['0'] :
		draw(word)
	else :
		print('Good Bye.')
		break
