import json
def readfile(filename):
  with open(filename) as f:
    s = f.read()
  s = s.split('\n')
  tmp =[]
  for i in range(len(s)):
    tmp.append(json.loads(s[i]))    
  #print(type(tmp[0]))
  return tmp

def q1(ss):
  print(len(ss))

def q2(ss):
  tmp,ans = [],0
  for i in range(len(ss)):
    res = ss[i]['reviewerID']
    if res not in tmp:
      tmp.append(res)
      ans +=1
  print(ans)

def q3(ss):
  tmp,ans = [],0
  for i in range(len(ss)):
    res = ss[i]['productID']
    if res not in tmp:
      tmp.append(res)
      ans +=1
  print(ans)

def q4(ss):
  tmp,ans = [],0
  for i in range(len(ss)):
    res = ss[i]['category'].split('>')
    if res[0] not in tmp:
      tmp.append(res[0])
      ans += 1
  print(ans)

def q5(ss):
  tmp,ans = [],0
  for i in range(len(ss)):
    res = ss[i]['category'].split('>')
    if res[1] not in tmp:
      tmp.append(res[1])
      ans += 1
  print(ans)

def q6(ss):
  ans,tmp = [],[]
  for i in range(len(ss)):
    res = ss[i]['reviewerID']
    if res not in ans:
      ans.append(res)
      tmp.append(1)
    else:
      a = ans.index(res)
      tmp[a] += 1
  b = tmp.index(max(tmp))
  print(ans[b])

def q7(ss):
  ans,tmp,res = [],[],[]
  for i in range(len(ss)):
    if ss[i]['productName'] not in ans:
      ans.append(ss[i]['productName'])
      tmp.append(1)
      res.append(float(ss[i]['overall']))
    else:
      a = ans.index(ss[i]['productName'])
      tmp[a] += 1
      res[a] += float(ss[i]['overall'])
  pp = []
  for i in range(len(ans)):
    pp.append(res[i]/(tmp[i]))
  maxans,maxtmp = [],[]
  res = max(pp)
  for i in range(len(ans)):
    if pp[i] == res:
      maxans.append(ans[i])
      maxtmp.append(tmp[i])
  b = maxtmp.index(max(maxtmp))
  print(maxans[b])

def q8(ss):
  ans,tmp,res = [],[],[]
  for i in range(len(ss)):
    if ss[i]['productName'] not in ans:
      ans.append(ss[i]['productName'])
      tmp.append(1)
      res.append(len(ss[i]['reviewText'].split()))
    else:
      b = ans.index(ss[i]['productName'])
      tmp[b] += 1
      res[b] += len(ss[i]['reviewText'].split())
  pp = []
  for i in range(len(ans)):
    pp.append(res[i]/tmp[i])
  c = pp.index(max(pp))
  print(ans[c])

tx = input('file name: ')
#tx = 'amazon1.json'
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