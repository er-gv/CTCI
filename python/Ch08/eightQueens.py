def print_board(board, n):
    for x in range(n):
        print(board[x])


def eight_queens(board, n, queens_left):

    def test_rows(board, n):
        # print("@test_rows")
        for row in range(n):
            if board[row].count(1) > 1:
                return False
        return True

    def test_coloumns(board, n):
        for col in range(n):
            if [item[col] for item in board].count(1) > 1:
                return False
        return True

    def test_positive_diagonals(board, n):
        # print("@test_positive_diagonals")
        for x in range(n):
            square = [x, 0]
            queens_count = 0
            while square[0] < n and queens_count < 2:
                queens_count = queens_count + board[square[0]][square[1]]
                square[1] += 1
                square[0] += 1
            if queens_count > 1:
                return False

        for x in range(n):
            square = [0, x]
            queens_count = 0
            while square[1] < n and queens_count < 2:
                queens_count = queens_count + board[square[0]][square[1]]
                square[1] += 1
                square[0] += 1
            if queens_count > 1:
                return False
        return True

    def test_negative_diagonals(board, n):
        # print("@test_negative_diagonals")
        for x in range(n):
            square = [0, x]
            queens_count = 0
            while square[1] > -1 and queens_count < 2:
                # print (square,  board[square[0]][square[1]])
                queens_count = queens_count + board[square[0]][square[1]]
                square[1] -= 1
                square[0] += 1
            if queens_count > 1:
                return False
        # print("@test_negative_diagonals_phase 2")
        for x in range(n):
            square = [x, n - 1]
            queens_count = 0
            while square[0] < n and queens_count < 2:
                # print (square, board[square[0]][square[1]])
                queens_count = queens_count + board[square[0]][square[1]]
                square[1] -= 1
                square[0] += 1
            if queens_count > 1:
                return False
        return True

    def no_contradictions(board, n):
        # test rows
        return test_rows(board, n) \
               and test_coloumns(board, n) \
               and test_negative_diagonals(board, n) \
               and test_positive_diagonals(
            board, n)


    if queens_left is 0:
        return board

    #print("need to place more " + str(queens_left) + " on this board:")
    #print_board(board, n)

    for i in range(0, n):
        #print("Will try col " + str(i) + " on row " + str(n - queens_left))
        board[n-queens_left][i] = 1
        #print("Now after placing a queen, the board looks like son:")
        #print_board(board, n)
        if no_contradictions(board, n):
            if not eight_queens(board, n, queens_left - 1):
                board[n - queens_left][i] = 0
            else:
                return board
        else:
            board[n - queens_left][i] = 0
    queens_left += 1
    if queens_left >= n:
        return False
    return True








def eight_queens_solver(n):
    b= [[0 for x in range(n)] for x in range(n)]
    if eight_queens(b, n, n):
        print("There is a solution for n = "+str(n)+".")

        print_board(b, n)
    else:
        print("No solution found for n = "+str(n)+".")
    print("")


