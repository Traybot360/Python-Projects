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
  log.write("User " + name + " viewed books in at " + get_current_time())
  print("----------------")
  print("Available books:")
  print("----------------")
  for book in books:
    print(str(books.index(book)) + ". " + book["title"])
  print("----------------")

  # select the book from list

  # remove book from list

  # add new book to the list

  # save books into file 
  # with open('books.json', 'w') as outfile:
  #   json.dumps(books, outfile)  

  log.write("User " + name + " logged out at " + get_current_time())
