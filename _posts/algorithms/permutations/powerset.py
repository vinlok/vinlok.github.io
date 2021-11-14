

def powerset(s,i,cur):

    if i == len(s):
        print(cur)
        return


    powerset(s,i+1,cur+s[i])
    powerset(s,i+1,cur)



def powerset_using_stack(a):

    '''
    number of element in powerset = 2^n
    algo:
    1. start with empty subset array.
    2. Now for each element in the array, add it to each element of subset. This will need two for loops

        for element in array:

            for subset in subsets:
                subset = subset+[element}
                add it to subsets


    Explanation: [1,2,3]

    element=1
    subset=[]
    subsets=[[],[1]]

    element=2
    subsets=[],[1],[2],[1,2]

    element=3

    subsets=all + 3,

    :param a:
    :return:
    '''



    subsets=[[]]

    for element in a:

        #for subset in subsets: #You cannot do this because each append to subset
                                #will increase the length of subsets
                                #and you will go in infinite loop
         for i in range(len(subsets)): #Here range is lazy operator and the len of subsets
                                        #during the first time is calculated.
            subset = subsets[i]+[element]
            subsets.append(subset)

    print(subsets)


def check_iteration():

    a=[1,2,3]
    i=4
    for e in range(len(a)):
        print(e)
        a.append(i)
        i+=1

s="abc"

a=[1,2,3]
#powerset(s,0,"")

powerset_using_stack(a)

# check_iteration()
