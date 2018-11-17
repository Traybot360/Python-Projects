def lst_int(lst):
  for i in range(len(lst)):
    lst[i] = int(lst[i])

a= input().split()
b = input().split()
charge = int(input())
lst_int(a)
lst_int(b)

if(abs( abs(a[0] - b[0]) + abs(a[1] - b[1])  ) <= charge):
  if(abs( abs(a[0] - b[0]) + abs(a[1] - b[1])  )%2 == 0 and charge%2 ==0):
    print("Y")
  elif(abs( abs(a[0] - b[0]) + abs(a[1] - b[1])  )%2 != 0 and charge%2 !=0):
    print("Y")
  else: print("N")
else: print("N")
