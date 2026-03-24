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


def get_open_slot_index(board, column):
    """
    Given a column and a board, return the position a game piece should fall into after being placed.

    Args:
        board (list[int]): a list of all positions in a 6 by 7 board, with all indexes having the value 0, 1, or 2.
        column (int): integer that represents the column to drop the game piece (0-6)
    Return:
        None if column is full. int representing the dropped game piece if the column is not full
    """
    current_col_pos = column + 35

    while current_col_pos >= column:
        if board[current_col_pos] == 0:
            return current_col_pos
        current_col_pos -= 7

    return None

def play_move(board, player, column):
    """
    Given a column, board, and player, return updated board after player has dropped a game piece.

    Args:
        board (list[int]): a list of all positions in a 6 by 7 board, with all indexes having the value 0, 1, or 2.
        column (int): integer that represents the column to drop the game piece (0-6)
        player (int): an integer represented the player dropping a game piece (1-2)
    Return:
        board list[int]) representing the updated board after player dropped a game piece
    """
    next_move_pos = get_open_slot_index(board, column)

    if next_move_pos is not None:
        board[next_move_pos] = player
        return board
    else:
        raise Exception("Column is full!")

def check_win_conditions(board):
    raise NotImplementedError("fill this in!")

# def check_diagonal_conditions(board, player):

def check_col_conditions(board, player):
    """
    Given a board and a player, check each col to see if a player
    has 4 checkers in a col.

    Args: 
        board (list[int]): list of board positions with 0s, 1s, 2s
        player (int): represents the player (1 or 2)
    Return:
        True or False if player has 4 checkers in a column
    """
    init_pos_1, init_pos_2, init_pos_3, init_pos_4 = 14, 21, 28, 35
    player_has_won = False

    for i in range(7):
        base_1 = init_pos_1 + 1 * i
        base_2 = init_pos_2 + 1 * i
        base_3 = init_pos_3 + 1 * i
        base_4 = init_pos_4 + 1 * i

        for j in range(3):
            curr_pos_1 = base_1 - 7 * j
            curr_pos_2 = base_2 - 7 * j
            curr_pos_3 = base_3 - 7 * j
            curr_pos_4 = base_4 - 7 * j
            if (player == board[curr_pos_1] and
                board[curr_pos_1] == board[curr_pos_2] and  
                board[curr_pos_2] == board[curr_pos_3] and
                board[curr_pos_3] == board[curr_pos_4]):
                player_has_won = True
                break
        if player_has_won:
            break
    return player_has_won

def check_row_conditions(board, player):
    """
    Given a board and a player, check each row to see if a player
    has 4 checkers in a row.

    Args: 
        board (list[int]): list of board positions with 0s, 1s, 2s
        player (int): represents the player (1 or 2)
    Return:
        True or False if player has 4 checkers in a row
    """
    init_pos_1, init_pos_2, init_pos_3, init_pos_4 = 0, 1, 2, 3
    player_has_won = False

    for i in range(6):
        base_1 = init_pos_1 + 7 * i
        base_2 = init_pos_2 + 7 * i
        base_3 = init_pos_3 + 7 * i
        base_4 = init_pos_4 + 7 * i

        for j in range(4):
            curr_pos_1 = base_1 + 1 * j
            curr_pos_2 = base_2 + 1 * j
            curr_pos_3 = base_3 + 1 * j
            curr_pos_4 = base_4 + 1 * j
            # print(curr_pos_1, curr_pos_2, curr_pos_3, curr_pos_4)
            if (player == board[curr_pos_1] and
                board[curr_pos_1] == board[curr_pos_2] and  
                board[curr_pos_2] == board[curr_pos_3] and
                board[curr_pos_3] == board[curr_pos_4]):
                player_has_won = True
                break
        if player_has_won:
            break
    return player_has_won


