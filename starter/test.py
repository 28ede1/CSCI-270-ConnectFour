from connectfour import *

# test args

test_board_1 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0
]

test_board_2 = [
    0,0,2,0,0,0,0,
    0,0,1,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,1,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,1,0,0,0,0
]

test_board_3 = [
    0,0,0,0,0,0,0,
    0,0,0,2,0,0,0,
    0,1,0,1,0,0,0,
    2,2,1,2,0,0,0,
    1,1,2,1,0,0,0,
    2,2,1,2,1,0,0
]

test_board_4 = [
    0,0,0,0,0,0,0,
    1,0,0,0,0,0,0,
    2,0,0,0,0,0,0,
    1,0,2,0,0,0,0,
    2,0,1,0,0,0,0,
    1,2,2,0,0,0,0
]

test_board_5 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,1,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,1,0,0,0,0
]

test_board_6 = [
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    1,1,1,1,0,0,0
]

test_board_7= [
    0,0,0,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,2,0,0,0,0,
    0,0,2,0,0,0,0,
    1,1,1,0,0,0,0
]

test_board_8 = [
    1,2,1,2,1,2,1,
    2,1,2,1,2,1,2,
    1,2,1,2,1,2,1,
    2,1,2,1,2,1,2,
    1,2,1,2,1,2,1,
    2,1,2,1,2,1,2
]


def test_get_open_slot_index():

    # Test that for an empty board, all dropped game pieces should end up on the last row
    # Test that for an full board, None is always returned (indicated that the column to drop a piece into is full)
    current_open_slot_index = 35
    for i in range(7):
        assert get_open_slot_index(test_board_1, i) == current_open_slot_index
        assert get_open_slot_index(test_board_8, i) == None
        current_open_slot_index += 1

    assert get_open_slot_index(test_board_3, 0) == 14
    assert get_open_slot_index(test_board_4, 1) == 29
    assert get_open_slot_index(test_board_5, 2) == 9
    assert get_open_slot_index(test_board_2, 2) == None

def test_play_move():
    final_state_1 = [
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,1,0
    ]

    final_state_2 = [
        0,0,0,1,0,0,0,
        0,0,0,2,0,0,0,
        0,1,0,1,0,0,0,
        2,2,1,2,0,0,0,
        1,1,2,1,0,0,0,
        2,2,1,2,1,0,0
    ]
    final_state_3 = [
        0,0,0,0,0,0,0,
        0,0,2,0,0,0,0,
        0,0,2,0,0,0,0,
        0,0,1,0,0,0,0,
        0,0,2,0,0,0,0,
        0,0,1,0,0,0,0
    ]

    assert play_move(list(test_board_1), 1, 5) == final_state_1
    assert play_move(list(test_board_3), 1, 3) == final_state_2
    assert play_move(list(test_board_5), 2, 2) == final_state_3

def test_column_win_conditions():
    assert check_col_conditions(test_board_7, 2) == True
    assert check_col_conditions(test_board_7, 1) == False

    assert check_col_conditions(test_board_8, 2) == False
    assert check_col_conditions(test_board_8, 1) == False

def test_row_win_conditions():

    assert check_row_conditions(test_board_6, 1) == True
    assert check_row_conditions(test_board_6, 2) == False

    assert check_row_conditions(test_board_8, 2) == False
    assert check_row_conditions(test_board_8, 1) == False


if __name__ == "__main__":
    test_get_open_slot_index()
    print('get_open_slot_index functions correctly! ✅')

    test_play_move()
    print('play_move functions correctly! ✅')

    test_column_win_conditions()
    print('column_win_conditions functions correctly! ✅')

    test_row_win_conditions()
    print('row_win_conditions functions correctly! ✅')