#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """If the first character in the string is an uppercase letter, the function 
    returns False, even if every other character is lowercase.  The function would
    work in cases where the first character is not uppercase.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """The for loop here isn't evaluating a string 's' (as long as the string exists)
    but rather is evaluating whether the character 'c' is lowercase.  The function will 
    always return True as long as any legitimate string is passed as an argument.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """The function is looking at each character in the string, and if it finds a single 
    lowercase letter it changes the value of flag to True.  The function has produced the 
    desired result for all my test cases, but will not work for empty strings as flag is 
    never assigned.
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """This function has worked for all test cases I've tried, including empty 
    strings
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """This function indexes through a string, and if it finds a single uppercase
    letter, the function returns False.
    """
    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print any_lowercase1("Test")
    print any_lowercase2("TEST")
    print any_lowercase3("(empty string)")
    print any_lowercase5("teSt")    
    

if __name__ == '__main__':
    main()