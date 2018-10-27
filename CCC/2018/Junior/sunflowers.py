matrix = [
	[3, 7, 9],
	[2, 5, 6],
	[1, 3, 4]
]

def rotate(data):
  touples = zip(*reversed(data))
  rotated = [list(item) for item in touples]
  return rotated

def check(data):
  for row in data:
    for col in row:
      if row[0] > col:
        return True
  return False

flag = True
while flag:
	matrix = rotate(matrix)
	flag = check(matrix)

for row in matrix:
	print(row)
