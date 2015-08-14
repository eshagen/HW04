#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body
def count(word, letter):
	letter_counter = 0

	for char_ in word:
		if (char_ == letter):
			letter_counter = letter_counter + 1
	print letter_counter		



################################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
 
    count('eric', 'e')
    count('banana', 'a')
    count("test", 'o')
    count("zkealfzkdlzzzzz", 'z')

if __name__ == '__main__':
    main()