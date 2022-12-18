m = int(input('How long have Buzz played ?: '))
hr = m//60
m2 = m%60
if m2 > 20 :
  new_hr = hr + 1
  if new_hr < 2 :
    print(f'Total price is {new_hr*900} baht.')
  elif new_hr < 4 :
    print(f'Total price is {new_hr*810} baht.')
  elif new_hr < 5 :
    print(f'Total price is {new_hr*720} baht.')
  else :
    print(f'Total price is {new_hr*630} baht.')
else : 
  new_hr = hr
  if new_hr < 2 :
    print(f'Total price is {new_hr*900} baht.')
  elif new_hr < 4 :
    print(f'Total price is {new_hr*810} baht.')
  elif new_hr < 5 :
    print(f'Total price is {new_hr*720} baht.')
  else :
    print(f'Total price is {new_hr*630} baht.')
    
