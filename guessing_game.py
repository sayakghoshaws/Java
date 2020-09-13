#Author:Sayak Ghosh
#Class:Python 1
#Project 1 - Guessing Game
#In this game, the computer will select a secret number between a min and max.  The user is then given n chances to guess the computer's secret number.
#If the user guesses correctly, they win.  Otherwise, the computer states whether the secret number is greater or less than the last guess
import random
First_pass = True   #this is a variable to define if the block of code for assigning initial random variable should execute or not
replay_game = False
replay_yes_no_input = 'no' #This variable tracks whether the user has opted for replay or not
attempts_left = 1   #This variable is just to initialize number of attempts,it will be overriden below
while attempts_left > 0 or First_pass: #While loop ensure that until the user wants the logic of the program should run
    if replay_yes_no_input == 'yes':
        replay_yes_no_input = 'no'
        First_pass = True
#This blocks asks for initial inputs from user
    if First_pass:
        guess_min = int(input('Enter minimum value: '))
        guess_max = int(input('Enter maximum value: '))
        random_number = random.randint(guess_min,guess_max)
        print(random_number)
        attempts_left = int(input('Enter maximum number of guesses:'))
        print('I\'m thinking of a number between ' + str(guess_min) + ' and ' + str(guess_max) + '...')
        First_pass = False
    guessed_num = int(input('You have ' + str(attempts_left) + ' guesses left: '))
#below ifelse block checks the user input and responds back
    if guessed_num == random_number:
        print('Correct!')
        replay_yes_no_input = input('Would you like to play again yes/no?')
        attempts_left = 2               #this varialble is set to 2 just to allow it to re enter while loop,this will be overwritten anyways
        if replay_yes_no_input != 'yes':
            break
    elif  guessed_num < random_number :
        print('Nope, higher!')
    else:
        print('Nope, lower!')
    attempts_left = attempts_left - 1
    if attempts_left == 0:              #if the user has exhausted attempts respond with a lose!
        print('You lose! I was thinking of ' + str(random_number) + '!')
        replay_yes_no_input = input('Would you like to play again yes/no?')
        if replay_yes_no_input == 'yes':
            attempts_left = 2           #this varialble is set to 2 just to allow it to re enter while loop,this will be overwritten anyways
#end of while loop
print('Thanks for playing!')

''' Feedback***********************
Your program seems to work just fine!  My only concerns are style-related, which you can find below:

(1) I would suggest using shorter lines (especially with comments).  Line length should generally be no more than 79 characters, and you can always break comments onto multiple lines.

(2) Splitting up your code into two loops (as in my sample solution) would simplify your code, as that would remove the need for your variable 'First_pass', and would remove the need for placing a dummy value into attempts_left (see line 29).

(3) I would also suggest putting comments on a line of their own.  In-line comments (on the same line as code) should generally be used for shorter comments that affect only that line.  Your use to describe variables in lines 7-10 is acceptable, but the descriptions should be shorter.
'''
