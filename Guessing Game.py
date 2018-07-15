# Sarah Sides
# 7/9/18
# Guessing Game

import random
import time
trials = 0
print ( "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" )
print ( "Ready to play? Try to guess my number, and I'll try to guess yours! We'll play three rounds.")
x = int (input( "Give me the range of numbers we can guess between. What's the lowest number? "))
y = int (input( "And what's the highest number? "))
print ( "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" )
while trials < 4:
    answer = random.randint(x,y)
    print ( "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" )
    print ("My turn! I'm thinking of a number between" ,x, "and" ,y,)
    guess = int (input ("What do you think my number is? "))

    if guess == answer:
        print ("Nice job! You guessed correctly. My number was" ,answer,  ".")
    elif y + 1 > guess > answer:
        print ("Oops! You're too high. Your guess was" ,guess,  ", but the answer was" ,answer,  ".")
    elif x - 1 < guess < answer:
        print ("Oops! You're too low. Your guess was" ,guess, ", but the answer was" ,answer,  ".")
    elif x > guess:
        print ("Oops! Your guess is too low out of range. Be sure to choose a number between" ,x, "and" ,y, ". Your guess was" ,guess, ", but the answer was" ,answer,  ".")
    else:
        print ("Oops! Your guess is too high out of range. Be sure to choose a number between" ,x, "and" ,y, ". Your guess was" ,guess, ", but the answer was" ,answer,  ".")
        
    print ( "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" )
    
    user_answer = int (input ("Your turn! Think of a number in your head and put it here. I'll close my eyes and see if I can guess. "))
    compute_guess = random.randint(x,y)
    print ("I'm guessing..." ,compute_guess, "!")

    if compute_guess == user_answer:
        print ("Yes!!! I guessed correctly! My guess was" ,compute_guess, ".")
    elif y + 1 > user_answer > compute_guess:
        print ("Oops! I was too low. My guess was" ,compute_guess,  ", but the answer was" ,user_answer,  ".")
    elif x - 1 < user_answer < compute_guess:
        print ("Oops! I was too high. My guess was" ,compute_guess, ", but the answer was" ,user_answer,  ".")
    elif x > user_answer:
        print ("You cheated! Your answer is too low out of range. Be sure to choose a number between" ,x, "and" ,y, ". My guess was" ,compute_guess, ", but the answer was" ,user_answer, ".")
    else:
        print ("You cheated! Your answer is too high out of range. Be sure to choose a number between" ,x, "and" ,y, ". My guess was" ,compute_guess, ", but the answer was" ,user_answer, ".")

    trials += 1

print ( "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" )
print ("Thanks for playing with me!")
time.sleep(5)
