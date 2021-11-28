
def minRemoveToMakeValid(s):

    '''

    Algo:

    1. We keep track of current number of "(".
    2. If the char is not either of () we add to array.
    3. If ( we incr current and add.
    4. If ) then we add only if current >0.

    This will be the first pass. Now there might be remaining ( at the end.

    So, we reverse and remove them by decrementing current.

    and then again reverse

    Things to remember:

    a=[1,1,1]
    a.remove(1) will remove only the first occurence of 1.
    '''


    # Pass 1
    result=[]

    current=0
    for c in s:
        print(c)
        if c not in["(",")"]:
            result.append(c)

        if c == "(":
            current += 1
            result.append(c)

        if c == ")" and current >0:
            result.append(c)
            current -=1

    print(result)
    print(current)
    # Now reverse
    result.reverse()

    while current >0:
        result.remove("(")
        current -= 1


    result.reverse()

    return("".join(result))
s = "lee(t(c)o)de)("

minRemoveToMakeValid(s)

