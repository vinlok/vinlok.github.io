class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Algo:
        1. Reverse sort
        2. Then the element at the given position is the one.

        If we need to remove duplicate, then use heapq.

        heapq.heapify(nums)

        This will remove the duplicates and also sort


        """

        nums.sort(reverse=True)
        i = 1
        for n in nums:
            if i == k:
                return n

            i += 1