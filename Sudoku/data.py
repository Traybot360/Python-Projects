from colorama import Fore, Style
import random

class Data:
    # constructor 
    def __init__(self, data):
        self.__data = []
        for i in data:
            self.__data.append(i)
    
    # get row
    def get_row(self,x):
        for row in range(9):
            if row == x:
                return self.__data[x]
    
    # get col 
    def get_col(self,y):
        column = []
        # column will hold a list of values from given column
        for col in range(9):
            for row in range(9):
                if col == y:
                    column.append(self.__data[row][col])
        return column
    
    # get sqr 
    def get_sqr(self,x,y):
        # sqr will hold a list of values from quadrant
        sqr = []
        # Q1
        if x >= 0 and x <=2 and y >= 0 and y <=2:
            x = 0 
            y = 0
            for i in range(x,x+3):
                for j in range(y,y+3):
                    sqr.append(self.__data[j][i])
        # Q2
        elif x >= 3 and x <=5 and y >= 0 and y <=2:
            x = 3 
            y = 0
            for i in range(x,x+3):
                for j in range(y,y+3):
                    sqr.append(self.__data[j][i])
        # Q3
        elif x >= 6 and x <=8 and y >= 0 and y <=2:
            x = 6 
            y = 0
            for i in range(x,x+3):
                for j in range(y,y+3):
                    sqr.append(self.__data[j][i])
        # Q4
        elif x >= 0 and x <=2 and y >= 3 and y <=5:
            x = 0 
            y = 3
            for i in range(x,x+3):
                for j in range(y,y+3):
                    sqr.append(self.__data[j][i])
        # Q5
        elif x >= 3 and x <=5 and y >= 3 and y <=5:
            x = 3 
            y = 3
            for i in range(x,x+3):
                for j in range(y,y+3):
                    sqr.append(self.__data[j][i])
        # Q6
        elif x >= 6 and x <=8 and y >= 3 and y <=5:
            x = 6 
            y = 3
            for i in range(x,x+3):
                for j in range(y,y+3):
                    sqr.append(self.__data[j][i])
        # Q7
        elif x >= 0 and x <=2 and y >= 6 and y <=8:
            x = 0 
            y = 6
            for i in range(x,x+3):
                for j in range(y,y+3):
                    sqr.append(self.__data[j][i])
        # Q8
        elif x >= 3 and x <=5 and y >= 6 and y <=8:
            x = 3 
            y = 6
            for i in range(x,x+3):
                for j in range(y,y+3):
                    sqr.append(self.__data[j][i])
        # Q9
        elif x >= 6 and x <=8 and y >= 6 and y <=8:
            x = 6 
            y = 6
            for i in range(x,x+3):
                for j in range(y,y+3):
                    sqr.append(self.__data[j][i])

        return sqr  

    # get value of one data member
    def get_value(self,x,y):
        return self.__data[x][y]

    # display sudoku to the console
    def show(self):
        print("------------------")
        for row in range(9):
            string = ""
            for item in range(9):
                if len(self.__data[row][item]) == 1:
                    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN] 
                    color = random.choice(colors)
                    string += color + str(self.__data[row][item]) + Style.RESET_ALL + "|"
            print(string)
        print("------------------")
