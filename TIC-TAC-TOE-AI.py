# Importing necessary libraries
import math
import copy

# Constants
X = 'X'  # Player X
O = 'O'  # Player O
EMPTY = ' '  # Empty cell
DRAW = 'Draw'  # Draw outcome
INFINITY = math.inf  # Infinity value

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('----------')

# Function to check if the current player wins
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the game is over
def game_over(board):
    return check_winner(board, X) or check_winner(board, O) or all(all(cell != EMPTY for cell in row) for row in board)

# Function to evaluate the board for the Minimax algorithm
def evaluate(board):
    if check_winner(board, X):
        return 1
    elif check_winner(board, O):
        return -1
    else:
        return 0

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if game_over(board) or depth == 0:
        return evaluate(board), None

    if maximizing_player:
        max_eval = -INFINITY
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board_copy = copy.deepcopy(board)
                    board_copy[i][j] = X
                    eval, _ = minimax(board_copy, depth - 1, False, alpha, beta)
                    if eval > max_eval:
                        max_eval = eval
                        best_move = (i, j)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval, best_move
    else:
        min_eval = INFINITY
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board_copy = copy.deepcopy(board)
                    board_copy[i][j] = O
                    eval, _ = minimax(board_copy, depth - 1, True, alpha, beta)
                    if eval < min_eval:
                        min_eval = eval
                        best_move = (i, j)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval, best_move

# Function for AI player's move
def ai_move(board):
    _, move = minimax(board, 4, True, -INFINITY, INFINITY)
    if move:
        board[move[0]][move[1]] = X

# Function for human player's move
def human_move(board):
    while True:
        try:
            row, col = map(int, input("Enter row and column (0-2) for your move: ").split())
            if 0 <= row <= 2 and 0 <= col <= 2:  # Check if row and col are within the valid range
                if board[row][col] == EMPTY:
                    board[row][col] = O
                    break
                else:
                    print("That cell is already occupied. Please choose another.")
            else:
                print("Invalid input! Please enter row and column numbers between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter row and column numbers separated by space.")
        except IndexError:
            print("Invalid input! Please enter row and column numbers between 0 and 2.")



# Main function to run the game
def main():
    print("Welcome to Tic-Tac-Toe!")
    print("You are playing as O and the AI is playing as X.")
    board = [[EMPTY] * 3 for _ in range(3)]
    while not game_over(board):
        # print_board(board)
        print("_____________")
        ai_move(board)
        if game_over(board):
            break
        print_board(board)
        if game_over(board):
            break
        human_move(board)
    print_board(board)
    if check_winner(board, X):
        print("AI wins!")
        print("-------Thanks for playing TIC-TAC-TOE Game-------")
    elif check_winner(board, O):
        print("You win!")
        print("-------Thanks for playing TIC-TAC-TOE Game-------")
    else:
        print("It's a draw!")
        print("-------Thanks for playing TIC-TAC-TOE Game-------")

if __name__ == "__main__":
    main()
