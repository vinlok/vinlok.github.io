

def remove_duplicates1(s):

    """
    Algo:
    1. Trick here is to do this inplace.
    2. Set r and w pointer to 0
    3. Create a empty hashset
    4. Iterate while r is less than len of s

        if s[r] not in hashset
            add it
            and set w as r
            incr both r and w
        else:
            only incr r

    s =dabbac

    TC: o(n)
    MC: o(1)

    """

    hashset=set()
    r=w=0
    s=list(s)
    # print(s)
    while r < len(s):
        # print(s[w])
        if s[r] not in hashset:
            hashset.add(s[r])
            s[w]=s[r]
            w+=1

        r+=1

    s[w]="\0"

    return s


def remove_duplicates2(s):

    '''
    Algo:
    1. Use set. Set do not store duplicates. Hence, when you convert string to set, duplicates will be removed.
    2. Order of elemets will not be maintained.

    :param s:
    :return:
    '''

    hashset=set()

    for i in range(0,len(s)):
        hashset.add(s[i])



    res="".join(hashset)
    print(res)





s = "dabbac"

res=remove_duplicates1(s)
str=""
for c in res:
    if c=="\0":
        break

    str=str+c

print(str)
remove_duplicates2(s)