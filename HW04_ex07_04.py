#!/usr/bin/env python
# HW04_ex07_04

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:
    
#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes the
# resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

################################################################################
# Imports
import sys
import math

# Body

def eval_loop():
	final_value = 0.0 # attempting to initialize a variable to hold the potential 'last expression evaluated'
	while True:
		user_statement = raw_input("Please enter a string to be evaluated:\n")
		if (user_statement == 'done'):
			return final_value # exit the while loop
		else:
			try:
				print eval(user_statement)			
				final_value = eval(user_statement) # Attempting to save value in case it is the last expression evaluated
			except:
				print "Please submit a valid string" 
				continue



		


################################################################################
def main():

    eval_loop()
    

if __name__ == '__main__':
    main()