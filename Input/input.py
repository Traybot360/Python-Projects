import turtle 

class Input:
    # constructor
    def __init__(self):
        self.string = ""

    # get key and display current value of input
    def key(self,value):
        self.string += value
        pen.clear()
        pen.write(self.string,align="center", font=("Arial", 12, "normal"))

    # display the result when user hit Enter
    def display(self):
        pen.clear()
        pen.color("red")
        pen.write("You have entered: " + self.string,align="center", font=("Arial", 12, "normal"))
        pen.color("black")
        self.string = ""
  
    # erase last character using Backspace
    def erase(self):
        pen.clear()
        self.string = self.string[:len(self.string)-1]
        pen.write(self.string,align="center", font=("Arial", 12, "normal"))

# display instructions for user
txt = turtle.Turtle()
txt.hideturtle()
txt.penup()
txt.goto(0,50)
txt.write("Type text, use Enter to start again",align="center", font=("Arial", 25, "normal"))

# draw user input
pen = turtle.Turtle()
pen.hideturtle()
screen = turtle.Screen()
inp = Input()

# check user input
screen.onkey(lambda: inp.display(), "Enter")
screen.onkey(lambda: inp.erase(), "BackSpace")
screen.onkey(lambda: inp.key(" "), "Space")
screen.onkey(lambda: inp.key("a"), "a")
screen.onkey(lambda: inp.key("b"), "b")
screen.onkey(lambda: inp.key("c"), "c")
screen.onkey(lambda: inp.key("d"), "d")
screen.onkey(lambda: inp.key("e"), "e")
screen.onkey(lambda: inp.key("f"), "f")
screen.onkey(lambda: inp.key("g"), "g")
screen.onkey(lambda: inp.key("h"), "h")
screen.onkey(lambda: inp.key("i"), "i")
screen.onkey(lambda: inp.key("j"), "j")
screen.onkey(lambda: inp.key("k"), "k")
screen.onkey(lambda: inp.key("l"), "l")
screen.onkey(lambda: inp.key("m"), "m")
screen.onkey(lambda: inp.key("n"), "n")
screen.onkey(lambda: inp.key("o"), "o")
screen.onkey(lambda: inp.key("p"), "p")
screen.onkey(lambda: inp.key("q"), "q")
screen.onkey(lambda: inp.key("r"), "r")
screen.onkey(lambda: inp.key("s"), "s")
screen.onkey(lambda: inp.key("t"), "t")
screen.onkey(lambda: inp.key("u"), "u")
screen.onkey(lambda: inp.key("v"), "v")
screen.onkey(lambda: inp.key("w"), "w")
screen.onkey(lambda: inp.key("x"), "x")
screen.onkey(lambda: inp.key("y"), "y")
screen.onkey(lambda: inp.key("z"), "z")
screen.onkey(lambda: inp.key("1"), "1")
screen.onkey(lambda: inp.key("2"), "2")
screen.onkey(lambda: inp.key("3"), "3")
screen.onkey(lambda: inp.key("4"), "4")
screen.onkey(lambda: inp.key("5"), "5")
screen.onkey(lambda: inp.key("6"), "6")
screen.onkey(lambda: inp.key("7"), "7")
screen.onkey(lambda: inp.key("8"), "8")
screen.onkey(lambda: inp.key("9"), "9")
screen.onkey(lambda: inp.key("0"), "0")

# listen to the changes 
screen.listen()