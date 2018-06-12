import turtle, random

# create an instance of screen
screen = turtle.Screen()

class Cell:
  def __init__(self,t):
    self.x = 0
    self.y = 0
    self.cell_size = 10
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
    turtle.tracer(0,0)
    self.cell.draw_cell(self.cell.x,self.cell.y, "green")
    turtle.tracer(20,10)
 
class Snake:
  # constructor
  def __init__(self):
    self.snake = []
    self.direction = "Right"
    self.begin_length = 5

    self.food = Food()
    self.food.draw_food()
    # turtle for snake
    self.pen = turtle.Turtle()
    self.pen.speed(0)
    self.create_snake()
  
  # set snake direction
  def set_direction(self,value):
    self.direction = value
    self.move_snake()

  def food_collision(self, x, y):
    return self.food.food_collision(x,y)

# TODO: change return 
  def self_collision(self, x, y):
    return False
# TODO: change return 
  def border_collision(self, x, y):
    return False

# TODO: change the frame rate using tracer
  def increase_speed(self):
    pass
    # self.speed += 1

  def create_snake(self):
    for i in range(self.begin_length):
      cell = Cell(self.pen)
      cell.set_cell(i*-cell.cell_size,cell.cell_size)
      self.snake.append(cell)
    self.draw_snake()

  def draw_snake(self):
    self.pen.clear()
    turtle.tracer(0,0)
    for i in range(len(self.snake)):
      self.snake[i].draw_cell(self.snake[i].x,self.snake[i].y, "black")
    turtle.tracer(20,400)

  def move_snake(self):
    self.pen.clear()
    print(self.direction)
    if self.direction == "Right":
      for square in range(len(self.snake)):
        self.snake[square].x += self.snake[0].cell_size
    if self.direction == "Left":
      for square in range(len(self.snake)):
        self.snake[square].x -= self.snake[0].cell_size
    if self.direction == "Up":
      for square in range(len(self.snake)):
        self.snake[square].y += self.snake[0].cell_size
    if self.direction == "Down":
      for square in range(len(self.snake)):
        self.snake[square].y -= self.snake[0].cell_size
    
    self.draw_snake()

    # new position of the snake
    new_x = self.snake[0].x
    new_y = self.snake[0].y    

    # food_collision
    if self.food_collision(new_x,new_y) == True:
      # add square to the snake
      cell = Cell(self.pen)
      cell.set_cell(new_x,new_y)
      self.snake.append(cell)
      # make snake move faster
      self.increase_speed()
      # make more food
      self.food.create_food()
      self.food.draw_food()

    # food_collision check
    if self.food_collision(new_x,new_y) == False:
      # self_collision check
      if self.self_collision(new_x,new_y) == False:
        # border_collision check
        if self.border_collision(new_x,new_y) == False:
          # no collision, move snake forward
          # self.move_snake()
          pass
        else:
          # border_collision, game over
          self.game_over()
      else:
        # self_collision, game over
        self.game_over()
  
def draw():
  # create an instance of turtle
  pen = turtle.Turtle()
  pen.hideturtle()
  # create an instance of snake
  snake = Snake()
  # check user input
  screen.onkey(lambda: snake.set_direction("Up"), "Up")
  screen.onkey(lambda: snake.set_direction("Left"), "Left")
  screen.onkey(lambda: snake.set_direction("Down"), "Down")
  screen.onkey(lambda: snake.set_direction("Right"), "Right")

  # keep track of the game
  game_over = False  

# TODO: check why onkey doesn't work with while/recursion
  # while not game_over:
  #   snake.move_snake()

draw()

# listen to the changes 
screen.listen()
turtle.update()
screen.mainloop()
