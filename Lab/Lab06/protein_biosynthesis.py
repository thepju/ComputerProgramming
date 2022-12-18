def dnatorna(n):
 a = ''
 for i in range(len(n)):
  if(n[i] == 'A'):
   a+= 'U'
  elif(n[i] == 'C'):
   a+= 'G'
  elif(n[i] == 'G'):
   a+= 'C'
  elif(n[i] == 'T'):
   a+= 'A'
 return a

#dna = 'CGTGGAACAACGCGGACAAGCGTACCTGCATCTAATTA'
dna = input('DNA: ')
rna = dnatorna(dna)
#print(rna)

start = 'AUG'
stop = ['UAA','UGA','UAG']
x = len(rna)
for i in range(0,len(rna)):
 #print(rna[i:i+3])
 if(rna[i:i+3] == start):
  x = i
  break
 
amino = 0
#print(rna[x:])
for i in range(0,len(rna[x:]),3):
 #print(rna[x+i:x+i+3])
 if (rna[x+i:x+i+3] in stop):
  break
 else:
  amino += 1
print(amino,'Amino acid(s)')