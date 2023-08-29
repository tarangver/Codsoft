
import math

def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def is_winner(board, player):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def game_over(board):
    return is_winner(board, "X") or is_winner(board, "O") or is_draw(board)

def evaluate(board):
    if is_winner(board, "X"):
        return 1
    elif is_winner(board, "O"):
        return -1
    else:
        return 0

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, "X"):
        return 1
    if is_winner(board, "O"):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def find_best_move(board):
    best_move = None
    best_eval = -math.inf
    for i, j in get_empty_cells(board):
        board[i][j] = "X"
        move_eval = minimax(board, 0, -math.inf, math.inf, False)
        board[i][j] = " "
        if move_eval > best_eval:
            best_eval = move_eval
            best_move = (i, j)
    return best_move

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while not game_over(board):
        print_board(board)
        player_move = input("Enter your move (row col, e.g. 1 1 for the center): ").split()
        row, col = int(player_move[0]) - 1, int(player_move[1]) - 1

        while board[row][col] != " ":
            print("Invalid move. Try again.")
            player_move = input("Enter your move (row col, e.g. 1 1 for the center): ").split()
            row, col = int(player_move[0]) - 1, int(player_move[1]) - 1

        board[row][col] = "O"

        if not game_over(board):
            ai_move = find_best_move(board)
            board[ai_move[0]][ai_move[1]] = "X"

    print_board(board)
    if is_winner(board, "X"):
        print("AI wins!")
    elif is_winner(board, "O"):
        print("You win!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_tic_tac_toe()



