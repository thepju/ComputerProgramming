days = int(input('Day: '))
f1 = 1 
f2 = 1 
if days <= 2 :
  if days < 2 :
    print(f1,end=" ")
  else :
    print(f1,end=" ")
    print(f2,end=" ")

else :
  print(f1,end=" ")
  print(f2,end=" ")
  for i in range(days-2) :
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3,end=" ")