import time 
import json

# return current time in a string format
def get_current_time():
  minutes = str(time.localtime(time.time()).tm_min)
  seconds = str(time.localtime(time.time()).tm_sec)
  hours = str(time.localtime(time.time()).tm_hour)
  return hours+":"+minutes+":"+seconds+"\n"

with open('log.txt','a') as log:
  # get name of the reader
  name = input("Please enter your name: ")
  log.write("User " + name + " logged in at " + get_current_time())
  # read data from json file
  books_file = open('books.json')
  books = json.load(books_file)
  books_file.close()
  # Let user view the books
  log.write("User " + name + " viewed books at " + get_current_time())
  print("----------------")
  print("Available books:")
  print("----------------")
  for book in books:
    print(str(books.index(book)+1) + ". " + book["title"])
  print("----------------")

  # select the book from list
  selected = int(input("Select a book:"))
  print("----------------")
  print(books[selected-1]["text"])
  log.write("User " + name + " viewed book " + books[selected-1]["title"] + " at " + get_current_time())
  # save books into file 
  with open('books.json', 'w') as outfile:
    json.dump(books, outfile)  
  log.write("Books saved into the file at " + get_current_time())

  log.write("User " + name + " logged out at " + get_current_time())
