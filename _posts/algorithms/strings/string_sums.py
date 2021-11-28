from collections import deque

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str


        Things to remember:
        1. Do not use != operator rather use the >= 0. Think!

        Algo:

        1. Use two pointers p1 and p2 pointing to end
        2.


        """

        p1=len(num1) - 1
        p2=len(num2) - 1

        c=0
        output=""
        out=deque()
        while p1 >= 0 or p2 >= 0:
            if p1 >= 0:
                diff1=ord(num1[p1])-ord('0')
            else:
                diff1=0

            if p2 >= 0:
                diff2 = ord(num2[p2]) - ord('0')
            else:
                diff2 = 0

            temp=diff1+diff2+c
            if temp > 9:
                res=temp%10
                c=temp//10
            else:
                res=temp
                c=0

            output=str(res)+output
            out.appendleft(res)
            p1 -= 1
            p2 -= 1

        if c > 0:
            output=str(c)+output
            out.appendleft(c)
        print(output)
        print(list(out))


    def addArrays(self,a,b):

        '''
        algo:

        1. create a answer deque() for this you need to import deque from collections.
        2. Use two pointers and start from the end of arrays.
        3. The carry should be set to 0.
        4. while p1 or p2 are >= 0:
            get the diff from ord(0) for p1 if p1 is greter
        :param a:
        :param b:
        :return:
        '''

s = Solution()

s.addStrings("81","19")