n = int(input('n: '))
#n = 10
a = 1
b = 1
x = 2*n+3
y = x - 2

for i in range(1,n*2+1) :
  if i % 2 != 0 :
    print(' '*(i-a),end='') 
    print('='*x)
    a += 1
    x -= 2
  else :
    print(' '*(i-a),end='')
    print('=',end='')
    print('#'*y,end='') 
    print('=')
    y -= 2 

x = 2*n+3
y = x//2
a = 1

for i in range(2*(n//2)) :
  if i % 2 == 0 :
    print(' '*y,end='')
    print('='*b)
    b += 2
    y -= 1
  else : 
    print(' '*y,end='')
    print('=',end='')
    print('#'*a,end='')
    print('=',)
    a +=2


