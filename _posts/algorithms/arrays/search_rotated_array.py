


def search_rotated_array(a,ele):
    '''

    Algo:
    - Use binary search
    - set low = 0
    - high = len(a)
    while true:

    - mid = (high-low)//2
    - if ele == mid(a)
        found the ele
        return

    if a[low] < a[mid] and ele < a[mid]:
        high=mid-1
    elif a[mid] < a[high] and ele > a[mid]:
        low= mid+1
    elif a[low] < a[mid]:
        high = mid -1
    elif a[mid] < a[start]:
        low = mid + 1


    - if ele > a[mid] then element should be on the left side of array
        then
            low = mid + 1
        else: element is on the right of the array
            high = mid-1


    :param a:
    :param ele:
    :return:
    '''

    low = 0
    high = len(a)-1

    while True:
        # print(low,mid,high)
        mid=(high-low)//2
        print(low, mid, high)
        if ele == a[mid]:
            return(mid, True)

        if a[low] < a[mid] and ele < a[mid]:
            high = mid - 1
        elif a[mid] < a[high] and ele > a[mid]:
            low = mid + 1
        elif a[low] > a[mid]:
            high = mid - 1
        elif a[high] < a[mid]:
            low = mid + 1

        if low > high:
            break

    return False


v1 = [6, 7, 1, 2, 3, 4, 5]
print(search_rotated_array(v1,1))