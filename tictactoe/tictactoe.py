from draw import clear
from draw import print_status
from draw import print_title
from draw import redraw
from human import get_ai_func
from human import get_human_move
from human import get_move_first
from human import get_two_player
from human import play_another
from utils import apply_move
from utils import get_winner
from utils import toggle_turn


def play_game(player_x_func, player_o_func):
    game_state = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
    turn = 'X'
    redraw(game_state)
    winner, _ = get_winner(game_state)
    while not winner:
        print_status(turn)
        if turn == 'X':
            move = player_x_func(game_state, turn)
        else:
            move = player_o_func(game_state, turn)
        apply_move(game_state, move, turn)
        redraw(game_state)
        turn = toggle_turn(turn)
        winner, _ = get_winner(game_state)
    if winner in ['X', 'O']:
        print winner, 'is victorious!'
    else:
        print "It's a tie!"
    print ''
    return winner


def main():
    # Choose between ai and 2-player.
    clear()
    print_title()
    two_player = get_two_player()
    if two_player:
        player_x_func = get_human_move
        player_o_func = get_human_move
    else:
        ai_func = get_ai_func()
        move_first = get_move_first()
        player_x_func = get_human_move if move_first else ai_func
        player_o_func = ai_func if move_first else get_human_move

    # Run games until the player is done.
    play_again = True
    standings = {'X': 0, 'O': 0, 'Tie': 0}
    try:
        while play_again:
            winner = play_game(player_x_func, player_o_func)
            standings[winner] += 1
            play_again = play_another()
    except SystemExit:
        pass

    # Tally results and print a farewell message.
    print ''
    print "Thanks for playing! Results:"
    x_score = standings['X']
    o_score = standings['O']
    player_x_string = 'Team X (%s):' % player_x_func.__doc__
    player_o_string = 'Team O (%s):' % player_o_func.__doc__

    if x_score >= o_score:
        print player_x_string, x_score
        print player_o_string, o_score
    else:
        print player_o_string, o_score
        print player_x_string, x_score
    print "Ties:", standings['Tie']
    print ''

if __name__ == '__main__':
    main()
