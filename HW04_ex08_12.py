# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function


################################################################################
# Body
""" Function rotate_word will serve the purpose of accepting a string and an int
as parameters, and will produce an output that 'shifts' each letter in the string
through the alphabet by the number of letters specified by the int, producing an
'encrypted' string.
"""

import string

def rotate_letter(letter_, rotate_amt): # Accepts a single character to increment
	if letter_.isupper():		# This whole function serves to rotate letters
		start = ord('A')		# to their new location.  The function preserves
	elif letter_.islower():		# uppercase letters as upperase, and lowercase
		start = ord('a')		# letters as lowercase.  I had to get help
	else:						# to figure this part out.
		return letter_

	ord_place = ord(letter_) - start #sets a 1-26 base to make next line easier
	return chr(((ord_place + rotate_amt) % 26) + start)

	""" The retur chr... line serves to get the remainder of the amount the character
	moves, mod 26, so that no matter how extreme the step (rotate_amt) is, we're able
	to bring it back into the 26 acceptable values for either uppercase or lowercase 
	letters.  The return statement then coverts back from the numeric code to a 
	character, and returns the character."""

def rotate_word(word_, step_): # Accepts a string and a 'step' to increment by
	""" Function takes each character in word_, the increment step_, and passes
	these to the rotate_letter function.  Then concatenates a string of rotated
	characters to produce the final result final_word"""
	
	final_word = ''

	for char_ in word_:
		final_word = final_word + rotate_letter(char_, step_)
	
	return final_word



################################################################################
def main():

 print rotate_word('cheer', 7) 
 print rotate_word("Melon", -10)   
    

if __name__ == '__main__':
    main()