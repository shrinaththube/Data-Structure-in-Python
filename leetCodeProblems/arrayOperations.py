'''
Created on Jun 26, 2016

@author: Shrinath Thube
'''
"""
    ************************* Array Operations ********************************
    Following problems are covered in this module
    
    1) Find the max sum sub array by Kadane's Algorithm
    2) Find any peek element in given unsorted array or list.
    3) Find element that came minimum 1/4 th times total elements in sorted array
    4) Find longest increasing sub sequence in given array
    5) Find Max Sum longest increasing sub sequence in given array
    6) Find minimum jumps to reach at the end of array
    7) Find minimum jumps to reach at the end of array by Dynamic Programming
    8) Find the next high / greater element of every element of array
    9) Find the majority element in given array if any or return None
   10) Merge K sorted arrays in O(nlogk)
   11) Merge K sorted arrays by iterative way

    ***************************************************************************
""" 

from copy import deepcopy


''' Find the max sum sub array 
    Kadane's Algorithm 
    Time complexity - O(n)
    Space complexity - O(1)
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
  
        current_max = max((arr[i]+ current_max), arr[i]) 
        
        if current_max > global_max:
            global_max = current_max
            end = i

    #print "start ->",start,"end ->", end,"sub array -> ", arr[start:end+1],global_max
    return (arr[start:end+1],global_max)


''' Find any peek element in given unsorted array or list. 
    Time complexity - O(log n) - Binary search algorithm
    space complexity - O(1)
'''
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
        

''' Find element that came minimum 1/4 th times total elements in sorted array
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
        #print i,position, start, parent, inc_sub
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


''' Minimum jumps to reach at end of array
    Ladder and stairs approach in Linear time
    Time complexity - O(n) 
    space complexity - O(1)
    '''
def minHopToEndOfArr(arr):
    if len(arr)<1:return
    if arr[0] < 1: return None
    ladder = arr[0]
    stairs = arr[0]
    i =1
    jump =1
    while i<len(arr):
        stairs -=1
        if arr[i] + i> ladder :
            ladder = arr[i] + i        
        if stairs <1  and ladder - i <1: return None #edge case when value encounter is 0
        if stairs <1:
            stairs = ladder - i
            jump +=1
        if stairs +i  >= len(arr): return jump
        i+=1
    return jump


''' Minimum jumps to reach at the end of array by Dynamic Programming
    Time complexity - O(n^2) 
    space complexity - O(n)
    '''
def minHopToEndOfArrByDP(arr):
    if len(arr)<1:return
    if arr[0] < 1: return None
    jump = [None for i in xrange(len(arr))]

    jump[0] = 0
    #print jump
    for i in xrange(len(arr)):
        if jump[i] == None or arr[i] < 0: return None
        
        for j in xrange(i+1,arr[i] +i +1):
            if j >= len(arr): break
            if jump[j] == None:
                jump[j] = jump[i] + 1
            elif jump[j] > jump[i] + 1:
                jump[j] = jump[i] + 1

    return jump[len(arr) -1]

''' Find the next high element of every element of array
    Time complexity - O(n)
    Space complexity - O(n)
'''
def nextGreaterElementList(arr):
    if len(arr) < 1: return
    
    greaterEle = {}
    
    st = list()
    st.append(arr[0])
    for i in xrange(len(arr)):
        if st[-1] >= arr[i]:
            st.append(arr[i])
        else:
            while arr[i] > st[-1]:
                greaterEle[st.pop()] = arr[i]
            st.append(arr[i])
            
    while st:
        greaterEle[st.pop()] = None
    return greaterEle

''' Find the majority element in given array if any or return None
    Boyer-Moore Vote algorithm
    Time - O(n)
    Space - O(1)
'''

def findMajorityElement(arr):
    if len(arr) < 1: return
    
    majEle = arr[0]
    count = 0
    # find majority element
    for ele in arr:
        if count == 0:
            majEle = ele
            count +=1
        else:
            if ele == majEle:
                count +=1
            else:
                count -=1
    # check if it is majority element
    count = 0
    for ele in arr:
        if ele == majEle:
            count +=1
    if count >= len(arr)/2:
        return majEle
    else:
        return None


''' Merge K sorted arrays in O(nlogk)
    Used merge sort approach
    Time - O(nlogk)
    Space - O(n)
'''

def mergeKArrays(listOfArray):
    if not listOfArray:
        return
    #print "Now in mergeKArray"
    return mergeSortPartion(listOfArray, 0, len(listOfArray)-1)
    
def mergeSortPartion(listOfArray,start,end):
    if start > end: return None
    if start == end: return listOfArray[start]
    elif start < end:
        mid = (start + end) / 2
            
        leftPart = mergeSortPartion(listOfArray, start, mid)
        #print "leftpart -->", leftPart
        rightPart = mergeSortPartion(listOfArray, mid + 1, end)
        #print "rightpart -->",rightPart
            
        return merge(leftPart,rightPart)
    
def merge(leftPart, rightPart):
    #print "in merge"
    if len(leftPart)<1 or len(rightPart)<1: return None
    i = 0 
    j = 0
    auxArray = []
    while i<len(leftPart) and j<len(rightPart):
        if leftPart[i] < rightPart[j]:
            auxArray.append(leftPart[i])
            i+=1
        else:
            auxArray.append(rightPart[j])
            j+=1
        
    if i<len(leftPart):
        auxArray+=leftPart[i:]
    if j<len(rightPart):
        auxArray+=rightPart[j:]
    #print "auxarray -> ",auxArray
    return auxArray

'''  Merge K sorted arrays
    Used iterative way. Merged one by one
    Time - O(nk)
    Space - O(n)
    
    example - 
          l1 &2 = 1,2,4,5,6,7,8,9,9,10,13
                   = 1,2,3,4,5,6,6,7,8,9,9,10,11,13,14
                    = 1,2,3,4,5,6,6,7,7,8,9,9,10,11,12,13,13,14
    
'''

def mergeKArrayByIterative(listOfArray):
    mergeL =[]
    for l in listOfArray:
        if len(mergeL) <1 :
            mergeL = l
            continue
        mInd = 0 
        lInd = 0
        newMerge = []
        while mInd < len(mergeL) and lInd < len(l):
            if mergeL[mInd ] < l[lInd]:
                newMerge.append( mergeL[mInd ] )
                mInd +=1
            else:
                newMerge.append( l[lInd] )
                lInd +=1
        if mInd < len(mergeL):
            newMerge += mergeL[mInd:]
    
        if  lInd < len(l):
            newMerge += l[lInd:]
        mergeL = newMerge        
    
    return mergeL

#"""
def main():
    
    # Finding max sum sub array
    print "--------Finding max sum of sub array and start and end index of it------------"
    print "sub array and max sum-> ",findMaxSumSubArray([1,-3,2,1,-1])
    print "sub array and max sum-> ",findMaxSumSubArray([-2,3,2,1,-1])
    print "sub array and max sum-> ",findMaxSumSubArray([-1,-2,3,4,-5,6])        
    
    
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

    # Find minimum jumps needed to reach at end of array by Ladder and stairs
    arr = [1,4,2,3,7,5,6,7,10]
    print "Minimum jumps needed by Ladder and Stairs-> ", minHopToEndOfArr(arr)

    # Find minimum jumps needed to reach at end of array by DP
    #arr = [1,4,2,3,7,5,6,7,10]
    print "Minimum jumps needed by DP-> ", minHopToEndOfArrByDP(arr)
    
    # Find next Greater Element List
    elements=[94,52,27,56,2,7]
    print nextGreaterElementList(elements)
    
    # Find majority element
    numbers = [1,2,2,3,2,4,2,2,1,1,2,3]
    print "Majority element in given array ->", findMajorityElement(numbers)

    # merge k sorted arrays    
    '''
              l1 &2 = 1,2,4,5,6,7,8,9,9,10,13
                       = 1,2,3,4,5,6,6,7,8,9,9,10,11,13,14
                        = 1,2,3,4,5,6,6,7,7,8,9,9,10,11,12,13,13,14
    '''
    
    l1 = [1,5,9,13]      
    l2 = [2,4,6,7,8,9,10]       
    l3 = [3,6,11,14]               
    l4 = [7,8,12,13]
    
    kList = [l1,l2,l3,l4]
    print "Merge k list --> " , kList
    print "-----------merge by merge sorting method-----------------------"
    print mergeKArrays(kList)
    print "-----------merge by iterative method----------------------------"
    print mergeKArrayByIterative(kList)


if __name__ == '__main__':
    main()
    #"""