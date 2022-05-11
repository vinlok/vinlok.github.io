from collections import defaultdict
from re import S

class Graph():


    def __init__(self,edges,s,d):
        self.edges=edges
        self.adj_list=defaultdict(list)
        self.UpdateAdjList()
        self.s=s 
        self.d=d

    def UpdateAdjList(self):
        for edge in self.edges:
            self.adj_list[edge[0]].append(edge[1])
            
    def check_path_exists(self,s,d):
        
        queue=[]
        visited=[]
        queue.append(s)
        while len(queue) > 0:
            curVertex=queue.pop()
            for n in self.adj_list[curVertex]:
                if n == d:
                    return True
                if n not in visited:
                    queue.append(n)
                    visited.append(n)
        return False  












edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]

o=Graph(edges,0,5)
print(o.check_path_exists(0,2))
# o.UpdateAdjList()