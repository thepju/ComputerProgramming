p = float(input('Input principal amount (P): '))
r = float(input('Input annual nominal interest rate (r): '))
n = float(input('Input # of times the interest is compounded per year (n): '))
t = float(input('Input # of years (t): '))
nt = n*t
finalAmount = p*((1+r/n)**nt)
print(f'Final amount: {finalAmount:.2f}')