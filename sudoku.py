from PyQt5.QtCore import Qt, pyqtSignal, QObject

class SudokuBoard(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.board =[[ "X_" + str(y)+ str(x) for x in range(9)] for y in range(9)]
        self.col_mapping = [[0 for i in range(9)] for j in range(9)]
        self.row_mapping = [[0 for i in range(9)] for j in range(9)]
        self.box_mapping = [[0 for i in range(9)] for j in range(9)]
        self.solved = False

    def create_board(self):
        # TODO Creates an easy board from a preset list
        pass

    def test(self):
        b = [[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,3,1,8,7,5,6,9,4],[6,7,4,9,1,2,5,3,8],[8,9,5,3,6,4,2,1,7],[3,1,7,5,4,2,9,6,8],[2,6,5,8,9,7,3,4,1],[9,4,8,6,3,1,5,7,2]]
        for box in range(len(b)):
            for location in range(len(b[box])):
                value = b[box][location]
                self.update_mappings(box, location, value)
                self.board[box][location] = value
        return
                

    def is_editable(self, col, row):
        return True

    def solve(self):
        # TODO Solve the board using the mappings
        print("Solved")
        self.solved = True

    def get_data(self, col, row):
        board = (row//3)*3 + (col//3)
        offset = (row % 3) *3 + (col %3)
        return self.board[board][offset]

    def check(self):
        # Checks if solved
        if self.check_mapping(self.box_mapping) and self.check_mapping(self.col_mapping) \
             and self.check_mapping(self.row_mapping):
            self.solved = True
        else:
            self.solved = False

    def check_mapping(self, mapping):
        assert(len(mapping) == 9)
        for l in mapping:
            for count in l:
                if count != 1:
                    return False
        return True

    def user_input(self, col, row, value):
        move = SudokuMove(col, row, value)
        if move.is_valid():
            self.update_mappings(move.box, move.location, move.value)
            self.board[move.box][move.location] = move.value
            self.check()
        
    def update_mappings(self, box, location, value):
        prev_index = -1
        try:
            prev_index = int(self.board[box][location]) - 1
        except ValueError:
            prev_index = -1

        curr_index = int(value) - 1

        # Update box mapping
        if prev_index >= 0 and self.box_mapping[box][prev_index] > 0:
            self.box_mapping[box][prev_index] -= 1
        self.box_mapping[box][curr_index] += 1

        # Update row mapping
        row = self.get_row(box, location)
        if prev_index >= 0 and self.row_mapping[row][prev_index] > 0:
            self.row_mapping[row][prev_index] -= 1
        self.row_mapping[row][curr_index] += 1
        
        # Update column mapping
        column = self.get_column(box, location)
        if prev_index >= 0 and self.col_mapping[column][prev_index] > 0:
            self.col_mapping[column][prev_index] -= 1
        self.col_mapping[column][curr_index] += 1

    def get_row(self, box, location):
        row = 0

        # Add offset based on box index
        if box >= 3 and box < 6:
            row += 3
        if box >= 6 and box < 9:
            row += 6
        
        # Add offset based on location index:
        if location >= 3 and location < 6:
            row += 1
        if location >= 6 and location < 9:
            row += 2
        
        return row

    def get_column(self, box, location):
        col = 0

        # Add offset based on box index
        if box % 3 == 1:
            col += 3
        if box % 3 == 2:
            col += 6

        # Add offset based on location index
        if location % 3 == 1:
            col += 1
        if location % 3 == 2:
            col += 2
        
        return col

class SudokuMove:
    def __init__(self, col, row, value):
        self.box = (row//3)*3 + (col//3)
        self.location = (row % 3) *3 + (col %3)
        try:
            self.value = int(value)
        except ValueError:
            self.value = -1

    def is_valid(self):
        if self.box < 0 or self.box >= 9:
            return False
        if self.location < 0 or self.location >= 9:
            return False
        if self.value < 1 or self.value > 9:
            return False
        return True

if __name__ == "__main__":
    game = SudokuBoard()
    game.user_input()