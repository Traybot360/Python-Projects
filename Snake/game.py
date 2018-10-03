import turtle
from snake import Snake
turtle.tracer(0,0)
screen = turtle.Screen()
class Game:
  """This is a controller for Snake game"""
  def __init__(self, screen):     
    """Constructor for Game class. This funcion is called upon 
    initialization. It saves a Screen object as a class member,
    creates snake_pen, food_pen, score_pen, border_pen turtles,
    binds keyboard keys, and listens for user input.
    Parameters
    ----------
    screen : turtle.Screen Screen object of the turtle library
    Returns
    -------
    None
    """
    # create an instance of screen
    self.screen = screen    
    # turtle for snake
    self.snake_pen = turtle.Turtle(visible=False)
    # turtle for food
    self.food_pen = turtle.Turtle(visible=False)
    # turtle for score 
    self.score_pen = turtle.Turtle(visible=False)    
    # turtle for borders and information
    self.border_pen = turtle.Turtle(visible=False)
    # check user input
    self.screen.onkey(lambda: self.snake.set_direction("u"), "Up")
    self.screen.onkey(lambda: self.snake.set_direction("l"), "Left")
    self.screen.onkey(lambda: self.snake.set_direction("d"), "Down")
    self.screen.onkey(lambda: self.snake.set_direction("r"), "Right")
    self.screen.onkey(lambda: self.play(), "space")
    self.screen.onkey(lambda: self.exit_game(), "Escape")
    self.screen.listen()
 
  def exit_game(self):
    """This function will terminate the program when it is called.
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    quit()
  def play(self):
    """This function will start the game and reset all the values.
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    self.game_over = False
    # clear the screen
    self.border_pen.clear()
    self.food_pen.clear()
    self.score_pen.clear()
    self.snake_pen.clear()
    # create an instance of snake
    self.snake = Snake(self.snake_pen, self.food_pen)
    self.snake.length = 5
    self.snake.speed = 1
    self.snake.food.draw_food()
    self.draw_border()
    self.draw_information()
    self.check_snake()

  def draw_score(self):
    """This function will draw game score.
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    self.score_pen.penup()
    self.score_pen.goto(0,250)
    self.score_pen.write("Score : " + str(self.snake.length - 5), align="center", font=("Arial", 20, "normal"))
    
  def draw_information(self):
    """This function will draw game information.
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    self.border_pen.penup()
    self.border_pen.goto(0,-250)
    self.border_pen.write("Press Space to restart", align="center", font=("Arial", 18, "normal"))
    self.border_pen.goto(0,-270)
    self.border_pen.write("Press Esc to exit", align="center", font=("Arial", 18, "normal"))
    self.border_pen.pendown()
  
  def draw_border(self):
    """This function will draw game border.
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    self.border_pen.penup()
    self.border_pen.goto(-210,210)
    self.border_pen.pendown()
    for _ in range(4):
      self.border_pen.fd(420)
      self.border_pen.right(90)
    
  # this funciton will check snake collisions and move
  def check_snake(self):
    """This function will check snake state. If game is over, snake
    game will show "Game Over" message. Otherwise, it will keep
    running as usual snake game.
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    if not self.game_over:  
      self.snake_pen.clear()
      self.snake.draw_snake()         
      self.score_pen.clear() 
      self.draw_score()
            
      self.snake.move_snake()
      self.screen.ontimer(lambda: self.check_snake(), 100-self.snake.speed*2)
            
      # check if snake ate more food
      if self.snake.food_collision(self.snake.snake[0].x, self.snake.snake[0].y):
        self.food_pen.clear() 
        self.snake.food.create_food()
        self.snake.food.draw_food()
      # self_collision check
      elif self.snake.self_collision():
        print("self collision")
        self.game_over = True
      # border_collision check
      elif self.snake.border_collision():
        print("border collision")
        self.game_over = True
     
    # game over message
    if self.game_over:
      self.food_pen.clear() 
      self.snake_pen.clear() 
      self.snake_pen.penup()
      self.snake_pen.goto(0,0)
      self.snake_pen.write("Game over",align="center",font=("Arial", 20, "normal"))
      self.game_over = True
        
game = Game(screen)
game.play()

# listen to the changes 
turtle.update()
screen.mainloop()