numbers = [x for x in range(1000000)]

def binary(data, el):
  if len(data) == 0:
    return False
  else:
    mid = len(data)//2
    if data[mid] == el:
      return True
    else:
      if el < data[mid]:
        return binary(data[:mid],el)
      else:
	      return binary(data[mid+1:],el)
	
print(binary(numbers, -1))
print(binary(numbers, 999999))
