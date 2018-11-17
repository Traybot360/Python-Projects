# using list comprehension to save digits
digits = [int(input()) for _ in range(4)]

def check(data):
  # Telemarketer number -> True
  if data[0] in [8,9]:
    if data[1] == data[2]:
      if data[3] in [8,9]:
        return True
  
  # Other numbers -> False
  return False

# main program
if check(digits):
  print('ignore')
else:
  print('answer')
