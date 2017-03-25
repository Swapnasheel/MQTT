# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# Swapnasheel Sonkamble
# Mini project "GUESS THE NUMBER "
#try running on www.codeskulptor.org


from simplegui import *
from math import *
from random import *

secret_number = 0
count = 0
range_num = 100 #default will be range 100 

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, count, range_num
    
    secret_number = randrange(0, range_num)
    
    #deciding my count------
    if range_num == 100:
        count = 7
    elif range_num == 1000:
        count = 10
    
    print 
    print 'New game, Range is from 0 to ' + str(range_num)
    print 'Number of remaining guesses is ', count 
        
    pass
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_num
    range_num = 100
    new_game()
    
        
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_num
    range_num = 1000
    new_game()
    pass

    
def input_guess(guess):
    # main game logic goes here	
    
    global secret_number, count
    print 
    
    win = False
    
    print "Guess was", guess
    
    count -= 1
    print 'Number of remaining guesses is', count
    
    if int(guess) == secret_number:
        won = True
        print "Congratulations, you won!! \n"
        new_game()
        return
    elif count == 0:
        print "Sorry, You lost!!\n "
        print 'Secret Number was', secret_number
        new_game()
        return
    elif int(guess) > secret_number:
        print 'Lower!'
    elif int(guess) < secret_number:
        print 'Higher!'
    else:
        pass
        
    
# create frame
f = create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
f.add_button('Range is [0,100)', range100, 200)
f.add_button('Range is [0, 1000)', range1000, 200)
f.add_input("Enter the guess", input_guess, 200)

# call new_game 
new_game()
f.start()

# always remember to check your completed program against the grading rubric
