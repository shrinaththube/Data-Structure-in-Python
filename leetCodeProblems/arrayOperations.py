'''
Created on Jun 26, 2016

@author: Shrinath Thube
'''
from copy import deepcopy


''' Kadane's Algorithm 
    Time complexity - O(n)
    '''
def findMaxSumSubArray(arr):
    if len(arr) < 1: return
    start = 0
    end = 0
    current_max = arr[0]
    global_max = arr[0]
    
    for i in xrange(1,len(arr)):
        
        if arr[i] > (arr[i] + current_max):
            start = i
        #else:
         
        current_max = max((arr[i]+ current_max), arr[i]) 
        
        if current_max > global_max:
            global_max = current_max
            end = i
            
    
    print "start ->",start,"end ->", end,"sub array -> ", arr[start:end+1],global_max
        
        


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
        

''' Find element that comes minimum 1/4 th times total elements in sorted array
    Time complexity - O (log n)
    Modified binary search 
'''

def findOneFourthLengthElement(arr,start,end,count):
    
    if len(arr) < 1: return
    
    if arr[start] == arr[end]:
        
        if not count.has_key(arr[start]):
            count.setdefault(arr[start],end - start +1)
        else:
            count[arr[start]] += end - start +1
        
        if count[arr[start]] > (len(arr)/4):
            # print count
            return arr[start]
    else:
        mid = (start + end)/2
        #print start, end, mid
        c = findOneFourthLengthElement(arr, start, mid, count)
        #print c, count
        if c:
            return c
        c = findOneFourthLengthElement(arr, mid +1, end, count)
        #print c
        if c: 
            return c


''' Find longest increasing sub sequence in given array 
    Time complexity - O(n log n)
    Space -> O(2n) -> O(n)
'''

def findLongesIncreasingSubsequence(arr):
    if len(arr) < 1: return
    
    parent =[None]*len(arr)
    inc_sub =[None]*(len(arr)+1)
    
    maxLength = 0
    
    for i in xrange(len(arr)):
        
        start = 1
        end = maxLength
        
        while start <= end:
            mid = (start + end) /2
            
            if arr[inc_sub[mid]] < arr[i]:
                start = mid + 1
            else:
                end = mid - 1
        
        position = start
       # print i,position, start, parent, inc_sub
        parent[i] = inc_sub[position-1]
        
        inc_sub[position] = i
        
        if position > maxLength:
            maxLength = position
            
    #print arr
    #print inc_sub,maxLength
    #print parent
    
    result = []
    position = inc_sub[maxLength]
    #print position, arr[6]
    for j in xrange(maxLength):
       # print arr[position]
       # result.append(arr[position])
        result = [arr[position]] + result
        position = parent[position]
        
    return result


''' Find Max Sum longest increasing sub sequence in given array 
    Time complexity - O(n^2)
    Space -> O(2n) -> O(n)
'''


def findMaxSumLongIncSubSeq(arr):
    if len(arr) <1:
        return
    sumSubSeq = deepcopy(arr)
    parPoint = [None]*len(arr)
    
    for i in xrange(1,len(arr)):
        for j in xrange(i):
            if arr[j] < arr[i]:
                if (sumSubSeq[j] + arr[i]) > sumSubSeq[i] : 
                    sumSubSeq[i] = sumSubSeq[j] + arr[i]
                    parPoint[i] = j 
                
    #print arr
    #print sumSubSeq
    #print parPoint
    
    #found index of max sum -> That gives last element of subsequence index and parPoint gives previous
    #elements sequence  
    position = sumSubSeq.index(max(sumSubSeq))
    result = []
    while  (position!= None):
        #print position,
        result.append(arr[position])
        #print result ,
        position = parPoint[position]
        #print position
    
    #print result[::-1]
    
    return result[::-1]



def main():
    
    # Finding max sum sub array
    print "--------Finding max sum of sub array and start and end index of it------------"
    findMaxSumSubArray([1,-3,2,1,-1])
    findMaxSumSubArray([-2,3,2,1,-1])
    findMaxSumSubArray([-1,-2,3,4,-5,6])        
    
    
    # Finding peek element in unsorted array
    print "Peek element - > ",findPeekElement([3,4,5,12,7,6,15,16,1])
    
    #Find element that has frequency 1/4 of the total elements in array
    arr = [1,1,1,1,2,2,3,4,4,4,5,5]
    count ={}
    print "1/4 th time present element - >", findOneFourthLengthElement(arr, 0, len(arr)-1, count)
    
    # Find longest increasing sub sequence
    l = [3,1,5,2,4,9]
    
    print "longest inc sub sequence - >",findLongesIncreasingSubsequence(l)
    
    # Find max sum longest increasing sub sequence
    print "Max Sum Sequence ->",findMaxSumLongIncSubSeq(l)


if __name__ == '__main__':
    main()