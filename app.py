import sys, signal
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableView, QHeaderView, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from sudoku_box_model import SudokuBoxModel

class MainWindow(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Sudoku!!'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.init_ui()
 
    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.create_table_view()
 
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table_view) 
        self.setLayout(self.layout) 
 
        # Show widget
        self.show()
 
    def create_table_view(self):
        self.table_view = QTableView()
        self.model = SudokuBoxModel()
        self.table_view.setModel(self.model)

        # set the cell size and fix the size. Then hide the headers
        hor_header = self.table_view.horizontalHeader()
        hor_header.setDefaultSectionSize(40)
        hor_header.setSectionResizeMode(QHeaderView.Fixed)
        hor_header.hide()
        vert_header = self.table_view.verticalHeader()
        vert_header.hide()
        vert_header.setDefaultSectionSize(40)
        vert_header.setSectionResizeMode(QHeaderView.Fixed)
  
def main():
    # Catch control-C to kill the program
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)
    main_window = MainWindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()