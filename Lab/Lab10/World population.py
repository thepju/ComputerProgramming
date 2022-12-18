import json
def readfile(filename):
  with open(filename) as f:
    s = f.read()
  ss = json.loads(s)
  #print(type(ss[0]))
  return ss

def q1(ss):
  print(len(ss))

def q2(ss):  
  tmp = 0
  for i in range(len(ss)):
    tmp += int(ss[i]['population'])
  print(tmp)

def q3(ss):
  a1,a2 = 0,0
  for i in range(len(ss)):
    res = ss[i]['country']
    if res[0] == 'C':
      a1 += 1
    if len(res) >5:
      a2 += 1
  print(a1)
  print(a2)

def q4(ss):
  a1,a2,a3 = 0,0,0
  for i in range(len(ss)):
    if int(ss[i]['population']) >500000000:
      a1 += 1
    if 250000000 < int(ss[i]['population']) < 750000000:
      a2 += 1
    if int(ss[i]['population']) < 10000000:
      a3 += 1
  print(a1)
  print(a2)
  print(a3)

def q5(ss):
  a1,a2 = 0,0
  for i in range(20):
    a1 += float(ss[i]['World'])
  print(f'{a1*100:.2f}')
  for i in range(49,150):
    a2 += float(ss[i]['World'])
  print(f'{a2*100:.2f}')

tx = input('File Name: ')
#tx = 'worldpopulation.json'
final = readfile(tx)
n = int(input('Input : '))
if n == 1:
  q1(final)
elif n == 2:
  q2(final)
elif n == 3:
  q3(final)
elif n == 4:
  q4(final)
elif n == 5:
  q5(final)