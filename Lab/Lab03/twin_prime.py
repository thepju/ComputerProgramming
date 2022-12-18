y = True
n = int(input('N: '))

def isPrime(n):
  if n < 1 :
    return False
  for i in range(2,n) :
    if n%i == 0 :
      return False
  return True 


for i in range(n,n+1000) :
  if isPrime(i) == True :
    if isPrime(i+2) == True :
      print(f"({i}, {i+2})")
      break
    
  