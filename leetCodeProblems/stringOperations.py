'''
Created on Jun 16, 2016

@author: Shrinath Thube
'''
"""
    ************************* String Operations *******************************
    Following problems are covered in this module
    
    1) Finds common characters of two strings
    2) Find the longest palindrome in given string by Monarch Algorithm
    3) Wild card match of text string and pattern by Dynamic programming
    4) Wild card match of text string and pattern by iterative
    5) Regular expression match of text string and pattern by Dynamic programming
    6) Find minimum distance between two string that needs to edit to match those strings by Dynamic programming
    7) Find if two strings are anagram
    8) Print anagram strings from k strings list 
    
    ***************************************************************************
""" 

from collections import OrderedDict

''' Finds common characters of two strings 
    Time complexity - O(n)
    Space complexity - O(1)
'''
def intersectionOf2String(str1,str2):
    intStr = ""
    flag = [False] * 256
 
    for b in str2:
        flag[ord(b)] = True
    
    for a in str1:
        if flag[ord(a)]: intStr +=a  
    
    return intStr


''' Find the longest palindrome in given string by Monarch Algorithm
    reference - ideserve
    Time complexity - O(n)
    Space complexity - O(n)
'''

def findLongestPalindrome(raw_string):
    manarcher_string = ['!','#']
    for ch in raw_string:
        manarcher_string.append(ch)
        manarcher_string.append('#')
    manarcher_string.append('$')
    
    pali_size = [0]*len(manarcher_string)
    
    ''' abababa
        !#a#b#a#b#a#b#a#$
    '''
    pali_center = 0
    pali_right_boundary = 0
    
    for position in xrange(len(manarcher_string)):
        pali_symmetry_pos = 2*pali_center - position
        
        if position < pali_right_boundary:
            pali_size[position] = min(pali_right_boundary - position,pali_size[pali_symmetry_pos])
        
        while(position + (pali_size[position] + 1) < len(manarcher_string) and manarcher_string[position + (pali_size[position] + 1)] == manarcher_string[position - (pali_size[position] + 1)]):
            pali_size[position] += 1
        
        if position + pali_size[position] > pali_right_boundary:
            pali_center = position
            pali_right_boundary = position + pali_size[position]
            
            
    max_pali_size = max(pali_size)
    pali_center = pali_size.index(max_pali_size)
    
    longest_pali = "".join(''.join(manarcher_string[pali_center - max_pali_size : pali_center + max_pali_size]).split("#"))
    return longest_pali
   

''' Wild card match of text string and pattern by Dynamic programming
    Time complexity - O(n^2)
    Space complexity - O(n^2)
'''
def wildCardMatchingByDP(text,pattern):
    if pattern == "*": return True
    if len(text)< 1 or len(pattern)<1: return
    
    WLMatrix = [[False for i in xrange(len(pattern)+1)] for j in xrange(len(text)+1)]
    
    WLMatrix[0][0] = True
    
    if pattern[0] =="*": WLMatrix[0][1] = True
        
    for row in xrange(1,len(WLMatrix)):
        for col in xrange(1,len(WLMatrix[0])):
            #print row , col, text[row-1], pattern[col-1]
            if text[row-1] == pattern[col-1] or pattern[col -1] == "?":
                WLMatrix[row][col] = WLMatrix[row-1][col-1]
            elif pattern[col-1] == "*":
                WLMatrix[row][col]= WLMatrix[row][col-1] or WLMatrix [row-1][col]
         
    #print WLMatrix
    return WLMatrix[row][col]

''' Wild card match of text string and pattern by iterative 
    Time complexity - O(n)
    Space complexity - O(1)
'''

def wildCardMatching(text,pattern):
    if len(text) <1 or len(pattern) < 1: return 
    
    posT = 0
    posP = 0
 
    ''' x?y*z  x?y*??a
        xaylmnz'''
    while posP < len(pattern) and posT < len(text):
        # print posP, posT, pattern[posP], text[posT]
        if pattern[posP] == "*":
            while  posP < len(pattern) -1  and pattern[posP] == "*" : posP +=1
            
            if pattern[posP] == "?":
                qCount = 0
                while posP < len(pattern) and pattern[posP] == "?": 
                    posP +=1
                    qCount +=1
                if  len(text) - posT < qCount: return False
               
                if posP >= len(pattern): return True
                
            while posT < len(text) and posP < len(pattern) and (pattern[posP] != text[posT]): posT +=1
           
        elif pattern[posP] == "?":
            posP +=1
            posT +=1
        
        elif pattern[posP] != text[posT]:
            return False
        
        else:
            posP +=1
            posT +=1

    #print posP, posT, len(pattern), len(text)
    
    if pattern[len(pattern)-1] == "*": return True
     
    if posP  != len(pattern) or posT  !=len(text):
        return False
      
    #if pattern[posP] == text[posT] or pattern[posP] == "?": 
    #   return True
    return True

'''
    Regular expression match of text string and pattern by Dynamic programming
    --reference - Tushar Roy video YouTube 
    Time complexity - O(n^2)
    Space complexity - O(n^2)

a*b - b, ab,aab,aaab
a.b - acb,aab,avb
a*.b - cb, acb, aacb, aavb
a*b.*y - by, bly, ably, ablmy

  ""a * b . c
""T F T F F F
a F T T F F F
a F F T F F F
b F F T T F F 
e F F T F T F
c F F T F F T

1> if text t match with pattern p or p == .
    regMat[t][p] = regMat[t-1][p-1]

2> if p == "*" then 

    0 occrence of previous letter -> regMat[t][p] = regMat[t][p-2]
    or multiple ocerence -> regMat[t][p] = regMat[t-1][p]
    or p == . Then T
    
3> no match p and t -> False


'''
def regularExpressionMatchingByDP(text,pattern):
    if len(text) < 1 or len(pattern) < 1: return
    
    regMat = [[False for i in xrange(len(pattern)+1)] for j in xrange(len(text)+1)]
    
    regMat[0][0] = True
    # Edge cases
    if pattern[0] == "*": regMat[0][1] = True
    if pattern[1] == "*": regMat[0][2] = True
    text = text
    pattern = pattern
    for t in xrange(1,len(regMat[0])):
        for p in xrange(1,len(regMat)):
            if text[t-1] == pattern[p-1] or pattern[p-1] == ".":
                regMat[t][p] = regMat[t-1][p-1]
            elif pattern[p-1] == "*":
                regMat[t][p] =  regMat[t][p-2] or regMat[t-1][p] or pattern[p-1] == "."
            #print t, p, text[t-1],pattern[p-1], regMat[t][p]    
    #print regMat           
    return regMat[-1][-1]
    
''' 
    Find minimum distance between two string that needs to edit to match those strings by Dynamic programming
    --reference - Tushar Roy video YouTube 
    Time complexity - O(n^2)
    Space complexity - O(N^2)

          a b c d e f g
        0 1 2 3 4 5 6 7
      a 1 0 1 2 3 4 5 6
      s 2 1 1 2 3 4 5 6
      x 3 2 2 2 3 4 5 6
      d 4 3 3 3 2 3 4 5
      e 5 4 4 4 3 2 3 4
    
    output --> 4
'''
def minEditDistance(str1,str2):
    if str1 == str2: return 0 # edge case. Best time complexity O(n)
    #Considering empty string size of matrix more than length of strings 
    minDistMat = [[None for i in xrange((len(str1) + 1))] for j in xrange((len(str2) + 1))]
   
    # 0 row and 0 column consider empty string   
    for i in xrange(len(str1)+1):
        minDistMat[0][i] = i
    
    for i in xrange(len(str2)+1):
        minDistMat[i][0] = i
    
    for i in xrange(1,len(minDistMat)):
        for j in xrange(1,len(minDistMat[0])):
            if str2[i-1] == str1[j-1]:
                minDistMat[i][j] = minDistMat[i-1][j-1]
            else:
                minDistMat[i][j] = min(minDistMat[i][j-1],minDistMat[i-1][j-1],minDistMat[i-1][j]) + 1
        
    #for i in xrange(len(minDistMat)):
    #    print minDistMat[i]
    return minDistMat[-1][-1]

''' Find if two strings are anagram 
    Add the ASCII value of each character of string and if two strings have same value then they are anagram 
    Time complexity - O(n)
    Space complexity - O(1)
'''

def isAnagram(str1,str2):
    #strip the strings from left and right
    str1 = str1.strip(' \t\n\r')
    str2 = str2.strip(' \t\n\r')
    if len(str1) != len(str2): return False
    if str1 == str2 : return True
    
    ''' # Normal way 
    str1_value = 0
    str2_value = 0
    for  ch in str1:
        str1_value += ord(ch)
    
    for ch in str2:
        str2_value += ord(ch)
    '''    
    # pythonic way    
    str1_value = sum(ord(ch)  for ch in str1)
    str2_value = sum(ord(ch)  for ch in str2)
    #print str1_value,str2_value
    return str1_value == str2_value


''' Print anagram strings from k strings list 
    Add the ASCII value of each character of string and if two strings have same value then they are anagram
    and keep key as ASCII value and strings list as a value 
    Time complexity - O(nk)
    Space complexity - O(1)
    
    Example - 
     ["abc","cba","rat","cat","tar","tea","act"]
'''
def printAnagramStrings(list_string):
    if not list_string: return
    ana_dict = OrderedDict() # to maintain insertion order
    for string in list_string:
        str_value = sum(ord(ch) for ch in string) # calculate the asci value of string
        if not str_value in ana_dict:
            ana_dict[str_value] = [string]
        else:
            ana_dict[str_value].append(string)
        
    for key in ana_dict:
        #print ana_dict[key]
        for ele in ana_dict[key]:
            print ele,
        print 

    
        
        
#"""
def main():
    
    # Find intersection of two string 
    print "Intersection of defagbc abcdefg ->", intersectionOf2String("defagbc", "abcdefg")
    
    # Find longest palindrome from given stirng
    print "Longest pali of tabababacgy -> ",findLongestPalindrome("tabababacgy")
    
    print"DP-", wildCardMatchingByDP("xaylmnz", "x?y*")
    #'''
    text = ["xaylmnzbb","xaylmnz","xaylmnz","xaylmnz","xa"] 
    pattern = ["x?y*","x?y*","x?y*z","*", "x?"]
    
    for tex, pat in zip(text,pattern):
        print"Iterative-", wildCardMatching(tex, pat)
        print"DP-", wildCardMatchingByDP(tex, pat)
    
    print 
    print "Regex match -> ", regularExpressionMatchingByDP("aabec", "a*b.c")
    print "Regex match -> ", regularExpressionMatchingByDP("xaabec", "xa*b.c")
    
    print "----------------------------------------------------------"
    #minimum edit distance method
    print "minimum distance - ",minEditDistance("abcdefg", "asxde")
    
    print "-----------------------------------------------------------"
    # Find strings ara anagram
    print "aab and aba are anagram - ",isAnagram("aab", " aba")
    
    print "-"*60
    #print anagram string from given list
    print "Following strings in row are anagram"
    printAnagramStrings(["abc","cba","rat","cat","tar","tea","act"])


if __name__ == '__main__':
    main()
    #"""