class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        s = s.strip()
        s = re.sub(r'\s+', " ", s)
        ans = s.split(" ")
        ans.reverse()
        return " ".join(ans)
