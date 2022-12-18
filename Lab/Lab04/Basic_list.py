a = -1
count = 0
listP = []
res = 0
res_max = -9999999
res_min = -res_max
sum = 0

while a != 0 :
  p = int(input('Enter a positive number: '))
  if p > 0 :
    count += 1 
    listP.append(p)
    if count == 5 :
      for i in range(5):
        sum += listP[i]
        res = listP[i]
        if res > res_max :
          res_max = res
        if res < res_min :
          res_min = res
      listP = sorted(listP)
      med = int(listP[2]) 
        
      print(f'sum: {sum}')
      print(f'min: {res_min}')
      print(f'max: {res_max}')
      print(f'med: {med}')
      a = 0
