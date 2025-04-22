PLAYER, OPPONENT, EMPTY = 'X', 'O', '_'

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_moves_left(board):
    for row in board:
        if EMPTY in row:
            return True
    return False

def evaluate(board):
    # Rows
    for row in board:
        if row.count(PLAYER) == 3:
            return 1
        if row.count(OPPONENT) == 3:
            return -1
    
    # Columns
    for col in range(3):
        if all(board[row][col] == PLAYER for row in range(3)):
            return 1
        if all(board[row][col] == OPPONENT for row in range(3)):
            return -1
    
    # Diagonals
    if all(board[i][i] == PLAYER for i in range(3)) or all(board[i][2 - i] == PLAYER for i in range(3)):
        return 1
    if all(board[i][i] == OPPONENT for i in range(3)) or all(board[i][2 - i] == OPPONENT for i in range(3)):
        return -1
    
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)
    if score == 1 or score == -1 or not is_moves_left(board):
        return score

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = OPPONENT
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                print(f"Position ({i},{j}) has utility: {move_val}")
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

def main():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Initial Board:")
    print_board(board)

    while is_moves_left(board) and evaluate(board) == 0:
        x, y = find_best_move(board)
        board[x][y] = PLAYER
        print("AI plays:")
        print_board(board)
        if evaluate(board) != 0 or not is_moves_left(board):
            break

        try:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if not (0 <= row <= 2 and 0 <= col <= 2):
                raise ValueError("Row and column must be between 0 and 2.")
            if board[row][col] != EMPTY:
                raise ValueError("Cell already occupied. Try again.")
            board[row][col] = OPPONENT
        except ValueError as e:
            print("Invalid input:", e)
            continue

        print("After your move:")
        print_board(board)

    result = evaluate(board)
    if result == 1:
        print("AI wins!")
    elif result == -1:
        print("You win!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
