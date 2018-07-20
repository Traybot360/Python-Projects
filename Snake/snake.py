import turtle
from food import Food
from square import Square

__version__ = '1.0.0'
__author__ = 'Oleksii Polovyi'

class Snake(object):
    """This class draws and operates the line for Snake game"""
    def __init__(self, pen, food_pen):
        """Constructor for Square class. This funcion is called upon 
        initialization. It saves a turtle object as a class member,
        start line length to 5, creates list of Squares, set direction
        to 'r', default speed to 1, creates food for snake and creates
        snake itself.

        Possible directions are : 'r', 'l', 'u', 'd'

        Parameters
        ----------
        pen : turtle
            Turtle object that will draw the square
        food_pen : turtle
            Turtle object that will draw the food
        Returns
        -------
        None
        """
        
        self.speed = 1
        self.snake = []
        self.direction = 'r'
        self.length = 5

        self.pen = pen
        self.food_pen = food_pen

        # creating initial snake
        for i in range(self.length):
            square = Square(self.pen)
            square.set_square(i*-square.size, square.size)
            self.snake.append(square)
        
        self.food = Food(self.food_pen)
        self.food.create_food()
        
    def set_direction(self,value):
        """Change direction of the snake.
        Parameters
        ----------
        value : str
            New snake direction
        Returns
        -------
        None
        """
        if self.direction == 'r' and value != 'l':
            self.direction = value
        if self.direction == 'l' and value != 'r':
            self.direction = value
        if self.direction == 'u' and value != 'd':
            self.direction = value
        if self.direction == 'd' and value != 'u':
            self.direction = value
       
    def self_collision(self):
        """Check snake collision with itself.
        Parameters
        ----------
        None
        Returns
        -------
        collision
            bool
        """
        collision = False
        for sqr in range(1,len(self.snake)):
            if self.snake[0].x == self.snake[sqr].x and self.snake[0].y == self.snake[sqr].y:
                collision = True
        return collision
    
    def border_collision(self):
        """Check snake collision with border.
        Parameters
        ----------
        None
        Returns
        -------
        collision
            bool
        """
        collision = False
        if self.snake[0].x > 200 or self.snake[0].x < -200:
            collision = True
        elif self.snake[0].y > 200 or self.snake[0].y < -200:
            collision = True
        
        return collision

    def draw_snake(self):
        """Draw snake.
        Parameters
        ----------
        None
        Returns
        -------
        None
        """
        for i in range(len(self.snake)):
            self.snake[i].draw(self.snake[i].x,self.snake[i].y, "black")

    def move_snake(self):
        """Move snake.
        Parameters
        ----------
        None
        Returns
        -------
        None
        """
        old_x = self.snake[0].x
        old_y = self.snake[0].y
    
        for square in range(len(self.snake)):
            if square == 0: 
                old_x = self.snake[square].x
                if self.direction == "r":  
                    self.snake[square].x += self.snake[0].size
                elif self.direction == "l":
                    self.snake[square].x -= self.snake[0].size
                elif self.direction == "u":
                    self.snake[square].y += self.snake[0].size
                elif self.direction == "d":
                    self.snake[square].y -= self.snake[0].size
            else:
                old_x, self.snake[square].x = self.snake[square].x, old_x
                old_y, self.snake[square].y = self.snake[square].y, old_y

    def food_collision(self,x,y):
        """Check collision with food.
        Parameters
        ----------
        x
            Horisontal Coordinate
        y
            Vertical Coordinate
        Returns
        -------
        collision
            bool
        """
        
        collision = False

        # food_collision
        if self.food.collision_with_food(x,y):
            # add square to the snake
            square = Square(self.pen)
            square.set_square(x,y)
            self.snake.append(square)

            # make snake move faster
            self.increase_speed()    
            
            # make more food
            self.food.create_food()
            self.food.draw_food()

            # increase the length of the snake
            self.length += 1
            
            collision = True
        
        return collision
    
    def increase_speed(self):
        """Incerease spped of the snake.
        Parameters
        ----------
        None
        Returns
        -------
        None
        """
        
        self.speed += 1
        self.pen.speed(self.speed)
