#!/usr/bin/env python3.10

def main():
    elve = ( 0, 0 )
    elve_counter = 0
    calorie_counter = 0

    for element in open( 'file.txt', 'r' ):
        try:
            calorie_counter += int( element )
        except:
            elve_counter += ( lambda x: 1 if x > 0 else 0 )( calorie_counter )
            calorie_counter = 0
        finally:
            elve = ( lambda x, y: ( elve_counter + 1, x ) if x > y else elve )( calorie_counter, elve[1] )
            
    print( 'Elve [{0}] has the most calories with a value of: [{1}]'.format( elve[0], elve[1] ) )

if __name__ == '__main__':
    main()