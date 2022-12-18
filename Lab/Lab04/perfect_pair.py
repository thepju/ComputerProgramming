n = input('Input: ')
#n = '1 2 3'
n = n.split()
len_n = len(n) # 3 
ans = []

for i in range(0,len_n): #0 1 2
  for j in range(i+1,len_n): # 1 2
    ans.append(int(n[i])+int(n[j]))

ans = set(ans)
ans = list(ans)
ans.sort()
for i in range(len(ans)) :
  if ans[i] <= 100 and ans[i] >= -100 :
    print(ans[i],end=' ')

