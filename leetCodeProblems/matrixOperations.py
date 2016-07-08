'''
Created on Jul 3, 2016

@author: Shrinath Thube
'''
"""
    ************************* Matrix Operations *******************************
    Following problems are covered in this module
    
    1) Knapsack Algorithm by recursive naive approach
    2) Knapsack Algorithm by Dynamic Programming approach
    3) find count of negative elements in matrix
    4) Search the element in sorted matrix
    5) Find minimum cost path from left most corner (0,0) to right low corner (last,last) of matrix
  
    ***************************************************************************
""" 




from copy import deepcopy


''' Knapsack by recursive naive approach
    Time complexity - O(2^n) exponential
    space - O(1)
'''
def knapsack(value,wt, cost,num):
        if num == 0 or cost == 0:
            return 0
        if wt[num-1] > cost:
            return knapsack(value,wt,cost, num-1)
        else:
            pick = value[num-1] + knapsack(value,wt,cost-wt[num-1],num-1)
            nope = knapsack(value,wt,cost,num-1)
            return max(pick,nope)
        
        
''' Knapsack by Dynamic Programming approach
    Time complexity - O(2^n) exponential
    space - O(1)
'''
def knapsackDP(valueList, wtList, wtRemaing,pos):
    
    KnapMat = [[0 for i in range(wtRemaing +1)] for j in range(wtRemaing+1)]
    
    for p in range(1,pos+1):
        for w in range(1,wtRemaing+1):
            if wtList[p-1] <= w:
                KnapMat[p][w] = max(valueList[p-1] + KnapMat[p-1][w-wtList[p-1]],  KnapMat[p-1][w])
            else:
                KnapMat[p][w] = KnapMat[p-1][w]
 
    # print K
    return KnapMat[pos][wtRemaing]
    
    
# Trying to use matrix in recursive solution to store intermediate results    
#     global mat
#     if cost ==0 or num ==0:
#         return 0
# 
#     if mat[num-1][cost-1] != None: return mat[num-1][cost-1]
#     
#     if wt[num-1] > cost:
#         return knapsack(value,wt,cost, cost, num-1,mat)
#     
#     else:
#         pick = value[num-1] + knapsackDP(value,wt,cost  - wt[num-1],num-1)
#         nope = knapsackDP(value,wt,cost,num-1)
#         result =  max(pick,nope)
#         mat[num-1][cost-1] = result
#         return result


''' Find minimum cost path from left most corner (0,0) to right low corner (last,last) of matrix
    row = m , col = n
    Time complexity - minCostMatrix formation - O(m * n) 
                      finding path - O(m + n) 
    Space complexity - O(m * n)
'''
def minCostPathInMatLtoR(mat):
    
    minCostMat = deepcopy(mat)
    
    for i in xrange(len(minCostMat)):
        for j in xrange(len(minCostMat[0])):
            if i==0 and j==0: continue
            if i==0:  #Added row 0 elements
                minCostMat[i][j] += minCostMat[i][j-1]
            elif j==0: # added column 0 elements
                minCostMat[i][j] += minCostMat[i-1][j]
            else: # for all other cells
                minCostMat[i][j] += min(minCostMat[i-1][j],minCostMat[i][j-1])  
                
            #print i,j,minCostMat
    path = []
    i = len(minCostMat)-1
    j = len(minCostMat[0])-1
    while i!=0 or j!=0:
        path.append(mat[i][j])
        if i!=0 and j!=0:
            if minCostMat[i][j-1] < minCostMat[i-1][j]:
                j -=1
            else:
                i -=1
        elif i==0: j-=1
        elif j==0: i-=1
    path.append(mat[0][0])
    return path[::-1]
    #print minCostMat

''' Search the element in sorted matrix
    Time complexity - O(m + n)
    Space complexity - O(1)
'''    
def searchElementInSortedMat(mat,ele):
    if len(mat) < 1: return
    
    # keep both in right most corner
    row = 0
    col = len(mat[0])-1
    # if element is greater then move down else move left
    while row < len(mat) and col >-1:
        if mat[row][col] == ele:
            return (row,col)
        elif mat[row][col] <= ele:
            row = row +1
        else:
            col = col - 1
            
    return None


''' find count of negative elements in matrix
    Time complexity - O(n)
    Space complexity - O(1)
''' 
def findNegativeElementsInSortedMat(mat):
    if len(mat)< 1: return
    # Start at most right corner
    row = 0
    col = len(mat[0])-1
    count = 0
    
    while col > -1 and row < len(mat):
        if mat[row][col] < 0:
            count += col +1
            row +=1
        else:
            col -=1

    return count

def main():

    wtList = [1,2,4,2,5]
    valueList =  [5,3,5,3,2]
    totalWt = 10
    
    print "total value for weight {} by recursive ->".format(totalWt),knapsack(valueList, wtList, totalWt, len(valueList))
    print "total value for weight {} by DP ->".format(totalWt), knapsackDP(valueList, wtList, totalWt, len(valueList))
    
    # Find minimum cost path from left most corner to right low corner
    mat = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    
    print "minimum cost path from left corner to right corner - >",minCostPathInMatLtoR(mat)
    
    # Find location of element in sorted array
    print "element present at ->",searchElementInSortedMat(mat, 4)
    
    # Find count of negative elements in sorted mat
    matNegative= [[-7,-6,-4, 2],
                  [-3,-2, 3, 4],
                  [ 5, 6, 7, 8]  ]
    print "Negative number count in matrix - >", findNegativeElementsInSortedMat(matNegative)

if __name__ == '__main__':
    main()