# total amout of parking spots
spots = int(input())

# spaces occupied in day 1
day1 = list(input())

# spaces occupied in day 2
day2 = list(input())

# variable to count same spots 
counter = 0

# counting same spots
for spot in range(spots):
  if day1[spot] == day2[spot]:
    if day1[spot] != '.':
      counter+=1

# print result
print(str(counter))
