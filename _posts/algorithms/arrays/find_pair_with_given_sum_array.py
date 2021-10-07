

def find_pair(a,target):
    '''
    algo:
    use hash

    iterate over array:
        if target-current_element in hash
            then we found pair

        add
    :param a:
    :param target:
    :return:
    '''
    t={}
    pair=[]
    for i in range(0,len(a)):
        print(t)
        if target-a[i] in t:
           pair.append([target-a[i],a[i]])

        t[a[i]]=True

    print(pair)





v = [5, 7, 1, 2, 8, 4, 3]

find_pair(v,10)