
lines = int(input())
matrix = []
for line in range(lines):
  matrix.append(input().split())

# test case 1
# matrix = [
#   [1,3],
#   [2,9]
# ]

# test case 2
# matrix = [
#   [4,3,1],
#   [6,5,2],
#   [9,7,3]
# ]

# test case 3
# matrix = [
# 	[3, 7, 9],
# 	[2, 5, 6],
# 	[1, 3, 4]
# ]

# print the matrix
def display(data):
  for row in data:  
    print(' '.join(row))

# 90 degrees matrix rotation
def rotate(data):
  touples = zip(*reversed(data))
  rotated = [list(item) for item in touples]
  return rotated

# True -> valid
# False -> not valid
def check(data):
  # every element in the row must be greater than previous
  for sublist in data:
    if sublist != sorted(sublist):
      return False

  # every first element in column must be greater than previous column
  sublist = []
  for row in data:
    sublist.append(row[0])
  
  if sublist != sorted(sublist):
    return False

  # list is valid
  return True

while not check(matrix):
  matrix = rotate(matrix)
display(matrix)
