import turtle

__version__ = '1.0.1'
__author__ = 'Oleksii Polovyi'

class Square:
    """This class draws the squares for Snake game"""
    def __init__(self, pen):
        """Constructor for Square class. This funcion is called upon 
        initialization. It saves a turtle object as a class member and
        sets size of the square to 20. Also, it sets default value of 
        the position to (0,0)
        Parameters
        ----------
        pen : turtle
            Turtle object that will draw the square
        Returns
        -------
        None
        """
        self.pen = pen
        self.size = 10
        self.x = 0
        self.y = 0
    
    def set_square(self, x, y):
        """Setter for square (x,y) location basen on given arguments.
        Parameters
        ----------
        x : int
            Horizontal coordinate
        y : int 
            Vertical coordinate 
        Returns
        -------
        None
        """
        self.x = x
        self.y = y

    def draw(self, x, y, color):   
        """Draw square at (x,y) location of given color using self.pen.
        Parameters
        ----------
        x : int
            Horizontal coordinate
        y : int 
            Vertical coordinate 
        color : str
            Color of the square
        Returns
        -------
        None
        """
        self.pen.penup()
        self.pen.goto(x,y)
        self.pen.color(color)
        self.pen.pendown()
        # fill the square
        self.pen.begin_fill()
        for _ in range(4):
            self.pen.fd(self.size)
            self.pen.left(90)
        self.pen.end_fill()

if __name__ == '__main__':
	sqr = Square(turtle.Turtle(visible=False))
	sqr.draw(20,0,"red")
	turtle.Screen().mainloop()
