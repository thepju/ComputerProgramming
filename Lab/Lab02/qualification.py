w = int(input('Weight: '))
h = int(input('Height: '))
bmi = w*10000 / (h*h)
if bmi < 18.6 :
  result = "You're in the underweight range."
  print(f"Your BMI is {bmi:.1f} {result}")
elif bmi < 25 :
  result = "You're in the healthy weight range."
  print(f"Your BMI is {bmi:.1f} {result}")
elif bmi < 30 :
  result = "You're in the overweight range."
  print(f"Your BMI is {bmi:.1f} {result}")
else :
  result = "You're in the obese range."
  print(f"Your BMI is {bmi:.1f} {result}")
