# max roschke :: sample solution to project 01
# repeat games until the user tells us to stop
import random

while True:
    # run a game
    # 1) select our random number
    secret = random.randint(1, 10)
    print("i'm thinking of a number between 1 and 10...")

    # 2) get some guesses from the user
    for guesses_left in range(6, 0, -1):
        # 2.1) prompt the user for a guess
        prompt = "you have " + str(guesses_left) + " guesses left: "
        guess = int(input(prompt))
        # guess = int(input("you have " + str(guesses_left) + " guesses left: "))
        # print("you have", guesses_left, "guesses left: ")

        # 2.2) compare that guess against the secret value
        if guess > secret:
            print('too high!')
        elif guess < secret:
            print('too low!')
        else: # guess == secret
            print('you win!')
            break
    else:
        # this runs if the loop didn't break, which means they ran out of guesses
        print('you lose! my number was', secret)

    # ask the user if they want to play again
    response = input("do you want to play again? ")
    if response == 'no' or response == 'n':
        break

# note that, even without the code, the comments still give a rough sketch of
# the entire program...
# repeat games until the user tells us to stop
    # run a game
    # 1) select our random number
    # 2) get some guesses from the user
        # 2.1) prompt the user for a guess
        # 2.2) compare that guess against the secret value
        # this runs if the loop didn't break, which means they ran out of guesses
    # ask the user if they want to play again
