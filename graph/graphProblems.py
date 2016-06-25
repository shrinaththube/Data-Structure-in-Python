'''
Created on Jun 11, 2016

@author: Shrinath
'''
from _collections import deque

class Graph(object):
    ''' reference - GeeksforGeeks'''
    def findMinHeightTrees(self, n, edges):
        graph = [[] for i in range(n)]
        print graph
        for v1, v2 in edges:
            print v1,v2
            graph[v1].append(v2)
            graph[v2].append(v1)
            print graph
        print
        p1 = self.FindLongestPath(graph, 0)
        print "p1",p1
        p2 = self.FindLongestPath(graph, p1[-1])
        print "p2 - ",p2

        if len(p2) % 2: return [p2[len(p2)/2]]
        else:           return [p2[len(p2)/2 - 1], p2[len(p2)/2]]

    def FindLongestPath(self, graph, root):
        print "longest pathss"
        queue = deque([[root]])
        traversed = set([root])
        while queue:
            path = queue.pop()
            print path , graph, graph[path[-1]]
            for v in graph[path[-1]]:
                print "  ",v,
                if v not in traversed:
                    print path + [v],
                    queue.appendleft(path + [v])
                    print queue,
                    traversed.add(v)
                print traversed
        return path
    
g1 = Graph()
'''n = 4
edges = [[1, 0], [1, 2], [1, 3]]
print edges
print g1.findMinHeightTrees(n, edges)'''
print "\n second-------------------------------\n"
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print edges
print g1.findMinHeightTrees(n, edges)