from flask import Flask, render_template

app = Flask(__name__)

# get distances from user
# distances = input().split()
# fixed to render into table
distances = [3, 10, 12, 5]
letters = ['A','B','C','D','E']

# calculate the distances
def distance(x,y):

  # distance between same cities
  if x == y:
    return 0
  
  # distance from 1 to 5 is same as distance from 5 to 1
  if y < x:
    x,y=y,x
    return distance(x,y)

  # base cases
  if x == 1 and y == 2:
    return distances[0]
  if x == 2 and y == 3:
    return distances[1]
  if x == 3 and y == 4:
    return distances[2]
  if x == 4 and y == 5:
    return distances[3]

  # recursion case
  return distance(x, y-1) + distance(y-1, y)    

# fill the data
data = [
  [
    distance(x,y) for y in range(1,len(distances)+2)
  ] 
  for x in range(1,len(distances)+2)
]

@app.route("/")
def render_table():
  return render_template("table.html", data=data, letters=letters)

if __name__ == '__main__':
