
def check_palindrome(string,s,e):

    print(string[s:e+1])
    # You will forget this
    start=s
    end=e
    while s < e:

        if string[s] != string[e]:
            return (False,None)
        s +=1
        e -=1

    return (True,string[start:end+1])



def find_all_palindromes(string):
    '''

    algo: (from educative.io)

    1. create a function which checks if a given string is palindrome or not.
        this will return (True,slice) if palindrom
            else
                return(False,None)
    2. Iterate on the string
        start=0
        end=1
        len=len_of_sting
        while start < len

            iterate again from start till len:
                send the slice of string (start, end) shifting end till len as input to check_palindrome
                if result true, add it to set

    '''


    s=0
    e=1
    l=len(string)

    palindromes=set()
    while s < l:
        palindromes.add(string[s])
        while e<l:
            (res,p)=check_palindrome(string,s,e)
            print(p)
            if res is True:
                palindromes.add(p)

            e += 1

        s +=1
        e =s+1


    return palindromes


def palindrome_with_one_skip(string):

    '''

    if the chars are not matching
    then if you have already skipped return

    l +=1
    if char not matching
        l -
        r -
        if char still not matching
            return false
        else
            skip +
    else
        skip +

    :param string:
    :return:
    '''

    r=len(string)-1
    l=0
    skip=0
    while l<r:

        if string[l]!=string[r]:
            if skip > 0:
                return False

            l += 1

            if string[l]!=string[r]:
                l-=1
                r-=1
                if string[l] != string[r]:
                    return False
                else:
                    skip +=1

            else:
                skip +=1

        l+=1
        r-=1

    return True




string="aabbbaa"
p=find_all_palindromes(string)

print(p)

print(palindrome_with_one_skip("racecar"))