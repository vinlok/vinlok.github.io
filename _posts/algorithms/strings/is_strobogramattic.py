class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        
        l=0
        r=len(num)-1
        
        maps={1:1,6:9,8:8,9:6,0:0}
        map1=(1,8,0)
        
        if len(num)==1:
            if int(num[0]) not in map1:
                return False
            
        if len(num)%2==1:
            if int(num[len(num)//2]) not in map1:
                return False
        
        while l < r:
            print(l,r)    
            res=maps.get(int(num[l]))
            print(num[l])
            print(res)
            if res is None:
                print("her")
                return False
            
            if res != int(num[r]):
                print("hhh")
                return False
            l+=1
            r-=1
        
        return True