import subprocess
from utils import get_winner


cell_width= 10
box_height= 3
square_size = 3


def clear():
    subprocess.check_call('clear')


def print_title():
    title = "DAN'S CRAZY TIC-TAC-TOE"
    board_width = cell_width * square_size + square_size + 1
    print '=' * board_width
    print center_string(title, board_width)
    print '=' * board_width
    print ''
    print 'Press "q" to exit at any time.'
    print ''


def center_padding(item_width, total_width):
    return (total_width - item_width) / 2 if item_width < total_width else 0


def center_string(string, length, after=False):
    padding = ' ' * center_padding(len(string), length)
    return padding + string + padding if after else padding + string


def draw_board(game_state):

    def print_col_nums():
        cols = ['A', 'B', 'C']
        padding = ' ' * center_padding(1, cell_width)
        for i in range(square_size):
            print ' ' + padding + cols[i] + padding,
        print ''

    def print_border():
        line = '-' * cell_width
        print ('*' + line) * square_size + '*'

    def compute_victory_char(i, j, winner_coords):
        if winner_coords is not None:
            if (i, j) in winner_coords:
                if winner_coords[0][0] == winner_coords[1][0]:
                    return '-'
                elif winner_coords[0][1] == winner_coords[1][1]:
                    return '|'
                elif winner_coords[0][1] > winner_coords[1][1]:
                    return '/'
                else:
                    return '\\'
        return ' '

    def print_empty_line(winner, row_idx, before):
        row = ''
        for j in range(square_size):
            victory_char = compute_victory_char(row_idx, j, winner)
            if victory_char == '|':
                space = center_string(victory_char, cell_width, after=True) + ' '
            elif victory_char == '\\':
                offset = 2 if before else 6
                space = ' ' * cell_width
                space = space[:offset] + victory_char + space[offset + 1:]
            elif victory_char == '/':
                offset = 6 if before else 2
                space = ' ' * cell_width
                space = space[:offset] + victory_char + space[offset + 1:]
            else:
                space = ' ' * cell_width
            row += '|' + space
        print row + '|'

    def print_item(item, pad_char):
        padding = pad_char * (center_padding(1, cell_width) - 1)
        front_padding = padding + ' '
        back_padding = ' ' + padding
        print '|' + front_padding + item + back_padding,

    def print_row(row_state, row_idx, winner_coords):
        num_blank_lines = center_padding(1, box_height)
        assert num_blank_lines == 1, "Only works for box_height of 3!"
        print_empty_line(winner_coords, row_idx, before=True)
        for col_idx, item in enumerate(row_state):
            victory_char = compute_victory_char(row_idx, col_idx, winner_coords)
            pad_char = '-' if victory_char == '-' else ' '
            print_item(item, pad_char)
        print '| ', row_idx + 1
        print_empty_line(winner_coords, row_idx, before=False)

    winner, winner_coords = get_winner(game_state)
    print_col_nums()
    for i, row_state in enumerate(game_state):
        print_border()
        print_row(row_state, i, winner_coords)
    print_border()


def print_status(turn):
    print "It is team", turn + "'s move."
    print ''


def redraw(game_state):
    clear()
    print_title()
    draw_board(game_state)
