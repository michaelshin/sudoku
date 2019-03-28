import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import pickle
import random

class SudokuBoxModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.board = [[ "" for x in range(9)] for y in range(9)]
        self.editable = [[ True for x in range(9)] for y in range(9)]
        self.col_mapping = [[0 for i in range(9)] for j in range(9)]
        self.row_mapping = [[0 for i in range(9)] for j in range(9)]
        self.box_mapping = [[0 for i in range(9)] for j in range(9)]
        self.solved = False
        self.create_board()

    # Implementing Virtual Functions
    def flags(self, index):
        flags = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        if self.is_editable(index.column(), index.row()):
            flags |= QtCore.Qt.ItemIsEditable
        return flags

    def data(self, index, role):
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter

        if role == QtCore.Qt.DisplayRole:
            return self.get_data(index.column(), index.row())
        
        if role == QtCore.Qt.BackgroundRole:
            box = self.get_box(index.column(), index.row())
            if box % 2 == 0:
                if self.solved:
                    return QtGui.QBrush(QtCore.Qt.green)
                else:
                    return QtGui.QBrush(QtCore.Qt.white)
            else:
                if self.solved:
                    return QtGui.QBrush(QtCore.Qt.darkGreen)
                else:
                    return QtGui.QBrush(QtCore.Qt.lightGray)
        
        if role == QtCore.Qt.FontRole:
            if not self.is_editable(index.column(), index.row()):
                font = QtGui.QFont()
                font.setBold(True)
                return font

        return None

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            if value == "test":
                self.test()
            else:
                print("user input")
                self.user_input(index.column(), index.row(), value)
            return True
        return False
    
    def columnCount(self, parent):
        return len(self.board)
    
    def rowCount(self, parent):
        return len(self.board[0])
    
    # Helper Functions

    def create_board(self):
        # TODO add more generalization with updating mappings
        games = pickle.load(open("games.p", "rb"))
        index = random.randint(0,len(games)-1)
        self.board = games[index]

        for box in range(9):
            for offset in range(9):
                if self.board[box][offset] != "0":
                    self.editable[box][offset] = False

    def is_editable(self, col, row):
        box = self.get_box(col, row)
        offset = self.get_offset(col, row)
        return self.editable[box][offset]

    def solve(self):
        # TODO Solve the board using the mappings
        print("Solved")
        self.solved = True
    
    def get_box(self, col, row):
        return (row//3)*3 + (col//3)

    def get_offset(self, col, row):
        return (row % 3) *3 + (col %3)

    def get_data(self, col, row):
        box = self.get_box(col, row)
        offset = self.get_offset(col, row)
        return self.board[box][offset]

    def check_solved(self):
        # Checks if solved
        print ("Checking rn!!!")
        print(self.box_mapping)
        print(self.col_mapping)
        print(self.row_mapping)
        if self.check_mapping(self.box_mapping) \
            and self.check_mapping(self.col_mapping) \
            and self.check_mapping(self.row_mapping):
            self.solved = True
        else:
            self.solved = False
        print(self.solved)

    def check_mapping(self, mapping):
        assert(len(mapping) == 9)
        for l in mapping:
            for count in l:
                if count != 1:
                    return False
        return True

    def user_input(self, col, row, value):
        box = self.get_box(col, row)
        offset = self.get_offset(col, row)
        if self.is_valid_move(box, offset, value):
            self.update_mappings(box, col, row, offset, value)
            self.board[box][offset] = value
            self.check_solved()
        return

    def is_valid_move(self, box, offset, value):
        try:
            value = int(value)
        except ValueError:
            return False
        
        if box < 0 or box >= 9:
            return False
        if offset < 0 or offset >= 9:
            return False
        if value < 1 or value > 9:
            return False
        return True

        
    def update_mappings(self, box, col, row, offset, value):
        prev_index = -1
        try:
            prev_index = int(self.board[box][offset]) - 1
        except ValueError:
            prev_index = -1

        curr_index = int(value) - 1

        # Update box mapping
        if prev_index >= 0 and self.box_mapping[box][prev_index] > 0:
            self.box_mapping[box][prev_index] -= 1
        self.box_mapping[box][curr_index] += 1

        # Update row mapping
        if prev_index >= 0 and self.row_mapping[row][prev_index] > 0:
            self.row_mapping[row][prev_index] -= 1
        self.row_mapping[row][curr_index] += 1
        
        # Update column mapping
        if prev_index >= 0 and self.col_mapping[col][prev_index] > 0:
            self.col_mapping[col][prev_index] -= 1
        self.col_mapping[col][curr_index] += 1

    def get_row(self, box, offset):
        row = 0

        # Add offset based on box index
        if box >= 3 and box < 6:
            row += 3
        if box >= 6 and box < 9:
            row += 6
        
        # Add offset based on offset index:
        if offset >= 3 and offset < 6:
            row += 1
        if offset >= 6 and offset < 9:
            row += 2
        
        return row

    def get_column(self, box, offset):
        col = 0

        # Add offset based on box index
        if box % 3 == 1:
            col += 3
        if box % 3 == 2:
            col += 6

        # Add offset based on offset index
        if offset % 3 == 1:
            col += 1
        if offset % 3 == 2:
            col += 2
        
        return col
    
    # Function to help test
    def test(self):
        b = [[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,3,1,8,7,5,6,9,4],[6,7,4,9,1,2,5,3,8],[8,9,5,3,6,4,2,1,7],[3,1,7,5,4,2,9,6,8],[2,6,5,8,9,7,3,4,1],[9,4,8,6,3,1,5,7,2]]
        for box in range(len(b)):
            for offset in range(len(b[box])):
                value = b[box][offset]
                row = self.get_row(box, offset)
                col = self.get_column(box, offset)
                self.update_mappings(box, col, row, offset, value)
                self.board[box][offset] = value
        return