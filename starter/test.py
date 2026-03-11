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



if __name__ == "__main__":
    test_column_is_full()
    print('test_column_is_full functions correctly! ✅')

    test_get_open_slot_index()
    print('test_get_open_slot_index functions correctly! ✅')

    test_play_move()
    print('test_play_move functions correctly! ✅')