'''
Created on Aug 9, 2016

@author: Shrinath Thube
'''

''' Wiggle sort in O(nlogn)
    Sort array using quick or merge sort and then insert half elements with first one 
    Time complexity - O(nlogn)
    Space complexity - O(n)
'''

def wiggle_sort(arr):
    if len(arr) < 1: return
    
    #sort in ascending order
    arr.sort()

    mid = len(arr) / 2
    
    i =0
    j = mid
    wiggle_arr =[]
    while i< mid and j < len(arr):
        wiggle_arr.append(arr[i])
        wiggle_arr.append(arr[j])
        i+=1
        j+=1
        
    #print i, j, arr, wiggle_arr
    if j < len(arr):
        if arr[j-2] < arr[j-1] and arr[j-1] < arr[j]:
            #wiggle_arr.append(arr[j])
            wiggle_arr.append(arr[j])
            wiggle_arr[j-1],wiggle_arr[j] = wiggle_arr[j],wiggle_arr[j-1]
        else:
            #wiggle_arr.append(arr[j-1])
            wiggle_arr.append(arr[j])
            
    return wiggle_arr

''' Wiggle sort in linear time O(n)
    Concentrating only on even indices of array and try to make them greater than previous or next index. If not swap it. 
    Time complexity - O(n)
    Space complexity - O(1)
'''

def wiggleSort(arr):
    for i in range(1,len(arr),2):
        #print i
        if arr[i-1] > arr[i]:
            arr[i],arr[i-1] = arr[i-1],arr[i]
        if i<len(arr)-1 and arr[i] < arr[i+1]:
            arr[i],arr[i+1]= arr[i+1],arr[i]
        i+=1
    return arr
            
arr = [1,2,3,4,5,7,6]
arr1 = [1,3,2,2,3,1]

wiggle_sort(arr)

print wiggleSort(arr1)

