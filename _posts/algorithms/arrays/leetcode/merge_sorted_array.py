#https://leetcode.com/problems/merge-sorted-array/

Note: this is also used for median of two arrays in log(m+n)

def merge_sorted_arrays(nums1,m,nums2,n):
    '''Algo:
    - use three pointers
        - p to the end of a1
        - p1 to val before zero
        - p2 to end of a2

    - iterate using for in reverse
        if p1 val > p2
            then p val == p1 val
                p--
                p1--
        else
            then p val == p2 val
                p--
                p2--





    '''


    p = len(nums1)-1
    p1= m-1
    p2= n-1

    for p in range(len(nums1)-1,-1,-1):

        if p2<0:
            break


        if p1 >=0 and nums1[p1]>nums2[p2]:
            nums1[p] = nums1[p1]
            # p -=1
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            # p -= 1
            p2 -= 1


    # # Set p1 and p2 to point to the end of their respective arrays.
    # p1 = m - 1
    # p2 = n - 1
    #
    # # And move p backwards through the array, each time writing
    # # the smallest value pointed at by p1 or p2.
    # for p in range(n + m - 1, -1, -1):
    #     if p2 < 0:
    #         break
    #     if p1 >= 0 and nums1[p1] > nums2[p2]:
    #         nums1[p] = nums1[p1]
    #         p1 -= 1
    #     else:
    #         nums1[p] = nums2[p2]
    #         p2 -= 1


        print(nums1)

nums1 = [4,5,6, 0, 0, 0]
nums2 = [1, 2, 3]

merge_sorted_arrays(nums1,3,nums2,3)
