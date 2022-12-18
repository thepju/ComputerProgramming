a= input()
b = a.split()
len_b = len(b)
count = int(b[0])+1
for i in range(1, len_b  , count):
      c = int(b[i])
      print( chr(c) ,end='' )