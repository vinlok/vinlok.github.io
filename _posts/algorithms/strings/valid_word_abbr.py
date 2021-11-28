def validWordAbbreviation(word, abbr):
    """
    :type word: str
    :type abbr: str
    :rtype: bool

    algo:
    1. set position=0. Iterate on the abbr
    2. if the element of abbr is char
        then
            value at same position in word should match
            position+=1
        elseif number
            position+=num



            "appleen"
            "a2l2n"
    """


    location = 0
    i= 0
    while i < len(abbr):

        if abbr[i].isalpha():  # try converting to int
            print(abbr[i],location,word[location])
            if abbr[i] != word[location]:
                return False
            i += 1
            location +=1
        else:
            temp = ""
            j = i
            while i < len(abbr):
                print(abbr[i])
                if abbr[i].isdigit():
                    temp = temp+abbr[j]
                    i += 1
                else:
                    print(temp)
                    location+=int(temp)
                    print(location)
                    break


    return True


print(validWordAbbreviation("appleen","a2l2n"))

