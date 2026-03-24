import random
from connectfour import check_win_conditions, game_is_over, get_open_slot_index, play_move

def random_player_fn(board, player):
    num_cols = 7
    valid_moves = [i for i in range(num_cols) if board[i] == 0]
    if len(valid_moves) == 0:
        return None
    else:
        return random.choice(valid_moves)

def evaluation_function(board, player):
    game_win_result = check_win_conditions(board)
    board_is_full = 0 not in {board[i] for i in range(7)} # assumes gravity rules for dropping game pieces are obeyed

    if game_win_result == player:
        return 1000000000
    elif game_win_result != 0:
        return -1000000000
    elif board_is_full:
        return 0
        
    board_score = 0

    # consider center column advantage (more possible ways to get 4 in a row available)

    center_count = 0
    center_index = 38
    for i in range(7):
        if board[center_index] == player:
            center_count += 1
        elif board[center_index] != 0:
            center_count -= 1
        center_index -= 7

    board_score += center_count * 3
    return board_score

def minimax(board, eval_fn, whose_turn, who_am_i, num_plys):

    def alpha_beta_minimax(board, eval_fn, whose_turn, who_am_i, num_plys, alpha=float("-inf"), beta=float("inf")):

        if (num_plys == 0) or game_is_over(board):
            return eval_fn(board, who_am_i)

        valid_moves = [i for i in range(7) if board[i] == 0]
        opposing_player = 2 if whose_turn == 1 else 1
        best_value = float("-inf") if whose_turn == who_am_i else float("inf")

        for move in valid_moves:
            if alpha >= beta:
                return best_value
            
            move_slot_index = get_open_slot_index(board, move)
            play_move(board, whose_turn, move)
            child_value = alpha_beta_minimax(board, eval_fn, opposing_player, who_am_i, num_plys - 1, alpha, beta)
            
            if whose_turn == who_am_i:
                best_value = max(best_value, child_value)
                alpha = max(alpha, child_value)
            else:
                best_value = min(best_value, child_value)
                beta = min(beta, child_value)

            board[move_slot_index] = 0
        return best_value
    return alpha_beta_minimax(board, eval_fn, whose_turn, who_am_i, num_plys)

    
def initialize_my_player_fn(num_plys=4):
    
    def my_player_fn(board, player):
        num_cols = 7
        valid_moves = [i for i in range(num_cols) if board[i] == 0]
        if len(valid_moves) == 0:
            return None
        
        opposing_player = 2 if player == 1 else 1

        best_move = None
        best_board_score = float("-inf")

        for move in valid_moves:
            move_slot_index = get_open_slot_index(board, move)
            play_move(board, player, move)

            move_score = minimax(board, evaluation_function, opposing_player, player, num_plys - 1)
            if move_score > best_board_score:
                best_board_score = move_score
                best_move = move

            board[move_slot_index] = 0
        
        return best_move
    
    return my_player_fn
