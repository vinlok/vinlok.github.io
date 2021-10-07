
def binary_search(a,k):
    '''
    algo:
    - divide and conquer, needs sorted array

    - set low and high for array
    - find the mid of the array (high-low)//2
    - if the ele at mid is less than the key then key is on left, move the low to mid+1
    - if the ele at mid is greater than key then key is right, move end to mid -1
    -
    :param a:
    :param k:
    :return:
    '''

    low=0
    high=len(a)-1

    while True:
        mid=low+(high-low)//2
        print(low,mid,high)
        if a[mid]==k:
            return(True,mid)
        if k > a[mid]:
            low=mid+1
        else:
            high=mid-1

        if low> high:
            break

    return(False,-1)

def find_low_high(array,key):
    '''
    algo:
    - Do a binary search and find the index of element
    - Once index if found:

        find the low by moving left until you see change in key val
        find the high by moving right until you see change in key val

    :param array:
    :param key:
    :return:
    '''

    result,index=binary_search(array,key)

    if result:

        low=high=index
        for i in range(index,0,-1):
            print(array[low])
            if array[low] != array[index]:
                break
            low = i

        for i in range(index,len(array)-1):

            if array[high] != array[index]:
                break
            high = i

    print(high-1)

array = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
key = 5
low = find_low_high(array, key)