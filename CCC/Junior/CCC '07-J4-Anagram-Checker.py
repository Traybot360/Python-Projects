def checker(first,second):

  for i in range(len(first)):

    if(first.count(first[i]) != second.count(first[i])):
      return "Is not an anagram."
      #if it doesn't have the same amount of a letter than its not an anagram
  return "Is an anagram."


first = list(input())
second = list(input())

#get the input as a list
[first.remove(" ") for i in range(first.count(" "))]
[second.remove(" ") for i in range(second.count(" "))]
#remove the spaces from the list

print(checker(first,second))
