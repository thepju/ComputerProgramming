text = input('Text: ')
#text = 'abcdeabc'
sub = input('Substring: ')
#sub = 'abc'
if sub in text:
 n = text.count(sub)
 a = text.split(sub)
 if(len(a) != n):
  for i in range(len(a)):
   print(a[i],end='')
   if(i != len(a)-1):
    print(f'[{sub}]',end='')
 else:
  for i in range(len(a)):
   print(a[i],end='')
   print(f'[{sub}]',end='')
else:
 print('Not found')