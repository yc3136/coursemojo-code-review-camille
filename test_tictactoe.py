from tictactoe import TicTacToe, BLANK_SQUARE

def test_horizontal_win():
    game = TicTacToe(board_size=3)
    game.board.cells = [
        "X", "X", "X",
        BLANK_SQUARE, BLANK_SQUARE, BLANK_SQUARE,
        BLANK_SQUARE, BLANK_SQUARE, BLANK_SQUARE,
    ]
    assert game.check_winner() == "X"

def test_vertical_win():
    game = TicTacToe(board_size=3)
    game.board.cells = [
        "O", BLANK_SQUARE, BLANK_SQUARE,
        "O", BLANK_SQUARE, BLANK_SQUARE,
        "O", BLANK_SQUARE, BLANK_SQUARE,
    ]
    assert game.check_winner() == "O"

def test_diagonal_win_lr():
    game = TicTacToe(board_size=3)
    game.board.cells = [
        "X", BLANK_SQUARE, BLANK_SQUARE,
        BLANK_SQUARE, "X", BLANK_SQUARE,
        BLANK_SQUARE, BLANK_SQUARE, "X",
    ]
    assert game.check_winner() == "X"

def test_diagonal_win_rl():
    game = TicTacToe(board_size=3)
    game.board.cells = [
        BLANK_SQUARE, BLANK_SQUARE, "O",
        BLANK_SQUARE, "O", BLANK_SQUARE,
        "O", BLANK_SQUARE, BLANK_SQUARE,
    ]
    assert game.check_winner() == "O"

def test_draw():
    game = TicTacToe(board_size=3)
    game.board.cells = [
        "X", "O", "X",
        "O", "X", "O",
        "O", "X", "O",
    ]
    assert game.check_winner() is None
    assert game.check_draw() is True

def test_reset():
    game = TicTacToe(board_size=3)
    game.board.cells = [
        "X", "X", "X",
        "O", "O", "X",
        "O", "X", "O",
    ]
    game.reset()
    assert game.board.cells == [BLANK_SQUARE] * 9
    assert game.current_player.name == "Player 1"

def test_is_move_valid():
    game = TicTacToe(board_size=3)

    # Occupy a spot manually
    game.board.set(0, 0, "X")

    # Case 1: None input (bad parse)
    assert game.is_move_valid(None) is False

    # Case 2: Out of bounds (row too large)
    assert game.is_move_valid((5, 1)) is False

    # Case 3: Out of bounds (negative col)
    assert game.is_move_valid((1, -1)) is False

    # Case 4: Occupied cell
    assert game.is_move_valid((0, 0)) is False

    # Case 5: Valid empty cell
    assert game.is_move_valid((1, 1)) is True


# Run tests
test_horizontal_win()
test_vertical_win()
test_diagonal_win_lr()
test_diagonal_win_rl()
test_draw()
test_reset()
test_is_move_valid()
print("✅ All tests passed.")
