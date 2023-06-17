import math, random


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):  # constructor, parameters used when calling the function 
        self.row_length = row_length 
        self.removed_cells = removed_cells
        self.board = [[0 for j in range(self.row_length)] for i in range(self.row_length)]  # creates a 2D list with zeros in it as placeholders
        self.box_length = int(math.sqrt(self.row_length)) 

    def get_board(self):  # getter of the board to see where things are placed in a 2D list
        return self.board

    def print_board(self):
        for i in self.board:  # prints each list from the board
            print(i)

    def valid_in_row(self, row, num):  # checks to see if the number is in the row, if it is returns false
        if num in self.board[row]:
            return False
        else:
            return True

    def valid_in_col(self, col, num):  # makes sure there are no doubles in a column
        for row in range(len(self.board)):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):  # checks each three
        new_list = []
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                new_list.append(self.board[i][j])  # uses the new list to see whether there are doubles/more than one
        if num in new_list: 
            return False
        else:
            return True

    def is_valid(self, row, col, num):
        start_row = 0
        start_col = 0
        if row == 0 or row == 1 or row == 2:  # makes sure to check each box, uses three rows and makes same starting row
            start_row = 0
        elif row == 3 or row == 4 or row == 5:
            start_row = 3
        elif row == 6 or row == 7 or row == 8:
            start_row = 6
        if col == 0 or col == 1 or col == 2:
            start_col = 0
        elif col == 3 or col == 4 or col == 5:
            start_col = 3
        elif col == 6 or col == 7 or col == 8:
            start_col = 6
        if self.valid_in_row(row, num) is True and self.valid_in_col(col, num) is True and self.valid_in_box(start_row, start_col, num) is True:
            return True  # checks the boxes and makes sure they do not have doubles as well as checks rows and cols to make sure the whole thing is valid
        else:
            return False

    def fill_box(self, row_start, col_start):
        numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list of numbers to place into the board
        for i in range(0, 3):
            for j in range(0, 3):
                adding_integer = random.choice(numlist)
                if self.valid_in_box(row_start, col_start, adding_integer) is True:
                    self.board[row_start+i][col_start + j] = adding_integer  # places the numbers
                    numlist.remove(adding_integer)  # once a number is selected it is removed
                # elif self.valid_in_box(row_start, col_start, adding_integer) is False:
                #     adding_integer = random.choice(numlist)

    def fill_diagonal(self):
        self.fill_box(0, 0)  # causes the fill box method to fill the boxes across the board
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):  
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()  # calls the diagnoal method to fill them in with random numbers
        self.fill_remaining(0, self.box_length)  # fills the rest with 0's as a placeholder

    def remove_cells(self):  
        count = 0
        while count < self.removed_cells:  # removes one cell at a time
            randrow = random.randint(0, 8)  # picks a cell in a random row/col
            randcol = random.randint(0, 8)
            if self.board[randrow][randcol] != 0:
                self.board[randrow][randcol] = 0  # replaces the cells with 0
                count += 1


def generate_sudoku(size, removed):  # has the size of the board and the number removed in the parameters
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


