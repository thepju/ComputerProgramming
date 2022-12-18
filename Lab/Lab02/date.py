d = int(input("d: "))
m = int(input("m: "))
y = int(input("y: "))
if  y%100 != 0 and y%4 == 0 :
  if m < 2 : 
    print(d)
  elif m < 3 : 
    d = d+31 
    print(d)
  elif m < 4 : 
    d = d+60  
    print(d)
  elif m < 5 : 
    d = d+91  
    print(d)
  elif m < 6 : 
    d = d+121 
    print(d)
  elif m < 7 : 
    d = d+152 
    print(d)
  elif m < 8 : 
    d = d+182
    print(d)
  elif m < 9 : 
    d = d+213 
    print(d)
  elif m < 10 : 
    d = d+244 
    print(d)
  elif m < 11 : 
    d = d+274
    print(d)
  elif m < 12 : 
    d = d+305 
    print(d)
  elif m < 13 : 
    d = d+335   
    print(d)
else :
   if m < 2 : 
    print(d)
   elif m < 3 : 
     d = d+31
     print(d)
   elif m < 4 : 
     d = d+59  
     print(d)
   elif m < 5 : 
     d = d+90  
     print(d)
   elif m < 6 : 
     d = d+120 
     print(d)
   elif m < 7 : 
     d = d+151 
     print(d)
   elif m < 8 : 
     d = d+181
     print(d)
   elif m < 9 : 
     d = d+212 
     print(d)
   elif m < 10 : 
      d = d+243 
      print(d)
   elif m < 11 : 
     d = d+273
     print(d)
   elif m < 12 : 
     d = d+304 
     print(d)
   elif m < 13 : 
      d = d+334
      print(d)  