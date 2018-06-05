from colorama import Fore, Style
import random

class Cell:
    # constructor 
    def __init__(self, value, x, y, row, col, sqr):
        # copy value and position of the cell
        self.__value = value
        self.__x = x
        self.__y = y

        # check if the value is empty
        if value != "0":
            self.__possibilities = []
        else: 
            self.__possibilities = ["1","2","3","4","5","6","7","8","9"]

        # give the cell info for possible values
        self.__col = []
        self.__row = []
        self.__sqr = []
        
        for c in col:
            self.__col.append(c)
        
        for r in row:
            self.__row.append(r)
        
        for s in sqr:
            self.__sqr.append(s)
    
    def set_possibilities(self):
            # check vertical line
            for c in self.__col:
                for p in self.__possibilities:
                    if p == c:
                        self.__possibilities.pop(self.__possibilities.index(p))
                
            # check horisontal line
            for r in self.__row:
                for p in self.__possibilities:
                    if p == r:
                        self.__possibilities.pop(self.__possibilities.index(p))

            # check square
            for s in self.__sqr:
                for p in self.__possibilities:
                    if p == s:
                        self.__possibilities.pop(self.__possibilities.index(p))
        
    # get x coordinate of Cell
    def get_x(self):
        return self.__x

    # get y coordinate of Cell
    def get_y(self):
       return self.__y
    
    # get possibilities of Cell
    def get_possibilities(self):
        return self.__possibilities
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
        for col in range(9):
            for row in range(9):
                if col == y:
                    column.append(self.__data[row][col])
        return column
    
    # get sqr 
    def get_sqr(self,x,y):
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

    #show
    def show(self):
        print("------------------")
        for row in range(9):
            string = ""
            for item in range(9):
                if len(self.__data[row][item]) == 1:
                    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN] 
                    color = random.choice(colors)
                    string += color + str(self.__data[row][item]) + Style.RESET_ALL + "|"
                else:
                    for possibility in self.__data[row][item]:
                        string += str(possibility)
                    string+="|"
            print(string)
        print("------------------")

class Board:
    # constructor 
    def __init__(self, data):
        self.__data = Data(data)
        self.__cells = [] 
        print(Fore.YELLOW + "Initial sudoku: " + Style.RESET_ALL) 
        self.show()    
        self.solve()
    #show
    def show(self):
        self.__data.show()

    # solve
    def solve(self):
        self.__cells = []
        # fill the cells with data
        for row in range(9):
            for col in range(9):
                if self.__data.get_value(row,col) == '0':
                    new_cell = Cell("0",col,row,self.__data.get_col(col),self.__data.get_row(row),self.__data.get_sqr(col,row))    
                    new_cell.set_possibilities()
                    self.__cells.append(new_cell)
                else:
                    new_cell = Cell(str(self.__data.get_value(row,col)),col,row,self.__data.get_col(col),self.__data.get_row(row),self.__data.get_sqr(col,row))
                    self.__cells.append(new_cell) 

        # set of data with possibilities
        rows = []
        result = []
        counter = 0

        for row in range(9):
            for col in range(9):
                # add possibilities to result data set
                if self.__data.get_value(row,col) == '0':
                    for cell in self.__cells:                    
                        if cell.get_x() == col:
                            if cell.get_y() == row:
                                if len(self.__cells[self.__cells.index(cell)].get_possibilities()) == 1:
                                    rows.append(self.__cells[self.__cells.index(cell)].get_possibilities()[0])
                                else:
                                    rows.append(self.__data.get_value(row,col))
                # add actual cells to result data set
                else:
                    rows.append(self.__data.get_value(row,col))
                if counter % 9 == 8:
                    result.append(rows)
                    rows = []
                counter += 1
                
        self.__data = []
        self.__data = Data(result)

        # recursion part
        done = True
        for row in range(9):
            for col in range(9):
                if self.__data.get_value(row,col) == '0':
                    done = False

        if done == True:
            print(Fore.GREEN + "Final solution is: " + Style.RESET_ALL)
            self.__data.show()
        else:
            self.solve()  

    # get possibilities of the cell    
    def get_possibilities(self,cell):
        return cell.get_possibilities()
    
# sudoku numbers
data = [
  ['5', '3', '0', '0', '7', '0', '0', '0', '0'],
  ['6', '0', '0', '1', '9', '5', '0', '0', '0'],
  ['0', '9', '8', '0', '0', '0', '0', '6', '0'],
  ['8', '0', '0', '0', '6', '0', '0', '0', '3'],
  ['4', '0', '0', '8', '0', '3', '0', '0', '1'],
  ['7', '0', '0', '0', '2', '0', '0', '0', '6'],
  ['0', '6', '0', '0', '0', '0', '2', '8', '0'],
  ['0', '0', '0', '4', '1', '9', '0', '0', '5'],
  ['0', '0', '0', '0', '8', '0', '0', '7', '9']]

b = Board(data)
