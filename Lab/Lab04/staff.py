eng = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
alphabet = []
special = []
number = []

engword = eng.split(' ')
Eng = eng.upper()
Engword = Eng.split(' ')
#print(engword)
#print(Engword)

a = str(input())
b = a.split()
#print(b)
len_b = len(b)

math = '1 2 3 4 5 6 7 8 9'
m = math.split(' ')


for i in range(0,len_b) :
  if b[i] in Engword   :
    alphabet.append(b[i])
  if b[i] in engword :
    alphabet.append(b[i])
  if b[i] in m :
    number.append(b[i])
  if b[i] not in Engword and  b[i] not in engword and b[i] not in m: 
    special.append(b[i])

print('Alphabet:',alphabet)
print('Number:',number)
print('Special:',special)

