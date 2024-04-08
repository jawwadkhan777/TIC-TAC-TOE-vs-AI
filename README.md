# Tic-Tac-Toe AI Documentation

## Introduction:

This documentation provides a comprehensive guide for understanding and implementing a Tic-Tac-Toe AI that plays against a human player. The AI player is designed to use the Minimax algorithm with Alpha-Beta Pruning to make optimal moves and become unbeatable.

## Features:

- Tic-Tac-Toe game implementation.
- Unbeatable AI player using Minimax algorithm with Alpha-Beta Pruning.
- Interactive gameplay against a human player.
- Visual representation of the game board.

## Requirements:

- Python (programming language)
- Text editor or integrated development environment (IDE)
- Basic understanding of Python programming language
- Knowledge of Minimax algorithm with Alpha-Beta Pruning

## Explanation:

### Game Representation:
The Tic-Tac-Toe board is represented as a 3x3 grid using a 2D list.

### Print Board Function:
The `print_board` function prints the current state of the Tic-Tac-Toe board.

### Winning Conditions:
The `check_winner` function checks if a player has won the game.

### Game Over Condition:
The `game_over` function checks if the game is over due to a win or draw.

### Evaluation Function:
The `evaluate` function evaluates the current state of the board for the Minimax algorithm.

### Minimax Algorithm:
The `minimax` function implements the Minimax algorithm with Alpha-Beta Pruning to determine the optimal move for the AI player.

### AI Move Function:
The `ai_move` function makes a move for the AI player based on the Minimax algorithm's output.

### Human Move Function:
The `human_move` function prompts the human player to make a move and updates the board accordingly.

### Main Function:
The `main` function initializes the game and alternates between AI and human player moves until the game is over.

## User Interactions:

### Game Start:
The game starts, and the player is informed that they are playing as 'O' against the AI player 'X'.

### Human Player's Move:
The human player makes their move by entering the row and column numbers for their move.

### AI Player's Move:
The AI player makes its move, and the updated board is displayed.

### Game Over:
The game ends with a win for either the AI player or the human player, or a draw if the board is filled without a winner.

## Conclusion:

This documentation provides a detailed explanation of the Tic-Tac-Toe AI project, including the implementation of the Minimax algorithm with Alpha-Beta Pruning. By following the provided code and explanations, users can understand...
