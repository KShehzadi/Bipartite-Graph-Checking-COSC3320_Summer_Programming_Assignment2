
# class of Graph to implement all the graph related functions
class Graph():
     # init function to declare class variables 
    def __init__(self,V): 
        self.V = V 
        self.edges = [[] for i in range(V)]
    # addEdge function to add the edges of graph
    def addEdge(self, v, w):
        if w not in self.edges[v]:
            self.edges[v].append(w)
        if v not in self.edges[w]:
            self.edges[w].append(v) 
    def DFSUtil(self, temp, v, visited): 
  
        # Mark the current vertex as visited 
        visited[v] = True
  
        # Store the vertex to list 
        temp.append(v) 
  
        # Repeat for all vertices adjacent 
        # to this vertex v 
        for i in self.edges[v]: 
            if visited[i] == False: 

                # Update the list 
                temp = self.DFSUtil(temp, i, visited) 
        return temp 
   
    # function to count connected components of the graph
    def NumberofconnectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        #given graph
        givengraph = Graph(len(graph));
        givengraph.edges=graph;
        # formation of G' graph
        gprime= Graph(len(graph)*2)
        i=0;
        for x in graph:
            for y in x:
                gprime.addEdge(i, y+len(graph))
                gprime.addEdge(y, i+len(graph))
            i=i+1;
        # number of connected components in given graph
        glength=len(givengraph.NumberofconnectedComponents())
        # number of connected components in formed graph by the algo
        gprimelength =len(gprime.NumberofconnectedComponents())
        
        # checking the condition of bipartiteness and returning the result
        if glength*2== gprimelength:
            return 1;
        else:
            return 0;
        
# driver program
# testing for 1st graph in assignment
g = Graph(4)
# name of vertices is shown by digits Graph(4) produces a graph with vertices 0 to 3
# Adding edges for the first graph
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2, 3)
s = Solution()
s.isBipartite(g.edges)