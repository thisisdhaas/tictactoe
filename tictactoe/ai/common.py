from utils import get_potential_wins
from utils import toggle_turn


def detect_threat(game_state, turn):
    for potential_win, coordinate in zip(*get_potential_wins(game_state, with_coordinates=True)):
        if potential_win.count(toggle_turn(turn)) == 2 and potential_win.count(' ') == 1:
            return coordinate[potential_win.index(' ')]
    return None


def detect_win(game_state, turn):
    for potential_win, coordinate in zip(*get_potential_wins(game_state, with_coordinates=True)):
        if potential_win.count(turn) == 2 and potential_win.count(' ') == 1:
            return coordinate[potential_win.index(' ')]
    return None
