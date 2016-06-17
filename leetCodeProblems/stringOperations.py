'''
Created on Jun 16, 2016

@author: Shrinath Thube
'''

''' Finds common characters of two strings '''
def intersectionOf2String(str1,str2):
    intStr = ""
    flag = [False] * 256
 
    for b in str2:
        flag[ord(b)] = True
    
    for a in str1:
        if flag[ord(a)]: intStr +=a  
    
    return intStr

print intersectionOf2String("defagbc", "abcdefg")

