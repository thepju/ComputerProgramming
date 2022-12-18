E_times = int(input('Estimated time : '))
cw = (E_times) // 8
hrC =(E_times * 5)/2
mod = (E_times * 5) % 2
if mod != 0 :
  hrC += 1 - (mod/2)
else :
  hrC += 0 
n1 = 0
n2 = 0
n3 = 0
for i in range (1,cw + 1) : 
  print(f'Week{i}')
  Pt = int(input('Physical therapy : '))
  n1 += Pt
  Wt = int(input('Weight training : '))
  n2 += Wt
  Ft = int(input('Fitness training : '))
  n3 += Ft
if n1 >= hrC  :
  if n2 >= hrC :
    if n3 >= hrC :
      print('Buzzy has recovered in time.')
    else : 
      print('Buzzy has not recovered in time.')
  else :
    print('Buzzy has not recovered in time.')
else :
  print('Buzzy has not recovered in time.')