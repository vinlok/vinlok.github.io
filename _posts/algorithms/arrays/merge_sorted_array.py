from collections import defaultdict




a=[[1,3],[2,5],[4,6]]


class MergeArrays():


    def __init__(self,a):
        self.l=len(a)
        self.a=a

    def doIt(self):        
        tracker=defaultdict(list)
        # e,p,l

        done=False
        merged=[]
        while not done:
            t=[]
            for i,currArray in enumerate(self.a):
                if tracker[i][1] < len(currArray):
                    t.append(currArray[tracker[i]],i)
            t.sort(key=lambda x:x[0])
            print(t)
            break
            merged.append(min(t))

o=MergeArrays(a)
o.doIt()