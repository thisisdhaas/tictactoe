from random import choice
from utils import get_possible_moves
from ai.common import detect_threat
from ai.common import detect_win


def random(game_state, turn):
    '''Random Algorithm'''
    possible_moves = get_possible_moves(game_state)
    return choice(possible_moves)


def random_blocker(game_state, turn):
    '''Defensive Algorithm'''
    threat_coordinate = detect_threat(game_state, turn)
    if threat_coordinate is not None:
        return threat_coordinate
    return random(game_state, turn)


def random_winner(game_state, turn):
    '''Offensive Algorithm'''
    win_coordinate = detect_win(game_state, turn)
    if win_coordinate is not None:
        return win_coordinate
    return random_blocker(game_state, turn)
