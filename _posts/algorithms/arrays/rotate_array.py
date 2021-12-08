def rotate_array(a,n):
    '''
    Algo:
    - calculate the number of rotations to be done in case n is greater than length:
        n = n%l
            note: 5%6 is 5 , 5/6 is .833 and 5//6 is 0
        if n is negative then number of rotation in right becomes n = n + l
    '''
    l=len(a)
    t=a[l-n:]

    print(l,n)
    print(t)
    for i in range(l-1,n-1,-1):
        print(a[i])
        a[i]=a[i-n]

    for i in range(0,n):
        a[i]=t[i]
    print(a)

arr = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
print("Array Before Rotation")
print(arr)

rotate_array(arr, 2)
# print("Array After Rotation")
# print(arr)