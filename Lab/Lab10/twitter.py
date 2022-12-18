import json
def readfile(filename):
  with open(filename) as f:
    s = f.read()
  ss = json.loads(s)
  return ss

def q1(ss):
  print(len(ss))

def q2(ss):
  tmp,ans = [],0
  for i in range(len(ss)):
    res = ss[i]['author']
    if res not in tmp:
      tmp.append(res)
      ans +=1
  print(ans)

def q3(ss):
  ans,tmp = [],[]
  for i in range(len(ss)):
    res = ss[i]['author']
    if res not in ans:
      ans.append(res)
      tmp.append(1)
    else:
      b = ans.index(res)
      tmp[b] += 1
  for i in range(len(ans)):
    if tmp[i] == max(tmp):
      print(ans[i])

def q4(ss):
  tmp = []
  for i in range(len(ss)):
    res = ss[i]['topic']
    if res not in tmp:
      tmp.append(res)
  print(len(tmp))

def q5(ss):
  ans = 0
  for i in range(len(ss)):
    res = ss[i]['topic_priority']
    if res == 'ALERT':
      ans += 1
  print(ans)

def q6(ss):
  ans = 0
  for i in range(len(ss)):
    res = ss[i]['topic_priority']
    if res == 'UNIMPORTANT':
      ans += 1
  print(ans)

def q7(ss):
  res = False
  for i in range(len(ss)):
    if ss[i]['language'] != 'EN':
      res = True
      break
  print(res)

def q8(ss):
  tmp = []
  for i in range(len(ss)):
    tmp.append(len(ss[i]['text'].split()))
  print(max(tmp))

tx = input('File name: ')
#tx = 'twitter.json'
final = readfile(tx)
n = int(input('input: '))
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
elif n == 6:
  q6(final)
elif n == 7:
  q7(final)
elif n == 8:
  q8(final)