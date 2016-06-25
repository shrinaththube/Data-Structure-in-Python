'''
Created on Jun 17, 2016

@author: Shrinath Thube

'''


class Vertex(object):
    
    def __init__(self,lable):
        self.lable = lable
        self.adjacent_vert = {}
        self.visit_Status = False
        
    def __str__(self):
        return str(self.lable) + ' adjacent : ' + str([v.lable for v in self.adjacent_vert]) 
            
    def get_lable(self):
        return self.lable
    
    def set_lable(self,lable):
        self.lable = lable
        
    def add_adjacent_vert(self,vert, weight = 0):
        self.adjacent_vert[vert] = weight
    
    def show_connections(self):
        return self.adjacent_vert.keys()
    
    def get_weight(self,neighbor):
        return self.adjacent_vert[neighbor]
    
    def is_visited(self):
        return self.visit_Status
    
    def set_visit_status(self, status):
        self.visit_Status = status
        
    def has_no_connections(self):
        if len(self.adjacent_vert) == 0: return True
        return False
        

class Graph(object):
    
    def __init__(self):
        self.vert_dict = {}
        self.numberOfvert = 0
       
    def __iter__(self):
        return iter(self.vert_dict.values())
    
    def add_vertices(self,vert):
        newVert = Vertex(vert)
        self.vert_dict[vert] = newVert
        self.numberOfvert +=1
        
    def add_edges(self,start, end, wt=0):
        if start not in self.vert_dict:
            self.add_Vertices(start)
        if end not in self.vert_dict:
            self.add_Vertices(end)
        self.vert_dict[start].add_adjacent_vert(self.vert_dict[end],wt)
        #self.vert_dict[end].add_adjacent_vert(self.vert_dict[start],wt)
        
    def create_directed_graph(self,vertexList, edgeList):
        for vert in vertexList:
            self.add_vertices(vert)
        
        if len(edgeList[0]) == 2:
            for start,end in edgeList:
                self.add_edges(start, end)
                
        elif len(edgeList[0]) == 3:
            for start,end,wt in edgeList:
                self.add_edges(start, end, wt)
    
    def create_undirected_graph(self,vertexList, edgeList):
        for vert in vertexList:
            self.add_vertices(vert)
        
        if len(edgeList[0]) == 2:
            for start,end in edgeList:
                self.add_edges(start, end)
                self.add_edges(end, start)
                
        elif len(edgeList[0]) == 3:
            for start,end,wt in edgeList:
                self.add_edges(start, end, wt)
    
    def dfs_traversal(self,vert):
        #if vert.has_no_connections(): return
        print vert.lable,
        for v in vert.adjacent_vert:
            if not v.is_visited(): 
                v.set_visit_status(True)
                self.dfs_traversal(v)
        
        #print vert.lable,
            
        
    
    def bfs_traversal(self,graph):
        pass

graph1= Graph()

vertexList = [0,1,2,3,4]
edgeList = [(0,1),(0,2),(0,3),(1,3),(1,4),(2,4),(3,4)]


graph1.create_directed_graph(vertexList, edgeList)


'''
graph1.add_vertices(0)
graph1.add_vertices(1)
graph1.add_vertices(2)
graph1.add_vertices(3)
graph1.add_vertices(4)

graph1.add_edges(0, 1)
graph1.add_edges(0, 2)
graph1.add_edges(0, 3)
graph1.add_edges(1, 3)
graph1.add_edges(1, 4)
graph1.add_edges(2, 4)
graph1.add_edges(3, 4)

graph1.add_vertices('a')
graph1.add_vertices('b')
graph1.add_vertices('c')
graph1.add_vertices('d')
graph1.add_vertices('e')

graph1.add_edges('a', 'b')
graph1.add_edges('a', 'c')
graph1.add_edges('a', 'd')
graph1.add_edges('b', 'd')
graph1.add_edges('b', 'e')
graph1.add_edges('c', 'e')
graph1.add_edges('d', 'e')
'''


for v in graph1:
    print v

graph1.create_undirected_graph(vertexList, edgeList)

for v in graph1:
    print v


print graph1.vert_dict[0]

graph1.dfs_traversal(graph1.vert_dict[0])
