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
