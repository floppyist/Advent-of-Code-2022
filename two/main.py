#!/usr/bin/env python3.10

import enum 

class Figure( enum.Enum ):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

# Scissor (3) > Paper (2) > Rock (1) > Scissor (3)
game_rules = [ Figure.SCISSOR, Figure.PAPER, Figure.ROCK ]

turns_one = [ Figure.ROCK, Figure.PAPER, Figure.SCISSOR ]
turns_two = [ Figure.PAPER, Figure.ROCK, Figure.SCISSOR ]

def main():
    scores = [ 0, 0 ]

    for i in range( len( turns_one ) ):
        result = is_win( turns_one[ i ], turns_two[ i ] )

        if result == -1:
            scores[0] += 3
            scores[1] += 3
        if result == 1: scores[0] += 6
        if result == 0: scores[1] += 6
       
        scores[0] += turns_one[ i ].value
        scores[1] += turns_two[ i ].value

    print( '[Player 1]: {}\n[Player 2]: {}'.format( scores[0], scores[1] ) )

def is_win( figure_one, figure_two ):
    if ( figure_one == figure_two ):
        return -1

    for i in range( len( game_rules ) ):
        if ( game_rules[ i ] == figure_one ):
            if ( ( i - 1 ) < 0 ):
                figure_win = game_rules[ -1 ]
            else:
                figure_win = game_rules[ i - 1 ]

            if ( figure_two == figure_win ):
                return 0
            else:
                return 1

if __name__ == '__main__':
    main()