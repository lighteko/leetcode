class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        left = list(word1)
        right = list(word2)

        string = []
        for i in range(len(left)+len(right)):
            if len(left) != 0 and i % 2 == 0 or len(right) == 0:
                string.append(left.pop(0))
            elif len(right) != 0 and i % 2 == 1 or len(left) == 0:
                string.append(right.pop(0))
        
        return "".join(string)