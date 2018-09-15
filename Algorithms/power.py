def power(base, n):
  if n == 0:
    return 1
  if n > 0:
    return base * power(base, n - 1)
