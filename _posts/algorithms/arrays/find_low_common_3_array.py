
def find_least_common_number(a1,a2,a3):
    '''
    Algo:
    Use three pointers i,j,k for a1, a2 and a3

    while true
        iterate over each array
        if value matches for all three at 1,j,k pointers then return that
        else
            find the smallest amongst the three and increments its pointer

        if any of the array has been exhausted then break

    :param a1:
    :param a2:
    :param a3:
    :return:
    '''


    i=j=k=0

    while True:
        t={}
        if a1[i] == a2[j] and a2[j] == a3[k]:
            return a1[i]

        if a2[j] <= a1[i] and a2[j] <= a3[k]:
            j+=1

        elif a3[k] <= a1[i] and a3[k] <= a2[j]:
            k+=1

        else:
            i+=1

        if i >= len(a1) or j >= len(a2) or k >= len(a3):
            break

    return False








v1 = [6, 7, 10, 25, 30, 63, 64]
v2 = [0, 4, 5, 6, 7, 8, 50]
v3 = [1, 6, 10, 14]

result = find_least_common_number(v1, v2, v3)
print("Least Common Number: " + str(result))