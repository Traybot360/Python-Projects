# b is base
# n is exponent
def power(b,n):
  print("runtime")
  if n == 0:
    return 1
  if n % 2 == 0:
    return power(b * b, n / 2)
  else:
    return b * power(b * b, (n - 1) / 2)
  
def power2(b,n):
  print("runtime")
  if n == 0:
    return 1
  else:
    return b*power2(b,n-1)

print(power(5,7))
print()
print(power2(5,7))
