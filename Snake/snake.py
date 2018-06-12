import turtle, random

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
    # create food
    self.food = Food()
    self.food.draw_food()
    # turtle for snake
    self.pen = turtle.Turtle()
    self.pen.hideturtle()
    self.pen.speed(0)
    # create snake
    self.speed = 400
    self.create_snake()
  
  # set snake direction
  def set_direction(self,value):
    self.direction = value
    self.move_snake()

  def food_collision(self, x, y):
    return self.food.food_collision(x,y)

  def self_collision(self):
    collision = False
    for cell in range(1,len(self.snake)):
      if self.snake[0].x == self.snake[cell].x and self.snake[0].y == self.snake[cell].y:
        collision = True
    return collision
    # return False

  def border_collision(self):
    if self.snake[0].x > 200 or self.snake[0].x < -200:
      return True
    elif self.snake[0].y > 200 or self.snake[0].y < -200:
      return True
    else:
      return False
    
  # TODO: move to the game class
  def game_over(self):
    game_over = True
    self.pen.write("Game over")

  def increase_speed(self):
    if self.speed > 100:
      self.speed -= 10

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
    turtle.tracer(20,self.speed)

  def move_snake(self):
    self.pen.clear()
    
    if self.direction == "Right":
      old_x = self.snake[0].x
      old_y = self.snake[0].y
      for square in range(len(self.snake)):
        if square == 0: 
          old_x = self.snake[square].x
          self.snake[square].x += self.snake[0].cell_size
        else:
          old_x, self.snake[square].x = self.snake[square].x, old_x
          old_y, self.snake[square].y = self.snake[square].y, old_y
          
    if self.direction == "Left":
      old_x = self.snake[0].x
      old_y = self.snake[0].y
      for square in range(len(self.snake)):
        if square == 0: 
          self.snake[square].x -= self.snake[0].cell_size
        else:
          old_x, self.snake[square].x = self.snake[square].x, old_x
          old_y, self.snake[square].y = self.snake[square].y, old_y

    if self.direction == "Up":
      old_x = self.snake[0].x
      old_y = self.snake[0].y
      for square in range(len(self.snake)):
        if square == 0: 
          self.snake[square].y += self.snake[0].cell_size
        else:
          old_x, self.snake[square].x = self.snake[square].x, old_x
          old_y, self.snake[square].y = self.snake[square].y, old_y

    if self.direction == "Down":
      old_x = self.snake[0].x
      old_y = self.snake[0].y
      for square in range(len(self.snake)):
        if square == 0: 
          self.snake[square].y -= self.snake[0].cell_size
        else:
          old_x, self.snake[square].x = self.snake[square].x, old_x
          old_y, self.snake[square].y = self.snake[square].y, old_y
    
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
      self.draw_snake()

    # food_collision check
    if self.food_collision(new_x,new_y) == False:
      # self_collision check
      if self.self_collision() == False:
        # border_collision check
        if self.border_collision() == False:
          # no collision, move snake forward
          self.draw_snake()
          # self.move_snake()
        else:
          # border_collision, game over
          self.game_over()
      else:
        # self_collision, game over
        self.game_over()
class Game:
  def __init__(self):    
    
    # create an instance of screen
    self.screen = turtle.Screen()
    
    # create an instance of turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    # create an instance of snake
    self.snake = Snake()

    # keep track of the game
    self.game_over = False  

    # TODO: check why onkey doesn't work with while/recursion
    # while not game_over:
    #   snake.move_snake()

    # check user input
    self.screen.onkey(lambda: self.snake.set_direction("Up"), "Up")
    self.screen.onkey(lambda: self.snake.set_direction("Left"), "Left")
    self.screen.onkey(lambda: self.snake.set_direction("Down"), "Down")
    self.screen.onkey(lambda: self.snake.set_direction("Right"), "Right")
    
    self.screen.listen()

# listen to the changes 
turtle.update()