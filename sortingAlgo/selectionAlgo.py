'''
Created on Aug 9, 2016

@author: Shrinath Thube
'''
import random
from math import floor

"""
''' Find kth smallest element using quick Select algorithm
    No need to sort the array and the find that element. It is also called partial select sort algo. It partialy sorted array.
    Time complexity - O(n)
    Space complexity - O(1)
'''
def quickSelect(arr,start,end,k):
    if len(arr) < 1: 
        print "Array is empty"
        return
    if start > end: 
        print "start > end... Invalid condition"
        return
    
    if k > len(arr): 
        print "k is larger than length of array"
        return
    print arr, start, end, k
    while start < end:
        
        #pivInd = (start + end)/2
        #print start,end,pivInd
        
        pivInd = partitionInd(arr,start,end)
        print arr,"s -", start,"e -", end,"k-",k,"pivIN -",pivInd
        if pivInd-start == k-1: 
            
            return arr[k-1]
        
        if pivInd-start < k-1:
            start = pivInd + 1
        else:
            end = pivInd - 1
            
    
    #print arr, start,end ,k
    return arr[start-1]


def partitionInd(arr,start,end):
    
    piv = arr[end]
    
    i = start
    #j = end-1
    print "I am in partition"
    print arr,start,end,piv
    partInd = start
    
    while i<= end-1:
        if arr[i]<= piv:
            arr[i], arr[partInd] = arr[partInd], arr[i]
            partInd +=1
        i+=1
    arr[end], arr[partInd] = arr[partInd], arr[end]
    print "end of partiitona"
    return partInd
    
    
arr = [1, 4, 2, 5, 3, 6]
arr1 =[12, 3, 5, 7, 4, 19, 26]
print quickSelect(arr, 0, len(arr)-1, 4)
        
"""


def medianOfMedian(arr,start,end,pos):
    print start,end, arr
    if end-start + 1 <= 5:
        first=[]
        sec=[]
        third=[]
        if start ==0:
            sec = sorted(arr[:end+1])
            third = arr[end+1:]
            #arr = sorted(arr[:end+1]) + arr[end:]
        elif end == len(arr)-1:
            first = arr[:start]
            sec = sorted(arr[start:end+1])
            #arr = arr[:start-1] + sorted(arr[start:end+1])
        else:
            first = arr[:start]
            sec = sorted(arr[start:end+1])
            third = arr[end:]
            #arr = arr[:start-1] + sorted(arr[start:end+1]) + arr[end:]
        print first,sec,third
        arr = first + sec + third
        print start,end, arr
        return start + pos - 1
    for i in range((end+1)/5):
        left = 5*i
        right = left + 4
        if right > end: 
            right = end
        med = medianOfMedian(arr,left,right,3)
        arr[med],arr[i] = arr[i],arr[med]
        
    return medianOfMedian(arr,0,(end+1)/5,(end+1)/10)

def select(L):
    if len(L) < 10:
        L.sort()
        return L[int(len(L)/2)]
    S = []
    lIndex = 0
    while lIndex+5 < len(L)-1:
        S.append(L[lIndex:lIndex+5])
        lIndex += 5
    S.append(L[lIndex:])
    Meds = []
    for subList in S:
        print(subList)
        Meds.append(select(subList))
    L2 = select(Meds)
    L1 = L3 = []
    for i in L:
        if i < L2:
            L1.append(i)
        if i > L2:
            L3.append(i)
    if len(L) < len(L1):
        return select(L1)
    elif len(L) > len(L1) + 1:
        return select(L3)
    else:
        print L
        return L2
medArray = [1,2,5,7,6,3,4,9,8,10,12,11,17,13,15]
#print medArray
#print medianOfMedian(medArray, 0, len(medArray)-1, (len(medArray))/2)
print select(medArray)

'''
int select(int *a, int s, int e, int k) {
if(e-s+1 <= 5)
{
    sort(a+s, a+e);
    return s+k-1;
}

for(int i=0; i<(e+1)/5; i++)
{
    int left = 5*i;
    int right = left + 4;
    if(right > e) right = e;

    int median = select(a, left, right, 3);
    swap(a[median], a[i]);
}
return select(a, 0, (e+1)/5, (e+1)/10); }

int main() 
{  
int a[] = {6,7,8,1,2,3,4,5,9,10};
int n = 10;

int mom = select(a, 0, n-1, n/2);
cout<<"Median of Medians: " << a[mom] << endl;
return 0; }
'''
    
