class sudoku_board:
    def __init__(self):
        self.board =[[ "X_" + str(y)+ str(x) for x in range(9)] for y in range(9)]
        self.col_mapping = { i: dict() for i in range(9)}
        self.row_mapping = { i: dict() for i in range(9)}
        self.box_mapping = { i: dict() for i in range(9)}

    def print_board(self):
        self.print_line(self.board[0:3])
        self.print_line(self.board[3:6])
        self.print_line(self.board[6:9])

    def print_line(self, line):
        string = ""
        for i in range(0,9,3):
            string = ""
            for j in range(0,3):
                for k in range(0,3):
                    string += str(line[j][k+i]) + " "
                string += "|"
            print string
        print "------------------------------------------------"

    def create_board(self):
        # TODO Creates an easy board from a preset list
        return

    def solve(self):
        # TODO Solve the board using the mappings
        print "Solved"

    def check(self):
        # TODO Checks if valid
        print "Checking if solved"

    def user_input(self):
        # Processes the user input
        self.print_board()
        move = sudoku_move(raw_input("What is your next move? "))
        if move.is_valid():
            self.update_mappings(move.box, move.location, move.value)
            self.board[move.board][move.location] = move.value
            self.check()
        else:
            print "Entered invalid move!!"

    def update_mappings(self, box, location, value):
        prev = self.board[box][location]
        
        # Update box mapping
        if prev in self.box_mapping[box]:
            self.box_mapping[box][prev] -= 1
        if value in self.box_mapping[box]:
            self.box_mapping[box][value] += 1
        else:
            self.box_mapping[box][value] = 1
        
        # Update row mapping
        row = self.get_row(box, location)
        
        # Update column mapping
        column = self.get_location(box, location)

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

    def get_column(self, box, location)
                

class sudoku_move:
    def __init__(self, user_input):
        # TODO need better names
        # Assumes user input is split by whitespace
        # Need a cleaner way to do this

        user_input = user_input.split()
        print user_input
        if (len(user_input) == 3):
            try:
                self.board = int(user_input[0])
                self.location = int(user_input[1])
                self.value = int(user_input[2])
            except ValueError:
                print("Not an integer! Try again.")
        else:
            self.board = -1
            self.location = -1
            self.value = -1

    def is_valid(self):
        # How would I remove this redundancy?
        if self.board < 0 or self.board >= 9:
            return False
        if self.location < 0 or self.location >= 9:
            return False
        if self.value < 1 or self.value > 9:
            return False
        return True

if __name__ == "__main__":
    a = sudoku_board()
    while True:
        a.user_input()