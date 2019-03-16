from PyQt5.QtWidgets import QApplication, QTableView

from sudoku_box_model import SudokuBoxModel
import signal

def main():
    # Catch control-C to kill the program
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication([])
    
    # Set title  (Not sure if this is the best solution)
    app.setApplicationDisplayName('Test')
    
    table_view = QTableView()
    model = SudokuBoxModel()
    table_view.setModel(model)

    # Hide headers
    hor_header = table_view.horizontalHeader()
    hor_header.hide()
    vert_header = table_view.verticalHeader()
    vert_header.hide()

    table_view.show()

    return app.exec()

if __name__ == "__main__":
    main()