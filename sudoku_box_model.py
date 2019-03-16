import PyQt5.QtCore as QtCore
import sudoku

class SudokuBoxModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.board_data = sudoku.SudokuBoard()

    def data(self, index, role):
        offset = index.row()*3 + index.column()
        return self.board_data.board[index.column()][index.row()]
    
    def columnCount(self, parent):
        return len(self.board_data.board)
    
    def rowCount(self, parent):
        return len(self.board_data.board[0])