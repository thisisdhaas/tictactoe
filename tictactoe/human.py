from ai import AI_DIFFICULTY


def get_input(prompt, choices, choices_readable):
    def _input(msg):
        ret = raw_input(prompt)
        if ret == 'q':
            exit()
        return ret
    data = _input(prompt).strip().lower()
    while data not in choices:
        error_message = 'Please enter %s: ' % choices_readable
        data = _input(error_message).strip().lower()
    return data


def get_human_move(game_state, turn):
    '''Human'''
    def _get_move():
        cols = ['a', 'b', 'c']
        col = get_input(
            'Enter the column you wish to choose (A, B, or C): ',
            cols,
            '"A", "B", or "C"')
        col = cols.index(col)

        row = get_input(
            'Enter the row you wish to choose (1, 2, or 3): ',
            ['1', '2', '3'],
            '"1", "2", or "3"')
        row = int(row) - 1

        return row, col

    row, col = _get_move()
    while game_state[row][col] != ' ':
        print ''
        print 'That square is already taken! Please choose a different square.'
        row, col = _get_move()
    return row, col


def get_ai_func():
    ai_func = get_input(
        'What level of difficulty do you want to play at? (1 - 4): ',
        ['1', '2', '3', '4'],
        'a number between 1 and 4')
    return AI_DIFFICULTY[int(ai_func)]


def get_yesno_input(prompt):
    return get_input(
        prompt + ' (y/n): ',
        ['y', 'yes', 'n', 'no'],
        '"y" or "n"'
    ) in ['y', 'yes']


def get_two_player():
    return not get_yesno_input('Do you want to play against the computer?')


def get_move_first():
    return get_yesno_input('Do you want to go first?')


def play_another():
    return get_yesno_input('Do you want to play again?')
