#!/usr/bin/env python

import random

def main():
    """Start a Genre Music game."""
    print("Guess the Music Genre!")

    genre = [
        
        "pop yeh yeh"
        ]

    x = random.choice(genre)
    
    guess = None

    while x != guess:

        guess = str(input("What song genre that your grandfather love? "))
        
        if x == guess:
            print("Tekaan anda : {}. Betul.... Atuk menyanyangi Anda!".format(guess))
            break
        else:
            print("Anda menjawab : {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()