c = 0
sd1 = 0
sum_sd = 0
y = []
n = ['a','b','c','d','e']
for i in n : 
  i = int(input(f'Input {i}: '))
  c += i 
  y.append(i)
mean = c / 5 
for j in y :
    sd1 = (mean-j)**2
    sum_sd += sd1   
print(f'mean: {mean:.3f}') 
print(f'sd: {(sum_sd / 5 )**(1/2):.3f}')  