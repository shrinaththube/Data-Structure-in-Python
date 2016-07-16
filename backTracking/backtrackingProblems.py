'''

@author: Shrinath Thube
'''

"""
    ************************* Backtracking ************************************
    Following problems are covered in this module
    
    1) Find all permutation of unique characters string by Backtracking
    2) Coooolest algorithm to count and print all permutation of unique characters string by iterative
    3) Find all permutation of repeated characters string by BackTracking
    4) Find all Subset of characters string considering repeated characters by BackTracking
    5) Find all valid IP addresses from combination of number string by BackTracking
    6) Find all valid IP addresses from combination of number string by iteration
    
    ***************************************************************************
""" 

import timeit


''' Find all permutation of unique characters string by Backtracking 
    Time complexity - O(n!) - recurrence equation T(n) = n * ( T(n-1) + O(1)) 
    Space complexity - exponential if consider recursive stack
'''

count = 0
def printAllPermutaionOfString(list_char,start,end):
    global count
    if len(list_char) < 1: return
    if start == end:
        count +=1
        print ''.join(list_char), 
        return
    else:
        for ind in range(start,end):
            list_char[start], list_char[ind] = list_char[ind],list_char[start]
            #print list_char [start], list_char[ind], list_char
            printAllPermutaionOfString(list_char, start + 1, end)
            #print "after re", list_char [start], list_char[ind], list_char
            list_char[start], list_char[ind] = list_char[ind],list_char[start]

''' Coooolest algorithm to count and print all permutation of unique characters string by iterative
    got it form -    http://www.quickperm.org/
    Time complexity - O(n!)
    Space complexity - O(1)
'''
def allPermutaionOfStringIterative(list_char):
    global count
    n = len(list_char)
    p = [0]*n
    print ''.join(list_char),
    i = 1
    while i< n:
        if p[i]<i:
            j = i%2
            #print j, 
            if j != 0:
                j = p[i]
            list_char[i],list_char[j] = list_char[j],list_char[i]
            #print "if ---", "j- ",j,"i -" ,i,"p - ", p,
            print ''.join(list_char),
            count +=1
            p[i] +=1
            #print p,list_char
            i=1
        else:
            p[i] = 0
            i +=1
            #print "else ---- ", "i -", i, p

''' Find all permutation of repeated characters string by BackTracking  
    Time complexity - O(n!)
    space complexity - O(1)
'''
def allPermutationOfRepeatedCharString(raw_string):
    list_unique_char = {}
    list_combi_char = ['']*len(raw_string)
    for ch in raw_string:
        if list_unique_char.has_key(ch):
            list_unique_char[ch] += 1
        else:
            list_unique_char.setdefault(ch,1)
    
    backTrackAllPermutationOfRepeatedCharString(list_unique_char,list_combi_char,0)
    

def backTrackAllPermutationOfRepeatedCharString(list_unique_char,list_combi_char,level_rec):
    if len(list_unique_char) <1: return
    if level_rec == len(list_combi_char):
        print ''.join(list_combi_char),
        return
    
    for ch in list_unique_char:
        if list_unique_char[ch] == 0: continue
        list_combi_char[level_rec] = ch
        list_unique_char[ch] -=1
        backTrackAllPermutationOfRepeatedCharString(list_unique_char, list_combi_char, level_rec + 1)
        # print list_unique_char,list_combi_char
        list_unique_char[ch] +=1
    


''' Find all Subset of characters string considering repeated characters by BackTracking  
    Time complexity - O(2 ^ n) exponential
    space complexity - O(1)
'''

def allSubSetOfString(raw_string):
    if len(raw_string) < 1:
        return
    unique_ch_list = []
    ch_count = []
    temp_arr = [""]*len(raw_string)
    result_sub = []
    #counting repeated characters and make list of unique char and their count
    for ch in raw_string:
        if ch in unique_ch_list:
            ch_count[unique_ch_list.index(ch)] +=1
        else:
            unique_ch_list.append(ch)
            ch_count.append(1)
    
    backTrackAllSubSetOfString(unique_ch_list, ch_count,temp_arr,result_sub, level =0, pos = 0)        
    return result_sub
    
def backTrackAllSubSetOfString(unique_ch,ch_count,temp_arr,result_sub,level,pos):
    
    if level == len(temp_arr): return
    
    for i in xrange(pos,len(unique_ch)):
        if ch_count[i] < 1: continue
        temp_arr[level] = unique_ch[i]
        ch_count[i] -=1
        #print ''.join(temp_arr),  temp_arr,  ch_count
        result_sub.append(''.join(temp_arr))
        backTrackAllSubSetOfString(unique_ch, ch_count, temp_arr,result_sub, level + 1, i)
        temp_arr[level] = ""
        ch_count[i] +=1

    

''' Find all valid IP addresses from combination of number string by BackTracking  
    reference - Leetcode discussion  
    Time complexity - O(n!)
    Space complexity - O(1)
'''
             
def restore_ip_addresses(raw_string):
    if len(raw_string) < 4 or len(raw_string)>12: return 
    restored_ip=[]
    ip = ['']*4
    restore_backtrack(raw_string,ip,0,restored_ip)
    return restored_ip

def restore_backtrack(raw_string,ip,octet,restored_ip):
    if len(raw_string) < 1: return
    if octet == 3:
        ip[octet] = raw_string
        if is_octet_valid(ip[octet]):
            restored_ip.append('.'.join(ip))
        return 
    
    for i in xrange(1,4):
        ip[octet] = raw_string[:i]
        if is_octet_valid(ip[octet]):
            restore_backtrack(raw_string[i:], ip, octet + 1, restored_ip)
    
def is_octet_valid(octet_string):
    if len(octet_string) <1: return False
    elif str(int(octet_string)) != octet_string or int(octet_string) > 255: return False
    return True
    

''' Find all valid IP addresses from combination of number string by iteration  
    reference - http://massivealgorithms.blogspot.com/2014/06/leetcode-restore-ip-addresses-darrens.html  
    Time complexity - O(n^4)
    Space complexity - O(1)
'''

def restore_ip_iterative(raw_string):
    restored_ip =[]
    for a in xrange(1,4):
        if len(raw_string[a:]) > 9:continue
        for b in xrange(1,4):
            if len(raw_string[a+b:]) > 6:continue
            for c in xrange(1,4):
                d = len(raw_string[a+b+c:])
                if d > 3:continue
                if a+b+c+d == len(raw_string):
                    octetA = raw_string[:a]
                    octetB = raw_string[a:a+b]
                    octetC = raw_string[a+b:a+b+c]
                    octetD = raw_string[a+b+c:]
                    if is_octet_valid(octetA) and is_octet_valid(octetB) and is_octet_valid(octetC) and is_octet_valid(octetD):
                        restored_ip.append(octetA + "." + octetB + "." + octetC+ "." + octetD)
                            
    return restored_ip


def main():
    #--------------  All permutation of unique character string --------------------#
    global count
    #list_char = list(string) 
    list_char = "a,b,c,d,e".split(",")
    
    print "\n----------------Backtracking -->All permutation of unique character string  -----------\n"
    start_time = timeit.default_timer()
    printAllPermutaionOfString(list_char, 0, len(list_char))
    print "\n number of permutation -",count
    elapsed = timeit.default_timer() - start_time
    print "time required to find - ",elapsed
    
    print "\n----------------Iterative with quick permutation algorithm -----------\n"
    count = 1
    start_time = timeit.default_timer()
    allPermutaionOfStringIterative(list_char)
    print "\n number of permutation -",count
    elapsed = timeit.default_timer() - start_time
    print "time required to find - ",elapsed
    
    #--------------  All permutation of repeated character string --------------------#
    print "\n----------------Backtracking --> All permutation of repeated character string -----------\n"
    
    allPermutationOfRepeatedCharString('AABC')
    
    # Subset of given string
    print
    print "\n----------------Backtracking --> All Subset of  string -----------------------------------\n"
    
    print allSubSetOfString("AABC")

    print
    print"\n------------print All possible valid ip addresses -----------------------\n"
    
    print "\n----------------Backtracking -----------\n"
    start_time = timeit.default_timer()
    print "12345678 -> ",restore_ip_addresses("1234567")
    elapsed = timeit.default_timer() - start_time
    print "time required to find - ",elapsed

    print "\n----------------Iterative with quick permutation algorithm -----------\n"
    
    start_time = timeit.default_timer()
    print "12345678 -> ", restore_ip_iterative("2550780")
    elapsed = timeit.default_timer() - start_time
    print "time required to find - ",elapsed


if __name__ == '__main__':
    main()
    
    