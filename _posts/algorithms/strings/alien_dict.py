class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        position_dict = {}

        for i in range(0, len(order)):
            position_dict[order[i]] = i

        current_word = 0
        done = False
        while True:
            next_word = current_word + 1
            if next_word >= len(words):
                break

            # now compare current_word and next_word
            # if the words do not match, then return false
            for i in range(0, len(words[current_word])):
                if i < len(words[next_word]):

                    if position_dict[words[current_word][i]] > position_dict[words[next_word][i]]:
                        print(words[current_word][i])
                        return False
                else:
                    break
            current_word += 1

        return True