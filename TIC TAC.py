import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    
    for row in board:
        if all(cell == player for cell in row):
            return True

   
   
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

   
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_val = float('-inf')
    best_move = None

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True 
    while True:
        print_board(board)

        if player_turn:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                player_turn = not player_turn
            else:
                print("Cell already occupied. Try again.")
        else:
            print("Computer's turn:")
            best_move = get_best_move(board)
            board[best_move[0]][best_move[1]] = 'O'
            player_turn = not player_turn

        if check_winner(board, 'X'):
            print_board(board)
            print("Player X wins!")
            break
        elif check_winner(board, 'O'):
            print_board(board)
            print("Player O wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
