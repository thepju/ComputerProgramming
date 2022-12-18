x = int(input('Distance from starting point(m.): '))
c = 0
i = 0
if x > 0 :
  while i < x :
    i += 5
    print(i,end=' ') 
    i -= 2 
    print(i,end=' ')
    c += 1 
  while i > x :
    i -= 4
    print(i,end=' ')  
    i += 3
    print(i,end=' ')  
    c += 1 
    if i == x : 
       print('')
       print(f'Buzz moved {c} set(s)')
elif x == 0 : 
  while i==x :
    print(i)
    break
  print(f'Buzz moved {c} set(s)')
elif x < 0 :
  while i > x :
    i -= 4
    print(i,end=' ') 
    i += 3 
    print(i,end=' ')
    c += 1 
  while i > x :
    i -= 4
    print(i,end=' ')  
    i += 3
    print(i,end=' ')  
    c += 1 
  if i == x : 
       print('')
       print(f'Buzz moved {c} set(s)')