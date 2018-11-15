weight=float(input())
height=float(input())
d=height*height
bmi=weight/d
if bmi<18.5:
  print("Underweight")
elif bmi>18.5 and bmi<25.0:
  print("Normal weight")
else:
  print("Overweight")
