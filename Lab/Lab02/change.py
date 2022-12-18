x = int(input(''))
if x >= 1000:
  x1 = x//1000
  print(f'1000 => {x1}')
  x -= x1*1000
if x < 1000 :
  x2 = x//500
  print(f'500 => {x2}')
  x -= x2*500
if x < 500 :
  x3 = x//100
  print(f'100 => {x3}')
  x -= x3*100
if x < 100 :
  x4 = x//50
  print(f'50 => {x4}')
  x -= x4*50
if x < 50 :
  x5 = x//20
  print(f'20 => {x5}')
  x -= x5*20
if x < 20 :
  x6 = x//10
  print(f'10 => {x6}')
  x -= x6*10
if x < 10 :
  x7 = x//5
  print(f'5 => {x7}')
  x -= x7*5
if x < 5  :
  x8 = x//1
  print(f'1 => {x8}')
  x -= x8*1