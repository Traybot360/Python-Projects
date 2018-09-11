def search(data, element):
  """Linear search for element in a list.

    Parameters
    ----------
    data : list with elements
    element : element to look for
    
    Returns
    -------
    index : position of the element if it is present, otherwise -1
  """
  for index in range(len(data)):
    if data[index] == element:
      return index
  return -1

if __name__ == "__main__":
  arr = [0,10,20,30,40,50,60,70,80,90]
  print(search(arr, 8))
  print(search(arr,70))

# Output:
# -1
# 7
