from colorama import Fore, Style

class Factorial:
  # constructor
  def __init__(self, number):
    self.number = number
    try:
      if int(self.number) >= 0:
        print(Fore.GREEN + "Answer: " + Fore.BLUE + str(self.factorial(int(self.number))) + Style.RESET_ALL)
      else:
        raise ValueError()
    except ValueError:
      print(Fore.RED + "Input must be greater or equal to zero. Please try again..." + Style.RESET_ALL)
  
  # factorial solver
  def factorial(self, n):
    if n == 0:
      return 1
    else:
      return n * self.factorial(n-1)

f = Factorial(input("Please input the number: "))
