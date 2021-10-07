

def move_zeros_to_left(a):

    '''
    Algo:
    create two pointers pointing to the end of the array

    while you have not reached to the start of the array
        move p1 by 1 to right
        if the value at p2 is zero and p1 non-zero:
            copy p1 val to p2
            move p2 to right
            set p2 val to 0


    :param a:
    :return:
    '''

    l=len(a)
    p1=p2=l-1
    while p1 > 0:
        p1= p1 -1

        if a[p2] == 0 and a[p1] != 0:
            a[p2] =a[p1]

            p2 = p2 -1
            a[p2] = 0

    print(p2)
    for i in range(0,p2):
        a[i]=0

    print(a)

v = [1, 10, 20, 0, 59, 63, 0, 88, 0]
print("Original Array:", v)

move_zeros_to_left(v)
# print("After Moving Zeroes to Left: ", v)