# Code Review: Coursemojo Take-Home (Tic-Tac-Toe)

## Summary

This is my response to Coursemojo’s take-home code review task for the Full Stack Engineer position. The project includes an annotated and improved version of the original `tictactoe.py` file.

I approached the task with three lenses:
1. **Functionality** – Ensuring correct and reliable behavior
2. **Style** – Improving readability and Pythonic expression
3. **Expandability** – Structuring the code to support future changes

---

## Structure

original/tictactoe.py → Original code
revised/tictactoe.py → My revised version
ai_transcript/ → ChatGPT discussion + feedback
review_notes.md → Optional extra notes (if needed)


---

## AI Usage

I used OpenAI’s ChatGPT-4 (gpt-4o model) to assist with:
- Reviewing specific functions for readability and logic
- Suggesting refactors for modularity and clarity
- Identifying edge cases and recommending validation logic

Chat transcript is included in `ai_transcript/chatgpt_review.pdf`.

---

## Key Improvements

### 🔧 Functionality
- Added validation for invalid or repeated moves
- Prevented out-of-range access on board
- Clearer win/draw detection logic

### ✨ Style
- Broke large functions into smaller, named helpers
- Improved variable naming for clarity
- Removed redundant conditions and nested blocks

### 🔮 Expandability
- Suggested (not implemented) class-based design for Game, Board, Player
- Commented on separation of game logic and CLI UI
