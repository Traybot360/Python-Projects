answer1,answer2,answer3=[int(input()) for _ in range(3)]
if answer1 + answer2 + answer3==180:
  if answer1==answer2==answer3:
    print("Equilateral")
  elif answer1 != answer2 and answer2 != answer3 and answer1 != answer3:
    print("Scalene")
  else:
    print("Isosceles")
else:
  print("Error")

