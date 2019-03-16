import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import sudoku

class SudokuBoxModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.board_data = sudoku.SudokuBoard(self)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.board_data.get_data(index.column(), index.row())
        
        if role == QtCore.Qt.BackgroundRole:
            if self.board_data.solved:
                return QtGui.QBrush(QtCore.Qt.darkGreen)
            val = self.board_data.get_data(index.column(), index.row())

            try:
                if (int(val) > 0 and int(val) < 10):
                    return QtGui.QBrush(QtCore.Qt.green)
                return QtGui.QBrush(QtCore.Qt.red)
            except ValueError:
                return QtGui.QBrush(QtCore.Qt.red)
        return None

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            if value == "test":
                self.board_data.test()
            else:
                self.board_data.user_input(index.column(), index.row(), value)
            return True
        return False
    
    def columnCount(self, parent):
        return len(self.board_data.board)
    
    def rowCount(self, parent):
        return len(self.board_data.board[0])
    
    def flags(self, index):
        flags = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        if self.board_data.is_editable(index.column(), index.row()):
            flags |= QtCore.Qt.ItemIsEditable
        return flags