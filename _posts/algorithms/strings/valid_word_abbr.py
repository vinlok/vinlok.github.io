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
    """

    location = 0

    for i in range(len(abbr)):

        if abbr[i].isalpha():  # try converting to int
            if abbr[i] != word[location]:
                return False
            location += 1
        else:
            temp = 0
            while temp < len(abbr):
                if abbr[i].isdigit():
                    temp = 10 * temp + int(abbr[i])
                    i += 1
                else:
                    location += temp
                    break

    return True

