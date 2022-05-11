
def encode_string(s):
    '''
     Algo:
     1. Iterate over the string and keep counting the element until there is change.
     2. when element changes, add the countand the letter to res
    '''

    c=1
    res=[]
    f=0
    r=1

    while True:
        if r == len(s):
            print("here")
            res.append(c)
            res.append(s[f])
            break
        if s[f] != s[r]:
            res.append(c)
            res.append(s[f])
            c=0
        c += 1
        f += 1
        r += 1

    print(res,r)
encode_string("aaaaaaa")