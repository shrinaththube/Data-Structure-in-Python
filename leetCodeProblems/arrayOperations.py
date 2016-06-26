'''
Created on Jun 26, 2016

@author: Shrinath Thube
'''

""" Find the any peek element in given unsorted array or list. 
Time complexity - O(log n) - Binary search algorithm
space complexity - O(1)
"""
def findPeekElement(array):
    if len(array) <1: return 
    start = 0
    end = len(array)
    
    while start <= end:
        mid = (start + end)/2
        #print start,mid, end,array[mid]
        if mid == len(array)-1 and array[mid] > array[mid-1]: #edge case- end element compare
            return array[mid]
        elif mid== 0 and array[mid] > array[mid+1]:  #edge case- first element compare
            return array[mid]
        elif array[mid] > array[mid+1] and array[mid] > array[mid-1]:
            return array[mid]
        elif array[mid] < array[mid+1]:
            start = mid + 1
        else:
            end = mid -1 
        

print "Peek element - > ",findPeekElement([3,4,5,12,7,6,15,16,1])
