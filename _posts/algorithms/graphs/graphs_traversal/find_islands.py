from collections import defaultdict

class island():

    def __init__(self,a):
        self.visited=defaultdict(lambda : False)
        self.stack=[]
        self.area=a
        self.rows=len(self.area)
        self.cols=len(self.area[0])
        self.island_count=0

    def check_adjacent_node(self,r,c):
        self.visited[(r,c)] = True
        if self.area[r][c] == 1:
            self.stack.append((r,c))

    def find_island(self):
        
        while len(self.stack) > 0:
            print(self.stack)
            r,c=self.stack.pop()
            
            #check if right side is land and not visited if yes, add for scaning
            if c+1 < self.cols and not self.visited[(r,c+1)]:
                self.check_adjacent_node(r,c+1)
            
            if c > 0 and not self.visited[(r,c-1)]:
                self.check_adjacent_node(r,c-1)
            
            if r+1 < self.rows and not self.visited[(r+1,c)]:
                self.check_adjacent_node(r+1,c)
            
            if r > 0 and not self.visited[(r-1,c)]:
                self.check_adjacent_node(r-1,c)


    def driver_prog(self):

        for r in range(self.rows):
            for c in range(self.cols):
                if self.visited[(r,c)] == False:
                    self.visited[(r,c)] = True
                    if self.area[r][c]==1:
                        self.island_count+=1
                        self.stack.append((r,c))
                        print(self.stack)
                        self.find_island()
                        print(self.island_count)
                        print(self.visited)
        
        










a=[[1,1,0,0,1],
    [1,1,0,0,0],
    [0,0,1,0,1],
    [1,0,0,1,1],
    ]

o=island(a)
o.driver_prog()