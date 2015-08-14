#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body


def rand_num_guess():
	x = random.randint(1, 25) 			# Generate the random number to be guessed
	
	for guess_num in range(5):
		try:
			user_guess = int(raw_input("Guess the random number:\n"))
		except:
			print "Please enter an integer value."	#Attempt at try/except
			continue
		else:
			if(user_guess == x):
				print "You guessed correctly!"
				break
			elif(user_guess < x):
				print "The random number is higher than your guess."
			elif(user_guess > x):
				print "The random number is lower than your guess."
		


""" This function kind of achieves the purposes of the exercise,
but I'd like to print a statement notifying the user they have exceeded 
the maximum guesses.  I'll check other solutions after I submit this."""




################################################################################
def main():


    rand_num_guess() # Remove this and replace with your function calls
    

if __name__ == '__main__':
    main()