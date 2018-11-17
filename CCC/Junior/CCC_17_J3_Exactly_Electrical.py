curr = input().split()
dest = input().split()
charge = int(input())
x1 = int(curr[0])
y1 = int(curr[1])
x2 = int(dest[0])
y2 = int(dest[1])

if(charge>abs(abs(x1-x2)-abs(y1-y2))):
  if(abs(abs(x1-x2)-abs(y1-y2))%2==0 and charge%2==0):
    print("Y")
  elif(abs(abs(x1-x2)-abs(y1-y2))%2!=0 and charge%2!=0):
    print("Y")
  else: print("N")
else: print("N")                                 
