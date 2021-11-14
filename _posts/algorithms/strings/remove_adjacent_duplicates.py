
def remove_duplicates(s):
    '''

    algo:
    1. Use Stack
    2. Iterate over the string, if the char matches the topof stack the pop it
    '''



    stack=[]
    for i in range(0,len(s)):

        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    print("".join(stack))


remove_duplicates("abbaca")