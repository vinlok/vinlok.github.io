def dup_array(a):

    l=len(a)

    for i in range(l):
        a.append(a[i])

    print(a)


a=[1,2,3]
dup_array(a)
