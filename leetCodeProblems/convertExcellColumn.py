'''
Created on Jun 16, 2016

@author: Shrinath Thube
'''


''' Converting excel column letter to integer number base is 0 --> A
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


num =  columnLetterToNumber("AABBCCDD")
print num
print columnNumberToLetter(num)