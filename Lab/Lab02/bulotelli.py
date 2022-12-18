injured = input('Is Bulotelli injured?(y/n) ')
if injured == 'n' :
  late = input('Is Bulotelli late for the training?(y/n) ')
  if late == 'n' :
    print('Starter')
  else :
    perfom = input('Did Bulotelli perform well in training?(y/n) ')
    if perfom == 'y' :
      print('Substitute')
    else : 
      print('Not selected')
else : 
  print('Not available')