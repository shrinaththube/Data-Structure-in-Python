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


''' Find the longest palindrom in given string Using Monarch Algo
    Time complexity - O(n)
    Space complexit - O(n)
'''

def findLongestPalindrome(raw_string):
    manarcher_string = ['!','#']
    for ch in raw_string:
        manarcher_string.append(ch)
        manarcher_string.append('#')
    manarcher_string.append('$')
    
    pali_size = [0]*len(manarcher_string)
    
    ''' abababa'''
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
   
# Find intersection of two string 
print "Intersection of defagbc abcdefg ->", intersectionOf2String("defagbc", "abcdefg")

# Find longest palindrome from given stirng
print "Longest pali of tabababacgy -> ",findLongestPalindrome("tabababacgy")
