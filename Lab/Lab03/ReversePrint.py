x = 1
y = ['']
count = 0
while x != 0 :
  x = int(input())
  if x != 0 :
   y.append(x)
   count += 1
x = y
for i in range(1,count+1) :
  print(y[-i],end = ' ')
