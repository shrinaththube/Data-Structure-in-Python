'''
Created on Aug 5, 2016

@author: Shrinath Thube
'''
from copy import deepcopy
import pprint 
import dis


'''
         0 1 2 3
      0  - - - q
      1  - q - -
      2  - - - q
      3  - q - -
'''

def nQueensValidPosition(q_num):
    validQPos = [[] for i in xrange(q_num)]
    dis = [["-" for j in xrange(q_num)] for i in xrange(q_num)]
    result = []
    graph = []
    #pprint.pprint(dis)
    pprint.pprint(nQueensValidPositionBackTrack(0, validQPos,result,dis,graph), indent=4, width=20) 

def nQueensValidPositionBackTrack(level,validQPos,result,dis,graph):
    if level == len(validQPos):
        '''
        if isSafe(validQPos,level,col):
            validQPos[level]+[level,col]
            return validQPos'''
        #print level, validQPos
        result.append(deepcopy(validQPos))
        #print dis
        temp = [" ".join(value) for value in dis]
        #print temp
        graph.append(temp)
        #print result
        return
    
    for col in xrange(len(validQPos)):
        
        if isSafe(validQPos,level,col):
            validQPos[level]= [level,col]
            dis[level][col] = "Q" 
            #print level,col,validQPos
            nQueensValidPositionBackTrack(level + 1, validQPos,result,dis,graph)
            dis[level][col] = "-"
            #validQPos[level] = []
    return graph

def isSafe(validQPos,level,col):
    #print level
    for i in range(level):
        #print validQPos
        if validQPos[i][0] == level or validQPos[i][1] == col or ((validQPos[i][0] - validQPos[i][1]) == (level - col)) or ((validQPos[i][0] + validQPos[i][1]) == (level + col)):
            return False
    return True

nQueensValidPosition(8)