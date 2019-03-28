import pickle
games = []
for i in range(1088):
    filename = "sudoku_games/image" + str(i) + ".dat"
    try:
        f = open(filename, "r")
    except:
        continue
    a = []
    for line in f:
        b = line.split()
        a.append(b) 
    a = a[2:]
    assert(len(a) == 9)
    board =[[ "" for x in range(9)] for y in range(9)]

    for row in range(9):
        for col in range(9):
            val = a[row][col]
            box = (row//3)*3 + (col//3)
            offset = (row % 3) *3 + (col %3)
            board[box][offset] = val
    games.append(board)

pickle.dump(games, open("games.p", "wb"))