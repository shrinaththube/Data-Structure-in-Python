'''
Created on Jul 6, 2016

@author: Shrinath Thube
'''

"""
    ************************* Histogram Area **********************************
    Following problems are covered in this module
    
    1) Find the maximum rectangle area formed by given histogram
    
    ***************************************************************************
""" 

''' Find the maximum rectangle area formed by given histogram
    Time complexity - O(n)
    Space complexity - O(n)
'''

def maxRecatangleAre(histo):
    if len(histo) <1: return
    st = list()
    st.append(0)
    i =1
    current_area = 0
    result_area = 0
    while i< len(histo):
        if histo[st[-1]]<histo[i]:
            st.append(i)
        else:
            pos = st.pop()
            
            if len(st) < 1: #stack is empty
                current_area = histo[pos] * i
            else:
                current_area = histo[pos] * (i - st[-1] -1 )
                print pos, current_area,histo[pos] , i,  st[-1] 
            st.append(i)    
        if current_area > result_area:
            result_area = current_area
        
        # print i,st, current_area, result_area
        i+=1
     
    print len(st)   
    while st:
        pos = st.pop()
        print pos,
        if len(st) < 1:
            current_area = histo[pos] * i
            print current_area
        else:
            current_area = histo[pos] * (i - st[-1] -1)
            print current_area ,histo[pos] , i,  st[-1]
                
        if current_area > result_area:
            result_area = current_area
            
    return result_area    

def main():    
    histo = [1,2,1,3,2,4]
    #histo = [1,2,3,2]
    histo = [1,1,1,1]
    print maxRecatangleAre(histo)
    
if __name__  =='__main__':
    main()