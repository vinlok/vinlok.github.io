class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])
        stack = []
        stack.append(intervals[0])
        i = 1
        while i < len(intervals):
            [s1, e1] = stack.pop()
            [s2, e2] = intervals[i]
            if s2 <= e1 and e2 >= e1:
                stack.append([s1, e2])
            elif s2 < e1 and e2 < e1:
                stack.append([s1, e1])
            elif s1 == s2 and e1 == e2:
                stack.append([s1, e1])
            else:
                stack.append([s1, e1])
                stack.append([s2, e2])

            i += 1

        return (stack)





intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals=[[1,4],[4,5]]
merge_intervals(intervals)
#Output should be: [[1,6],[8,10],[15,18]]