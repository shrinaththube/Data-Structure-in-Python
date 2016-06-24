import timeit


''' Backtracking way to find all permutation of string '''

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

''' Coooolest algorithm to count and print all permutation
    got it form -    http://www.quickperm.org/
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



""" Leetcode discussion  
BackTracking way to find all valid ip combination of number string
"""
             
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
    

count = 0
#list_char = list(string) 
list_char = "a,b,c,d,e".split(",")

print "\n----------------Backtracking -----------\n"
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

print"\n------------print All possible valid ip addresses -----------------------\n"
print "12345678 -> ",restore_ip_addresses("12345678")
print "25525511135 ->",restore_ip_addresses("25525511135")
print "1234 ->",restore_ip_addresses("1234")
print "12345678902344 ->",restore_ip_addresses("12345678902344")
print "123 ->",restore_ip_addresses("123")