# Overall, the code is clear and functional, and I appreciate the flexibility for variable board sizes. 
# I’ve made a few suggestions to improve modularity, readability, and edge case handling. 
# Most changes are stylistic or minor structural tweaks, aimed at making the code easier to test and extend.

BLANK_SQUARE = '_'

# Suggestion: Introduced a simple Player class to encapsulate player-related data.
# This improves separation of concerns and makes it easier to manage future features
# such as AI behavior, score tracking, or customizable player markers.

class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
        self.score = 0  # Optional: track number of wins

    def __str__(self):
        return self.name

# Suggestion: Introduced a dedicated Board class to encapsulate board state and related operations.
# This cleanly separates game state from game logic and presentation, making the code easier to maintain, test,
# and extend. Future features like undo/redo, custom board rendering, or saving/loading game state 
# can now be added more easily by modifying the Board class without touching the rest of the game logic.

class Board:
    def __init__(self, size):
        self.size = size
        self.cells = [BLANK_SQUARE] * (size * size)

    def get(self, row, col):
        return self.cells[row * self.size + col]

    def set(self, row, col, marker):
        self.cells[row * self.size + col] = marker

    def is_empty(self, row, col):
        return self.get(row, col) == BLANK_SQUARE

    def is_full(self):
        return BLANK_SQUARE not in self.cells

    def reset(self):
        self.cells = [BLANK_SQUARE] * (self.size * self.size)

    # Suggestion: Extracted win-checking logic into helper methods to reduce repetition 
    # and make it easier to support rule variants (e.g., "4 in a row" on 5x5 boards).
    
    def get_lines(self):
        lines = []

        for i in range(self.size):
            lines.append([self.get(i, j) for j in range(self.size)])  # row
            lines.append([self.get(j, i) for j in range(self.size)])  # column

        lines.append([self.get(i, i) for i in range(self.size)])  # main diagonal
        lines.append([self.get(i, self.size - i - 1) for i in range(self.size)])  # anti-diagonal

        return lines

    # Suggestion: Updated board printing to include coordinate labels,
    # making it easier for players to reference rows/columns when entering moves.
    # This improves usability especially for larger boards.

    def print(self):
        print("\n  ", end="")
        for col in range(1, self.size + 1): # Row label (1-based)
            print(f"{col} ", end="")
        print()

        for row in range(self.size):
            print(f"{row + 1} ", end="")
            for col in range(self.size):
                print(f"{self.get(row, col)} ", end="")
            print()
        print()


class TicTacToe:
    def __init__(self, board_size=3):
        self.board = Board(board_size)
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.current_player = self.player1

    def check_winner(self):
        for line in self.board.get_lines():
            if line.count(line[0]) == self.board.size and line[0] != BLANK_SQUARE:
                return line[0]
        return None

    def check_draw(self):
        return self.board.is_full()

    def reset(self):
        self.board.reset()
        self.current_player = self.player1        

    # Suggestion: Refactored input and validation into three focused methods:
    # - `input_move()` handles raw user input only, with minimal responsibility
    # - `is_move_valid()` performs all validation checks and prints user-friendly error messages
    # - `make_move()` now encapsulates the full turn interaction loop, ensuring only valid moves are applied
    # 
    # This separation of concerns improves readability, testability (e.g., `is_move_valid()` can be unit tested),
    # and makes the game flow logic easier to reason about. Encapsulating the full move loop inside `make_move()`
    # also simplifies the main game loop.

    def input_move(self):   # Switched from 0-indexed to 1-based (row, col) input format.
        raw = input(f"{self.current_player}'s turn. Enter your move as row,col (1-based): ").strip()
        try:
            row_str, col_str = raw.split(',')
            return int(row_str) - 1, int(col_str) - 1
        except ValueError:
            return None  # Still return None for bad parsing
    
    def is_move_valid(self, move):
        if move is None:
            print("Invalid input! Please enter row and column as two numbers separated by a comma (e.g., 1,3).")
            return False
        row, col = move
        if not (0 <= row < self.board.size and 0 <= col < self.board.size):
            print(f"Invalid move! Row and column must be between 1 and {self.board.size}.")
            return False
        if not self.board.is_empty(row, col):
            print("Invalid move! That spot is already taken.")
            return False
        return True
    
    def make_move(self):
        while True:
            move = self.input_move()
            if self.is_move_valid(move):
                row, col = move
                self.board.set(row, col, self.current_player.marker)
                self.current_player = (
                    self.player1 if self.current_player == self.player2 else self.player2
                )
                break


# Main program starts here
if __name__ == "__main__":  # Added this line to avoid running when being tested.
    
    # Helper function to repeatedly prompt for a valid board size (>= 3)
    def prompt_board_size(): 
        while True:
            try:    # Set minimum board size to 3 for meaningful gameplay
                size = int(input("What board size do you want? (minimum 3): "))
                if size >= 3:
                    return size
                print("Board size must be at least 3.")
            except ValueError:
                print("Please enter a valid number.")

    board_size = prompt_board_size()
    game = TicTacToe(board_size=board_size)

    while True: # Added loop to allow replay and ask board size every time
        # Game loop
        while game.check_winner() is None and not game.check_draw():
            game.board.print()
            game.make_move()

        game.board.print()

        # Suggestion: Added a message to announce the result instead of exiting silently
        winner = game.check_winner()
        if winner:
            print(f"🎉 Player {winner} wins!")
        else:
            print("🤝 It's a draw!")
        
        # Suggestion: Added replay prompt after game end to improve user experience.
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            break
        
        same_size = input("Same board size? (y/n): ").strip().lower()
        if same_size != 'y':
            board_size = prompt_board_size()
            game = TicTacToe(board_size=board_size)  # recreate
        else:
            game.reset()  # reuse existing instance
