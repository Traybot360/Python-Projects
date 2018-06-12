import turtle, random

class Cell:
  def __init__(self,t):
    self.x = 0
    self.y = 0
    self.cell_size = 20
    self.t = t
  
  # draw a square
  def draw_cell(self,x,y,color):
    self.t.penup()
    self.t.goto(self.x,self.y)
    self.t.pendown()
    self.t.color(color)
    self.t.begin_fill()
    for i in range(4):
      self.t.fd(self.cell_size)
      self.t.left(90)
    self.t.end_fill()
  
  def set_cell(self, x, y):
    self.x = x
    self.y = y

class Food:
  # constructor
  def __init__(self):
    # turtle for the food
    self.t = turtle.Turtle()
    self.t.hideturtle()
    self.t.speed(0)
    self.cell = Cell(self.t)

  # create food for snake
  def create_food(self):
    multiplier = (200-self.cell.cell_size)/self.cell.cell_size
    self.cell.x = random.randint(0,multiplier)*self.cell.cell_size 
    self.cell.y = random.randint(0,multiplier)*self.cell.cell_size 
  
  # check if snake ate food
  def food_collision(self, x, y):
    if self.cell.x == x and y == self.cell.y:
      return True
    else: 
      return False

  # draw the food
  def draw_food(self):
    self.t.clear()
    self.cell.draw_cell(self.cell.x,self.cell.y, "green")
 
class Snake:
  # constructor
  def __init__(self):
    self.snake = []
    self.direction = "Right"
    self.begin_length = 5
    # turtle for snake
    self.pen = turtle.Turtle()
    self.pen.speed(0)
  
  # set snake direction
  def set_direction(self,value):
    self.direction = value

  def create_snake(self):
    for i in range(self.begin_length):
      cell = Cell(self.pen)
      cell.set_cell(i*-cell.cell_size,cell.cell_size)
      self.snake.append(cell)

  def draw_snake(self):
    self.pen.clear()
    turtle.tracer(0,0)
    for i in range(len(self.snake)):
      self.snake[i].draw_cell(self.snake[i].x,self.snake[i].y, "black")
    turtle.tracer(20,0)

  def food_collision(self, x, y):
    self.food.food_collision(x,y)

  # TODO: finish later
  def increase_speed(self):
    pass
    # self.speed += 1
    # change the frame rate using tracer

  def move_snake(self):
    n_x = self.snake[0].x
    n_y = self.snake[0].y

    # TODO: check this later
    tail = []

    if self.direction == "Right":
      n_x += self.cell_size
    if self.direction == "Left":
      n_x -= self.cell_size
    if self.direction == "Up":
      n_y += self.cell_size
    if self.direction == "Down":
      n_x -= self.cell_size

    if self.food_collision(n_x,n_y) == False:
      tail = self.snake.pop()
      # TODO: figure out why do we need this
      # tail.x = nx;
      # tail.y = ny;
    if self.food_collision(n_x,n_y) == True:
      tail = self.snake_body(n_x,n_y)
      self.increase_speed()
      self.create_food()
    # TODO: check this later
    self.snake = self.snake[1:]

  # TODO: check this later
  def collision(self):
    pass# if snake[0]

# create an instance of screen
screen = turtle.Screen()

def draw():
  # create an instance of turtle
  pen = turtle.Turtle()
  pen.hideturtle()
  # create an instance of snake
  # snake = Snake()

  # keep track of the game
  gameOver = False  
  # check user input
  screen.onkey(lambda: snake.set_direction("Up"), "Up")
  screen.onkey(lambda: snake.set_direction("Left"), "Left")
  screen.onkey(lambda: snake.set_direction("Down"), "Down")
  screen.onkey(lambda: snake.set_direction("Right"), "Right")
draw()

# testing the food class
food = Food()
food.draw_food()
food.create_food()
food.draw_food()
# testing the snake class
snake = Snake()
snake.create_snake()
snake.draw_snake()

# listen to the changes 
screen.listen()
turtle.update()