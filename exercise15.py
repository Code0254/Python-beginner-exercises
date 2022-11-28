'''*#15*
#TIC TAC TOE GAME
## PART ONE -- Draw the tic tac toe board

- Create a 3x3 board (like in tic tac toe). Obviously, 
they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

- Ask the user what size game board they want to draw, 
and draw it for them to the screen using Pythons print statement.'''
def board_size(k):
    a= ' --- '
    b = '    |' 
    for num in range (k):    
        print (a*k)
        print (f'|{b*k}')
        
    print (' --- '*k)

k = int(input('What size of game board?'))
board_size(k)