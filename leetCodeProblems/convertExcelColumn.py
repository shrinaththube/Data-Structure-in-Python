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

''' Converting excel column letters to integer number base is 1 --> A
    for base 0 --> A we have to use 25 instead of 26 everywhere
'''
def columnLetterToNumber(letters):
    number = 0
    for l in letters:
        number *= 26
        number += ord(l.upper()) - ord('A') +1
    return number


''' Converting excel column number to letter'''
def columnNumberToLetter(number):
    letter = ""
    while number > 0:
        number -=1 # This is very important ... It convert number form (1 to n) to (0 to n-1) number bcz ord('A') = 65 and ord('Z') = 90
        # if we get 26 as a 'Z' then 65 + 26 = 91 is not valid... So need to subtract 1 every time from number
        rem = number % 26 
        #print number , rem
        letter = chr(ord('A') + rem) + letter
        number /= 26
                    
    return letter

def main():
    num =  columnLetterToNumber("AABBCCDD")
    print num
    print columnNumberToLetter(num)

if __name__ == '__main__':
    main()