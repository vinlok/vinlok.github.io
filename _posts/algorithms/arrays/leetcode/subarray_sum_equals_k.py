def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    # sum=0
    # p=0
    # res=0
    #
    # while p < len(nums):
    #
    #     sum = sum + nums[p]
    #
    #     if sum > k:
    #         sum = nums[p]
    #
    #     if sum == k:
    #         res +=1
    #         sum=nums[p]
    #
    #     p += 1
    #
    # print(res)
    from collections import defaultdict
    m = defaultdict(int)
    sum = 0
    count = 0
    for i in nums:
        sum += i
        if sum == k:
            count += 1

        if sum - k in m:
            count += m[sum - k]
        m[sum] += 1
    return count


subarraySum([1,2,3,1,2],3)