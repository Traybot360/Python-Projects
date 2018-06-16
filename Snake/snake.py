import turtle, random

class Cell:
  def __init__(self,t):
    # set initial position
    self.x = 0
    self.y = 0
    # set initial size of a cell
    self.cell_size = 10
    # set the turtle
    self.t = t
  
  # draw a square at (x,y) of color
  def draw_cell(self,x,y,color):
    # update cell information
    self.set_cell(x,y)
    # move to (x,y)
    self.t.penup()
    self.t.goto(self.x,self.y)
    self.t.pendown()
    # set the color
    self.t.color(color)
    # draw the square
    self.t.begin_fill()
    for i in range(4):
      self.t.fd(self.cell_size)
      self.t.left(90)
    self.t.end_fill()
  
  # update coordinates of the cell
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

    # food colors
    self.colors = ["red","green","yellow","blue","magenta", "cyan"]

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
    self.cell.draw_cell(self.cell.x,self.cell.y, random.choice(self.colors))
    turtle.tracer(20,0) 

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
    # if game is over this will be True
    self.game_over = False

  # set snake direction
  def set_direction(self,value):
    if self.direction == "Right" and (value == "Up" or value == "Down"):
      self.direction = value
    if self.direction == "Left" and (value == "Up" or value == "Down"):
      self.direction = value
    if self.direction == "Up" and (value == "Left" or value == "Right"):
      self.direction = value
    if self.direction == "Down" and (value == "Left" or value == "Right"):
      self.direction = value
    
    self.check_snake()

  # check snake collision with food
  def food_collision(self, x, y):
    return self.food.food_collision(x,y)

  # check snake collision with itself
  def self_collision(self):
    collision = False
    for cell in range(1,len(self.snake)):
      if self.snake[0].x == self.snake[cell].x and self.snake[0].y == self.snake[cell].y:
        collision = True
    return collision

  # check snake collision with border
  def border_collision(self):
    if self.snake[0].x > 200 or self.snake[0].x < -200:
      return True
    elif self.snake[0].y > 200 or self.snake[0].y < -200:
      return True
    else:
      return False
    
  # end the game
  def game_is_over(self):
    if self.game_over:
      self.pen.clear()
      self.pen.write("Game over")
      return True
    else:
      return False

  # move the snake faster as it goes
  def increase_speed(self):
    if self.speed > 100:
      self.speed -= 10

  # create the snake at (0,0)
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

  # this function will move snake
  def move_snake(self):
    old_x = self.snake[0].x
    old_y = self.snake[0].y
    
    for square in range(len(self.snake)):
      if square == 0: 
        old_x = self.snake[square].x
        if self.direction == "Right":  
          self.snake[square].x += self.snake[0].cell_size
        elif self.direction == "Left":
          self.snake[square].x -= self.snake[0].cell_size
        elif self.direction == "Up":
          self.snake[square].y += self.snake[0].cell_size
        elif self.direction == "Down":
          self.snake[square].y -= self.snake[0].cell_size
      else:
        old_x, self.snake[square].x = self.snake[square].x, old_x
        old_y, self.snake[square].y = self.snake[square].y, old_y

  # check if food overlaps with the snake
  def food_overlap(self):
    for cell in self.snake:
      if self.food.cell.x == cell.x:
        self.food.create_food()
        return True
      
    return False

  def check_food_collision(self,x,y):
    # food_collision
    if self.food_collision(x,y) == True:
      # add square to the snake
      cell = Cell(self.pen)
      cell.set_cell(x,y)
      self.snake.append(cell)
      # make snake move faster
      self.increase_speed()
      # make more food
      if self.food_overlap():
        self.food.create_food()
      self.food.draw_food()
      # increase the length of the snake
      self.begin_length += 1
      return True
    elif self.food_collision(x,y) == False:
      return False
  
  # this funciton will check snake collisions and move
  def check_snake(self):
    self.pen.clear() 
    if not self.game_over:    
      self.move_snake()   

      # check if snake ate more food
      if self.check_food_collision(self.snake[0].x,self.snake[0].y):
        print("Score = " + str(self.begin_length - 5))
      # self_collision check
      elif self.self_collision() == True:
        self.game_over = True
      # border_collision check
      elif self.border_collision() == True:
        self.game_over = True

      self.draw_snake()    
      
    # game over screen
    if self.game_over:
      self.game_is_over()

class Game:
  def __init__(self):     
    # create an instance of screen
    self.screen = turtle.Screen()
    
    # create an instance of turtle
    self.pen = turtle.Turtle()
    self.pen.hideturtle()
    # create an instance of snake
    self.snake = Snake()
    
    # keep track of the game
    self.game_over = False  

    # check user input
    self.screen.onkey(lambda: self.snake.set_direction("Up"), "Up")
    self.screen.onkey(lambda: self.snake.set_direction("Left"), "Left")
    self.screen.onkey(lambda: self.snake.set_direction("Down"), "Down")
    self.screen.onkey(lambda: self.snake.set_direction("Right"), "Right")
    
    self.screen.listen()

  def draw_border(self):
    self.pen.penup()
    self.pen.goto(-210,210)
    self.pen.pendown()
    for side in range(4):
      self.pen.fd(420)
      self.pen.right(90)

game = Game()
game.draw_border()

# listen to the changes 
turtle.update()
turtle.Screen().mainloop()