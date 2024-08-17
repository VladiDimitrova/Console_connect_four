ROWS = 6
COLS = 7

direction_mapper = {
    "up": (-1, 0),
    # "down": (1, 0),

    "right": (0, 1),
    # "left": (0, -1),

    "up_right": (-1, 1),
    # "down_left": (1, -1),

    "up_left": (-1, -1),
    # "down_right": (1, 1),

}


class FullColumnError(Exception):
    pass


board = []

for _ in range(ROWS):
    board.append([0 for el in range(COLS)])


def print_board(board):
    for data_row in board:
        print(data_row)


def is_valid_column_choice(col_number):
    return 1 <= col_number < COLS


def place_player_choice(board, col_index, player_num):
    for row_index in range(len(board) - 1, -1, -1):
        if board[row_index][col_index] == 0:
            board[row_index][col_index] = player_num
            return row_index, col_index
    raise FullColumnError

def is_valid_place(row_index, col_index):
    return 0<=row_index< ROWS and 0<= col_index<COLS

def check_direction(board, row_index, col_index, row_movement_index, col_movement_index, player_num):
    count = 0
    for i in range(1, 4):
        current_row_index = row_index + row_movement_index*i
        current_col_index = col_index + col_movement_index*i

        if not is_valid_place(current_row_index, current_col_index):
            break

        if board[current_row_index][current_col_index] != player_num:
            break
        count += 1
    return count


def check_opposite_direction(board, row_index, col_index, row_movement_index, col_movement_index, player_num):
    count = 0
    for i in range(1, 4):
        current_row_index = row_index - row_movement_index*i
        current_col_index = col_index - col_movement_index*i

        if not is_valid_place(current_row_index, current_col_index):
            break

        if board[current_row_index][current_col_index] != player_num:
            break

        count += 1
    return count


def is_winner(board, row_index, col_index, player_num):
    for direction, values in direction_mapper.items():
        result = 1
        row_movement_index, col_movement_index = values
        direction_count = check_direction(board, row_index, col_index, row_movement_index, col_movement_index,
                                          player_num)
        opposite_direction_count = check_opposite_direction(board, row_index, col_index, row_movement_index, col_movement_index,
                                                  player_num)

        result += (direction_count + opposite_direction_count)
        if result >= 4:
            return True
    return False


print_board(board)

turn = 1

while True:
    player_num = 1 if turn % 2 != 0 else 2
    try:
        selected_column = int(input(f"Player {player_num}, please choose a column: "))
    except ValueError:
        print(f'Please enter a valid digit')
        continue

    if not is_valid_column_choice(selected_column):
        print(f"Please select a number between 1 and {COLS}")
        continue
    selected_col_index = selected_column - 1
    try:
        current_row, current_col= place_player_choice(board, selected_col_index, player_num)
    except FullColumnError:
        print("This column is full, please select another one with available space")
        continue

    if is_winner(board, current_row, current_col, player_num):
        print(f"Winner!!! Player {player_num} you won!")
        break

    print_board(board)
    turn += 1

print(board)
