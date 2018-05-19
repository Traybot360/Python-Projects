import math
from colorama import Fore, Style

# NOTE: remove on repl.it
# for windows 10 colors
from colorama import init
init(convert=True)
# end of windows 10 colors

class Pascal:
    # constructor
    def __init__(self, amount):
        try: 
            if int(amount) > 0:
                self.amount = int(amount)
                
                # fill the data
                self.data = []
                for index in range(self.amount):
                    row = []
                    for i in range(index+1):
                        row.append(self.combo(index, i))
                    self.data.append(row)
                # display the values
                self.show()
            else: 
                raise ValueError()
        except ValueError:
            print(Fore.RED + "Please enter integer greater than zero..." + Style.RESET_ALL)

    # using the formula: n! / k! * (n-k)!
    def combo(self, n, k):
        return int((math.factorial(n)) / ((math.factorial(k)) * math.factorial(n - k)))

    def show(self):
        for row in self.data:
            if self.data.index(row) % 2 == 0 :
                print(Fore.YELLOW + str(row) + Style.RESET_ALL)
            else:
                print(Fore.CYAN + str(row) + Style.RESET_ALL)

p = Pascal(input("Number of rows: "))