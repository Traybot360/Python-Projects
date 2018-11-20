def devisors(num):
  output = [i for i in range(1,num-1) if(num/i).is_integer()]
  return output
def type_say(num):
  num_sum = sum(devisors(num))
  if(num_sum== num):
    return str(num) + " is a perfect number."
  elif(num_sum < num):
    return str(num) + " is a deficient number."
  elif(num_sum > num):
    return str(num) + " is an abundant number."

times = int(input())
nums = [int(input()) for i in range(times)]

[print(type_say(i)) for i in nums]
