'''
Created on Jun 16, 2016

@author: Shrinath Thube
'''
"""
    ************************* Excel ********************************
    Following problems are covered in this module
    
    1) Convert excel column letters to integer number
    2) Convert excel column number to letters
    
    ***************************************************************************
""" 

''' Converting excel column letters to integer number base is 0 --> A
    for base 1 --> A we have to use 26 instead of 25 everywhere
'''
def columnLetterToNumber(letters):
    number = 0
    for l in letters:
        number *= 25
        number += ord(l.upper()) - ord('A') + 1
    return number


''' Converting excel column number to letter'''
def columnNumberToLetter(number):
    letter = ""
    while number > 0:
        rem = number % 25
        letter += chr(rem + ord('A') -1 )
        number /= 25
    return letter[::-1]


def main():
    num =  columnLetterToNumber("AABBCCDD")
    print num
    print columnNumberToLetter(num)

if __name__ == '__main__':
    main()