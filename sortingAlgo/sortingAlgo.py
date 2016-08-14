'''
Created on Aug 13, 2016

@author: Shrinath Thube
'''

def mergerSort(arr):
    if len(arr)< 2: return
    
    mid = len(arr)/2
    left = arr[:mid]
    right = arr[mid:]
    
    mergerSort(left)
    mergerSort(right)
    
    merge(arr,left,right)
    
def merge(arr,left,right):
    i = 0
    j = 0
    k = 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
            k+=1
        else:
            arr[k] = right[j]
            j+=1
            k+=1
    
    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    
    while j<len(right):
        arr[k] = right[j]
        j+=1
        k+=1

def quickSort(arr,start,end):
    if start>end: return
    
    pivInd = partition(arr,start,end)
    quickSort(arr, start, pivInd-1)
    quickSort(arr, pivInd+1, end)

def partition(arr,start,end):
    if start>=end: 
        return start
    piv = arr[end]
    i = start
    j = end -1
    while i<j:
        while arr[i] < piv:
            i+=1
        while arr[j] > piv:
            j-=1
        if i < j :
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i] >= arr[end]:
        arr[end] = arr[i]
        arr[i] = piv
    else:
        i = end
    return i        

def bubbleSort(arr):
    if len(arr)<1: return
    flag = True
    for i in xrange(len(arr)):
        for j in xrange(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                flag = False
        if flag:
            break
    return arr

def sectionSort(arr):
    if len(arr)<1:
        return
    
    for i in xrange(len(arr)):
        small = i
        for j in xrange(i+1,len(arr)):
            if arr[j] < arr[small]:
                small = j
        arr[i],arr[small] = arr[small],arr[i]
    return arr

def insertionSort(arr):
    if len(arr)<1: return
    
    for i in xrange(1,len(arr)):
        pos = i
        ele = arr[i]
        for j in reversed(xrange(i)):
            if arr[j] > ele:
                arr[j+1] = arr[j]
                pos = j
        arr[pos] = ele  
    return arr

arr = [ 2, 1,4,5, 3, 7, 6]
arr1 = [4,3,7,2,9,1,0,2,3,12,17,11]

mergerSort(arr)
quickSort(arr, 0, len(arr)-1)
print arr

quickSort(arr1, 0, len(arr1)-1)
print arr1

print bubbleSort(arr)

print sectionSort(arr1)

print insertionSort(arr)