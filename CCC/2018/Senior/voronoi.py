times = int(input())
nums = [int(input()) for i in range(times)]
nums = list(reversed(sorted(nums)))
smallest = ((nums[0]-nums[1])/2) + ((nums[1]-nums[2])/2)

for i in range(1,len(nums)-1):
  if( (((nums[i-1]-nums[i])/2) + ((nums[i]-nums[i+1]))/2) < smallest ):
    smallest = (((nums[i-1]-nums[i])/2) + ((nums[i]-nums[i+1]))/2)
print(smallest)

'''
5
16
0
10
4
15
'''

