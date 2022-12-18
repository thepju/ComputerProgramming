n = input('Text: ').split()
chain = [] 
count = 1 
for i in range(len(n)):
	word= 0 
	for j in range(len(n[i])):
		if(i == len(n) - 1 ) :
			chain.append(count)
			break
		elif len(n[i]) != len(n[i+1]):
			chain.append(count) 
			count =1 
			break
		elif(n[i][j] != n[i+1][j] ) :
			word += 1 
	if word <3 :
		count += 1
	elif word>2 :
		chain.append(count) 
		count = 1

print(len(chain),'Chain(s). Maximum length is',max(chain),'word(s).') 