import turtle, time

turtles = []
for i in range(4):
  turtles.append(turtle.Turtle())

class Clock:
  # constructor
  def __init__(self, turtles, size):
    self.size = size
    self.t = []
    for turtle in turtles:
      turtle.hideturtle()
      turtle.speed(0)
      self.t.append(turtle)
  
  # draw the clock circle using first turtle
  def border(self):
    self.t[0].speed(0)
    self.t[0].circle(self.size)
  
  # draw the clock hours arrow
  def hours(self):
    self.t[1].clear()
    self.t[1].penup()
    self.t[1].goto(0,self.size)
    self.t[1].setheading((-1)*(self.get_h()*360/12-90))
    self.t[1].pendown()
    self.t[1].pensize(3)
    self.t[1].fd(self.size*0.6)
  
  # draw the clock minutes arrow
  def minutes(self):
    self.t[2].clear()
    self.t[2].penup()
    self.t[2].goto(0,self.size)
    self.t[2].setheading((-1)*(self.get_m()*360/60-90))
    self.t[2].pendown()
    self.t[2].pensize(2)
    self.t[2].fd(self.size*0.7)
  
  # draw the clock seconds arrow
  def seconds(self):
    self.t[3].clear()
    self.t[3].penup()
    self.t[3].goto(0,self.size)
    self.t[3].setheading((-1)*(self.get_s()*360/60-90))
    self.t[3].pendown()
    self.t[3].pensize(1)
    self.t[3].fd(self.size*0.8)

  def get_h(self):
    return time.localtime(time.time()).tm_hour

  def get_m(self):
    return time.localtime(time.time()).tm_min

  def get_s(self):
    return time.localtime(time.time()).tm_sec

def main():  
  clock = Clock(turtles,100)
  clock.border()
  
  # numbers
  t = turtle.Turtle()
  t.speed(0)
  t.hideturtle()
  for number in range(1,13):
    t.penup()
    t.goto(0,100)
    t.setheading((-1)*(30*number -90))
    t.fd(85)
    # # use next line to draw the numbers
    # t.write(number, align="center")
    # # use next 3 lines to draw the dashes
    t.pendown()
    t.fd(5)
    t.penup()

  while True:
    turtle.tracer(0,0)
    clock.hours()
    clock.minutes()
    clock.seconds()
    turtle.tracer(20,0)

main()
turtle.update()
