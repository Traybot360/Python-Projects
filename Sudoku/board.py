from colorama import Fore, Style
from data import Data
from cell import Cell
class Board:
    # constructor 
    def __init__(self, data):
        self.__data = Data(data)
        self.__cells = [] 
        print(Fore.YELLOW + "Initial sudoku: " + Style.RESET_ALL) 
        self.show()    
        self.solve()
    
    # display sudoku to the console 
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
        # counter for the rows
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
