import turtle, random

class Snake:
  # constructor
  def __init__(self):
    self.snake = []
    self.cell_size = 20
    self.direction = "Right"
    self.beginLength = 5
    self.speed = 10
    self.food_x = 0
    self.food_y = 0
  
  def snake_body(self,x,y):
    self.x = x
    self.y = y
  
  def create_snake(self):
    for i in range(self.beginLength):
      self.snake.append(snake_body(i*-self.cell_size,self.cell_size))
  
  def create_food(self):
    multiplier = (400-self.cell_size)/self.cell_size
    self.food_x = random.randint(0,multiplier)*self.cell_size 
    self.food_y = random.randint(0,multiplier)*self.cell_size 

  # TODO: finish later
  def draw_food(self):
    # set color to green
    # draw square
    pass
  
  def food_collision(self, x, y):
    if x == self.food_x and y == self.food_y:
      return True
    else: 
      return False

  # TODO: finish later
  def increase_speed(self):
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

  def collision(self):
    if snake[0]

  # set snake direction
  def set_direction(self,value):
    self.direction = value
    pen.clear()
    pen.write(self.direction)


# keep track of the game
gameOver = False
# create an instance of turtle
pen = turtle.Turtle()
pen.hideturtle()
# create an instance of turtle
screen = turtle.Screen()
# create an instance of snake
snake = Snake()


# check user input
screen.onkey(lambda: snake.set_direction("Up"), "Up")
screen.onkey(lambda: snake.set_direction("Left"), "Left")
screen.onkey(lambda: snake.set_direction("Down"), "Down")
screen.onkey(lambda: snake.set_direction("Right"), "Right")

# listen to the changes 
screen.listen()
