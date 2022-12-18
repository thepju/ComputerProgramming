a = input()
x = 1 
i = 0
while x != 0 :
  b = int(input())
  if b == int(a[i])   :
    i += 1
    if i == 3 :
      print('Succeed!!')
      x = 0
  else :
    print('Fail!!')
    x = 0
