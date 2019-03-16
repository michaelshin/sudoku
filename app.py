if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QTableView
    from sudoku_box_model import SudokuBoxModel

    app = QApplication([])
    table_view = QTableView()
    # Model the boxes
    model = SudokuBoxModel()
    table_view.setModel(model)


    # Model the sub-boxes and link with the parent box
    
    # Connect the model to the widget


    table_view.show()

    app.exec()