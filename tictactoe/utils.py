def get_potential_wins(game_state, with_coordinates=False):
    potential_wins = (
        game_state +            # The rows

        zip(*game_state) +      # The columns

        [                       # The diagonals
            (game_state[0][0],  # Left-to-right diagonal
             game_state[1][1],
             game_state[2][2]),

            (game_state[0][2],  # Right-to-left diagonal
             game_state[1][1],
             game_state[2][0])
        ]
    )
    if not with_coordinates:
        return potential_wins
    else:
        coordinates = (
            # Rows
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],

            # Columns
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],

            # Diagonals
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)],
        )
        return potential_wins, coordinates


def get_winner(game_state):
    potential_wins = get_potential_wins(game_state, with_coordinates=True)

    for potential_win, coordinates in zip(*potential_wins):
        if potential_win.count('O') == 3:
            return 'O', coordinates
        if potential_win.count('X') == 3:
            return 'X', coordinates

    # Check for tie
    if ' ' not in [symbol for row in game_state for symbol in row]:
        return 'Tie', None
    return None, None


def apply_move(game_state, move, symbol):
    row, col = move
    assert game_state[row][col] == ' '
    game_state[row][col] = symbol


def toggle_turn(turn):
    return 'X' if turn == 'O' else 'O'


def get_possible_moves(game_state):
    possible_moves = []
    for row_num, row in enumerate(game_state):
        for col_num, symbol in enumerate(row):
            if symbol == ' ':
                possible_moves.append((row_num, col_num))
    return possible_moves
