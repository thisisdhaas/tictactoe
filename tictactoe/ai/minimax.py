import sys
from copy import deepcopy
from utils import apply_move
from utils import get_possible_moves
from utils import get_winner
from utils import toggle_turn


def optimal(game_state, turn):
    '''Minimax-Optimal Algorithm'''
    sys.stdout.write('Computer is thinking... Progress: 0.00%\r')
    sys.stdout.flush()

    # Run the minimax algorithm on the full remaining game tree
    best_score, best_move, best_move_depth = minimax(game_state, turn, turn, top=True)
    return best_move


def minimax(game_state, turn, maximizer_turn, round_num=0, top=False):
    possible_moves = get_possible_moves(game_state)
    if not possible_moves or get_winner(game_state)[0] is not None:
        return _score(game_state, maximizer_turn), None, round_num

    if turn == maximizer_turn:
        best = -2  # Lower than lowest possible score.
        best_move = None
        best_move_depth = 10  # Larger than deepest possible tree.
        for i, move in enumerate(possible_moves):
            move_score, _, move_depth = minimax(
                _simulate_move(game_state, move, turn), toggle_turn(turn), maximizer_turn, round_num + 1)

            # break ties by preferring faster wins
            is_faster = move_depth < best_move_depth
            if move_score > best or (move_score == best and is_faster):
                best_move = move
                best = move_score
                best_move_depth = move_depth

            # Print a progress bar at the top level
            if top:
                progress = 100. * (i + 1.) / len(possible_moves)
                sys.stdout.write('Computer is thinking... Progress: %.02f%%\r' % progress)
                sys.stdout.flush()
        return (best, best_move, best_move_depth)

    else:
        best = 2  # Higher than highest possible score
        best_move = None
        best_move_depth = 10  # Larger than deepest possible tree.
        for move in possible_moves:
            move_score, _, move_depth = minimax(
                _simulate_move(game_state, move, turn), toggle_turn(turn), maximizer_turn, round_num + 1)

            # break ties by preferring faster wins
            is_faster = move_depth < best_move_depth
            if move_score < best or (move_score == best and is_faster):
                best_move = move
                best = move_score
                best_move_depth = move_depth
        return (best, best_move, best_move_depth)


def _score(game_state, our_turn):
    winner, _ = get_winner(game_state)
    assert winner
    if winner == our_turn: return 1
    if winner == toggle_turn(our_turn): return -1
    if winner == 'Tie': return -0.5


def _simulate_move(game_state, move, turn):
    new_state = deepcopy(game_state)
    apply_move(new_state, move, turn)
    return new_state
