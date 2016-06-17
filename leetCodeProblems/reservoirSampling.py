'''
Created on Jun 17, 2016

@author: Shrinath Thube
'''

import random


''' -------------------- GeeksForGeeks ----------------------------------------- 
If there is streaming data that can not fit in to memory. Then first decide the return data size. 
Fill it with stream data as it is first k elements. Then iterate the new coming data and compare the 
parameters with the filled data and replace better data with those one '''
def randomKsamples(streamData,k):
    if k<1 : return
    
    n  =  len(streamData) #len of laege data or we can keep as undefine
    
    if n< 1 : return
    
    reservoir = [streamData[i] for i in xrange(k)]
    
    for i in xrange(k,n):
        r = random.randint(0,n) % (i +1) # random index  0 to i
        if r< k:
            reservoir[r],streamData[i] = streamData[i],reservoir[r] #swap first k with stream data after k
    return reservoir

streamData = [1,2,3,4,5,6,7,8,9,10]
print "Stream data = ", streamData        
print "k random result = ", randomKsamples(streamData, 4)