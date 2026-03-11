def stringify_board(board):
    """Returns a nice string representation of a Connect Four board."""

    def checker(board_value):
        if board_value == 0:
            return "⚪"
        elif board_value == 1:
            return "🔴"
        elif board_value == 2:
            return "🟡"
        else:
            raise Exception(f"Invalid connect-four board value: {board_value}")

    mapped = [checker(val) for val in board]
    structured = ["".join(mapped[i : i + 7]) for i in range(0, 42, 7)]
    return "\n".join(structured)


def print_board(board):
    """Prints a nice string representation of a Connect Four board."""
    print(stringify_board(board))


def check_win_conditions(board):
    raise NotImplementedError("fill this in!")

def column_is_full(board, column):
    """
    Given a column number and board list, return true if the column is full (if the entire column is all 1s/2s).
    Assumes that the column obeys laws of gravity (that all non-zero items in a column are pushed to bottom of the column)

    Args:
        board (list[int]): list of board positions with 0s, 1s, and 2s integers
        column (int): integer that represents the column to drop the game piece (0-6)
    Return:
        True if the the selected column is nonzero, False if not.
    """

    for i in range(column, 42, 7):
        if board[i] == 0:
            return False
    return True

def get_open_slot_index(board, column):
    """
    Given a column number and board list, return None if the column selected is full. Else, return the topmost position to
    drop a game piece into.

    Args:
        board (list[int]): list of board positions with 0s, 1s, and 2s integers
        column (int): integer that represents the column to drop the game piece (0-6)
    Return:
        None if board is full, and int position if not
    """

    if column_is_full(board, column):
        return None
    
    current_col_pos = column

    # while the NEXT index is within range and next index is 0

    while current_col_pos + 7 <= 41 and board[current_col_pos + 7] == 0:
        current_col_pos += 7

    return current_col_pos

def play_move(board, player, column):
    next_move_pos = get_open_slot_index(board, column)

    if next_move_pos is not None:
        board[next_move_pos] = player
        return board
    else:
        raise Exception("Column is full!")
