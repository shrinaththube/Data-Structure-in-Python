'''
Created on Jun 24, 2016

@author: Shrinath Thube
'''

import timeit

from backTracking.backtrackingProblems import *

#--------------  All permutation of unique character string --------------------#
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

print
print"\n------------print All possible valid ip addresses -----------------------\n"

print "\n----------------Backtracking -----------\n"
start_time = timeit.default_timer()
print "12345678 -> ",restore_ip_addresses("1234567")
elapsed = timeit.default_timer() - start_time
print "time required to find - ",elapsed

print
start_time = timeit.default_timer()
print "25525511135 ->",restore_ip_addresses("25525511135")
elapsed = timeit.default_timer() - start_time
print "time required to find - ",elapsed

print 
start_time = timeit.default_timer()
print "1234 ->",restore_ip_addresses("1234")
elapsed = timeit.default_timer() - start_time
print "time required to find - ",elapsed

print
print "12345678902344 ->",restore_ip_addresses("12345678902344")
print "123 ->",restore_ip_addresses("123")


print "\n----------------Iterative with quick permutation algorithm -----------\n"

start_time = timeit.default_timer()
print "12345678 -> ", restore_ip_iterative("1234567")
elapsed = timeit.default_timer() - start_time
print "time required to find - ",elapsed

print
start_time = timeit.default_timer()
print "25525511135 ->",restore_ip_iterative("25525511135")
elapsed = timeit.default_timer() - start_time
print "time required to find - ",elapsed

print 
start_time = timeit.default_timer()
print "1234 ->",restore_ip_iterative("1234")
elapsed = timeit.default_timer() - start_time
print "time required to find - ",elapsed

