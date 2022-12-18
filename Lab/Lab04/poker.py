def find(a,n):
 res = -1
 for i in range(len(a)):
  if(a[i] == n):
   res = i
   return res
 return res





#a = '7 7 10 7 7'
a = input('Cards: ')
a = a.split()
len_a = len(a)
card = []
count = []
for i in range(len_a):
 x = find(card,a[i])
 if(x == -1):
  card.append(a[i])
  count.append(1)
 elif(x != -1):
  count[x] += 1

mymax = max(count)
if(mymax == 1):
 print('Mark got "High Card"')
elif(mymax == 3):
 if(2 in count):
  print('Mark got "Full House"')
 else:
  print('Mark got "Three of a kind"')
elif(mymax == 4):
 print('Mark got "Four of a kind"')