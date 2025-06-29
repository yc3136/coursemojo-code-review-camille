# Tic-Tac-Toe Code Review  
Coursemojo Take-Home Task  
Author: Camille Cao

## Overview

This folder contains my response to Coursemojo’s take-home code review assignment for the Full Stack Engineer position. I approached the task as a collaborative teammate would: reviewing the original logic, testing for robustness, and improving the code with a focus on clarity, user experience, and expandability — all while documenting the rationale behind my changes.

---

## Files Included

- `tictactoe.py`: Revised implementation of the Tic-Tac-Toe game
- `test_tictactoe.py`: Manual unit tests for win condition and draw logic
- `README.md`: This file, summarizing my approach and improvements
- `chatgpt_transcript.pdf`: Full transcript of AI assistance


---

## Key Improvements

### Functionality
- Replaced raw position input with intuitive **(row, col)** coordinates (1-based)
- Added clear **winner/draw messaging** at game end
- Gracefully handled invalid input, including out-of-bounds positions, wrong formats, and already-taken squares
- Added replay loop with option to play again after each round
- Added flexible replay flow: players can choose to replay with the same or a different board size

### Style & Usability
- Updated board printing with **coordinate labels** for improved navigation
- Replaced magic values with clearly named constants (e.g., `BLANK_SQUARE`)
- Used a dedicated **`Player` class** to store player name, marker, and enable future metadata like scores or AI type

### Code Structure & Readability
- Modularized win-checking logic using helper methods (e.g., `get_lines()`)
- Introduced `if __name__ == "__main__"` guard to support testing and import safety
- Reformatted user prompts and error messages for a clearer player experience
- Extracted `prompt_board_size()` to encapsulate validation logic and improve reusability
- Refactored user input and validation logic into three distinct methods to make future testing or feature additions easier.
  - `input_move()` handles raw input parsing only
  - `is_move_valid()` encapsulates all validation rules and feedback
  - `make_move()` now drives the full input-validate-apply loop

### Expandability
- Introduced a dedicated **`Board` class** to manage board state and operations separately from game logic
- Cleanly separates concerns across classes: `Board` handles state, `Player` encapsulates metadata, and `TicTacToe` drives the game flow
- Architecture now supports future features like custom emojis, AI opponents, score tracking, undo/redo, or save/load functionality


---

### Future Considerations

While the current implementation fulfills the assignment requirements, I considered a number of possible enhancements that could improve the game’s robustness and user experience. I intentionally chose not to implement these in order to stay within the scope of a peer-level code review. These ideas include:

- Allowing users to **quit the game at any point** by typing a universal exit command (e.g., `q` or `exit`)
- Providing a way for a player to **forfeit the game**, immediately granting victory to the opponent
- Randomizing or toggling **which player starts first**, rather than always defaulting to Player 1
- Allowing players to **enter their names** at the start for personalized turns and results
- Prompting each player to **choose a custom marker**, including support for emojis (e.g., 🐶 vs 🐱)
- Maintaining a **running scoreboard** across rounds to track total wins per player

These ideas reflect areas for further iteration in a production setting or future UX-focused extensions.


---

## AI Tools Used

I used **OpenAI’s ChatGPT (gpt-4o model)** as a technical assistant during this review. I used it to:
- Validate specific pieces of logic
- Refactor repetitive sections (like win checking)
- Review clarity and testability of input-handling logic
- Guide comments to match professional team collaboration tone


---

## Testing

While this is not a full test suite, I created a `test_tictactoe.py` file with basic assertions for:
- Win detection in all directions (horizontal, vertical, both diagonals)
- Draw detection on a full board
- Game board reset functionality and player state reset
- Rejection of invalid moves, including None, out-of-bounds inputs, and occupied cells passed to `is_move_valid()`

These tests demonstrate the correctness of the revised win logic, turn tracking, and board state handling.

To run the tests, use:

```bash
python3 test_tictactoe.py


---

Thank you for reviewing!