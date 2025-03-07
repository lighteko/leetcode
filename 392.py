class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sec = list(s)
        for char in t:
            if not sec: return True
            if char == sec[0]:
                sec.pop(0)
        return not sec
