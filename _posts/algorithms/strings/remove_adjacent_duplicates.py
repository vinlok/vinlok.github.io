
def remove_duplicates(s):
    '''

    algo:
    1. Use Stack
    2. Iterate over the string, if the char matches the topof stack the pop it

    Things to remember: a[-1] will error if a is empty.
    '''

    stack = []

    for i in range(0, len(s)):

        if len(stack) > 0 and s[i] == stack[-1]:
            stack.pop()

        else:
            stack.append(s[i])

    print(stack)
    return "".join(stack)


remove_duplicates("abbaca")

