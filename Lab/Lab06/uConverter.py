def anytoten(a,n):
 p = int(a,n)
 return p

def tentoany(a,m):
 poop = ''
 while(a>0):
   k = (a%m)
   poop = inttostr(k) + poop
   a = a//m 
 return poop
  
def inttostr(n):
 if(n == 10):
  return 'A'
 elif(n == 11):
  return 'B'
 elif(n == 12):
  return 'C'
 elif(n == 13):
  return 'D'
 elif(n == 14):
  return 'E'
 elif(n == 15):
  return 'F'
 elif(n == 16):
  return 'G'
 elif(n == 17):
  return 'H'
 elif(n == 18):
  return 'I'
 elif(n == 19):
  return 'J'
 elif(n == 20):
  return 'K'
 elif(n == 21):
  return 'L'
 elif(n == 22):
  return 'M'
 elif(n == 23):
  return 'N'
 elif(n == 24):
  return 'O'
 elif(n == 25):
  return 'P'
 elif(n == 26):
  return 'Q'
 elif(n == 27):
  return 'R'
 elif(n == 28):
  return 'S'
 elif(n == 29):
  return 'T'
 elif(n == 30):
  return 'U'
 elif(n < 10):
  return '%d'%n

#main
n = int(input(''))
m = int(input(''))
num = input('')
num = anytoten(num,n)
num = tentoany(num,m)
print(num)