from connectfour import *

# test args
test_board_1 = [
    0,0,0,0,0,0,1,
    2,0,0,0,0,0,2,
    2,0,0,0,0,0,2,
    2,0,0,0,0,0,2,
    1,0,0,0,0,0,1,
    1,0,0,0,0,1,1
]

test_board_2 = [
    0,0,0,0,0,0,1,
    2,0,0,0,0,0,2,
    2,0,0,2,0,0,2,
    2,0,0,1,1,0,2,
    1,0,2,1,2,0,1,
    1,0,1,1,1,1,1
]

test_board_3 = [
    0,0,0,0,0,0,1,
    2,0,0,0,0,0,2,
    2,1,0,2,0,0,2,
    2,1,0,1,1,0,2,
    2,1,2,1,2,0,1,
    1,1,1,1,1,1,1
]

test_board_4 = [
    0,0,0,0,0,0,1,
    2,0,0,0,0,0,2,
    2,1,0,2,0,0,2,
    2,1,0,1,1,0,2,
    2,1,2,2,2,2,1,
    1,1,1,1,1,1,1
]

def test_column_is_full():

    assert column_is_full(test_board_1, 0) == False
    assert column_is_full(test_board_1, 3) == False
    assert column_is_full(test_board_1, 6) == True

def test_get_open_slot_index():
    assert get_open_slot_index(test_board_1, 6) == None
    assert get_open_slot_index(test_board_1, 0) == 0
    assert get_open_slot_index(test_board_1, 1) == 36
    assert get_open_slot_index(test_board_1, 5) == 33

def test_play_move():
    final_state_1 = [
        2,0,0,0,0,0,1,
        2,0,0,0,0,0,2,
        2,0,0,2,0,0,2,
        2,0,0,1,1,0,2,
        1,0,2,1,2,0,1,
        1,0,1,1,1,1,1
    ]
    final_state_2 = [
        0,0,0,0,0,0,1,
        2,0,0,0,0,0,2,
        2,0,0,2,0,0,2,
        2,0,0,1,1,0,2,
        1,0,2,1,2,0,1,
        1,1,1,1,1,1,1
    ]
    final_state_3 = [
        0,0,0,0,0,0,1,
        2,0,0,0,0,0,2,
        2,0,0,2,2,0,2,
        2,0,0,1,1,0,2,
        1,0,2,1,2,0,1,
        1,0,1,1,1,1,1
    ]
    final_state_4 = [
        0,0,0,0,0,0,1,
        2,0,0,0,0,0,2,
        2,0,0,2,0,0,2,
        2,0,0,1,1,0,2,
        1,0,2,1,2,2,1,
        1,0,1,1,1,1,1
    ]

    assert play_move(list(test_board_2), 2, 0) == final_state_1
    assert play_move(list(test_board_2), 1, 1) == final_state_2
    # assert play_move(list(test_board_2), 2, 6) == None
    assert play_move(list(test_board_2), 2, 4) == final_state_3
    assert play_move(list(test_board_2), 2, 5) == final_state_4

def test_column_win_conditions():
    assert check_col_conditions(test_board_3, 2) == True
    assert check_col_conditions(test_board_3, 1) == True
    assert check_col_conditions(test_board_1, 1) == False

def test_row_win_conditions():

    assert check_row_conditions(test_board_3, 2) == False
    assert check_row_conditions(test_board_3, 1) == True
    assert check_row_conditions(test_board_4, 2) == True


if __name__ == "__main__":
    test_column_is_full()
    print('column_is_full functions correctly! ✅')

    test_get_open_slot_index()
    print('get_open_slot_index functions correctly! ✅')

    test_play_move()
    print('play_move functions correctly! ✅')

    test_column_win_conditions()
    print('column_win_conditions functions correctly! ✅')

    test_row_win_conditions()
    print('row_win_conditions functions correctly! ✅')