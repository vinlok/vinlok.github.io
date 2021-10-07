'''
Binary search uses divide and conquer

Algo:

- Array needs to be sorted.

    - low=0
    - high=len(array)-1
- while True:

    - Find the mid of the (high-low)//2
    - if the ele==array(mid)
        return(True, index)
      elif element at the mid is greater than ele, then the element will be on the left side.
        - set the high = mid-1
      else ( mid is smaller the ele, ele is on the right side)
        - set the low to mid +1


'''


a=[10,15,20,25,30,40,50]
a=[1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]


def binary_search(a,ele):
    low=0
    high=len(a)-1

    while True:
        mid=low + (high-low)//2
        if low > high:
            break

        if ele==a[mid]:
            return(True,mid)

        if ele < a[mid]:
            high= mid -1
        else:
            low=mid + 1

    return(False)
print(binary_search(a,5))