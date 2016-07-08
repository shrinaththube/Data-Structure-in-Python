'''
Created on Jun 3, 2016

@author: Shrinath Thube
'''
"""
    ************************* Rain water Trapping *****************************
    Following problems are covered in this module
    
    1) Solution for Trapping Rain Water problem
    
    ***************************************************************************
""" 




''' Solution for Trapping Rain Water problem 
    Time complexity - O(n)
    Space complexity - O(n)
'''
class TrapRW(object):
    
    def totalRainWater(self,arrHeight):
        #edge case - if list is empty
        if len(arrHeight) == 0:
            print "Array is invalid"
            return None
        
        #list of max height surface
        sur = []
        mHeight = arrHeight[0]
        sur.append(arrHeight[0])
        
        #keeping maximum height by cumulative way
        for ele in arrHeight[1:]:
            mHeight = max(ele,mHeight)
            sur.append(mHeight)
            
        mHeight = arrHeight[-1]
        sur.reverse()
        arrHeight.reverse()
        
        watReserve = 0
        for ind,ele in enumerate(arrHeight): #start scan from second last element
            mHeight = max(ele,mHeight)
            sur[ind] = min(mHeight,sur[ind])
            #watReserve += sur[ind] - ele # final result can be calculate here
        
        #final output is summation of height difference between surface/boundary of tall buildings height and
        # original height in list at particular position
        for ele1,ele2 in zip(sur,arrHeight):
            watReserve += ele1 - ele2
        
        return watReserve
         
if __name__ == '__main__':
    #object of TrapRW class
    obj = TrapRW()
    hightOfBuildings = [0,1,0,2,1,0,1,3,2,1,2,1]
    print "total trapped water reservior =" ,obj.totalRainWater(hightOfBuildings)