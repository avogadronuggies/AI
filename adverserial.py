PLAYER, OPPONENT, EMPTY = 'X', 'O', '_'

def print_board(board): print('\n'.join(' '.join(row) for row in board), '\n')

def is_moves_left(board): return any(EMPTY in row for row in board)

def evaluate(board):
    for row in board:
        if row.count(PLAYER) == 3: return 1
        if row.count(OPPONENT) == 3: return -1
    for col in range(3):
        if all(board[row][col] == PLAYER for row in range(3)): return 1
        if all(board[row][col] == OPPONENT for row in range(3)): return -1
    if all(board[i][i] == PLAYER for i in range(3)) or all(board[i][2 - i] == PLAYER for i in range(3)): return 1
    if all(board[i][i] == OPPONENT for i in range(3)) or all(board[i][2 - i] == OPPONENT for i in range(3)): return -1
    return 0

def minimax(board, is_max):
    score = evaluate(board)
    if score or not is_moves_left(board): return score
    best = -1000 if is_max else 1000
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER if is_max else OPPONENT
                best = max(best, minimax(board, False)) if is_max else min(best, minimax(board, True))
                board[i][j] = EMPTY
    return best

def find_best_move(board):
    best_val, best_move = -1000, (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER
                move_val = minimax(board, False)
                board[i][j] = EMPTY
                if move_val > best_val: best_val, best_move = move_val, (i, j)
    return best_move

def main():
    board = [[EMPTY] * 3 for _ in range(3)]
    print_board(board)
    while is_moves_left(board) and not evaluate(board):
        x, y = find_best_move(board)
        board[x][y] = PLAYER
        print("AI plays:")
        print_board(board)
        if evaluate(board) or not is_moves_left(board): break
        try:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] != EMPTY: raise ValueError("Cell occupied.")
            board[row][col] = OPPONENT
        except: print("Invalid input. Try again.")
        print_board(board)
    print("AI wins!" if evaluate(board) == 1 else "You win!" if evaluate(board) == -1 else "It's a draw!")

if __name__ == "__main__":
    main()
