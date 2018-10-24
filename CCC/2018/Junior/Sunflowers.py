matrix = [
	[3, 7, 9],
	[2, 5, 6],
	[1, 3, 4]
]

def rotate(data):
	return list((zip(*reversed(data))))

def check(data):
	for row in data:
		for col in row:
			if row[0] > col:
				return True

flag = True
while flag:
	matrix = rotate(matrix)
	flag = check(matrix)

for row in rotate(matrix):
	print(row)
