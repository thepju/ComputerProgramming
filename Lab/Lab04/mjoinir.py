gold = float(input('Input Gold: '))
#gold = 300
gold = gold/1 
gold_level = int(gold//1000) 
if gold_level < 1 :
  print('Not enough gold.')
else :
  print(' ',end='')
  print('o'*(3*gold_level+4))
  for i in range(2*gold_level+1):  
    print('o'*(3*gold_level+6))     #ความกว้างของค้อน
  print(' ',end='')
  print('o'*(3*gold_level+4))
  for i in range(gold_level+2):
    for i in range( (((3*gold_level+6)-gold_level) //2)) :
      print(' ',end='')
    print('o'*gold_level,end='')
    for i in range( (((3*gold_level+6)-gold_level) //2)) :
      print(' ',end='')
    print()
  for i in range(gold_level) :
    for i in range( ((3*gold_level+6)-(gold_level+2) ) //2 ):
      print(' ',end='')
    print('o'*(gold_level+2))
  for i in range( (((3*gold_level+6)-gold_level) //2)) :
      print(' ',end='')
  print('o'*gold_level,end='')

