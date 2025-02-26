class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""

        gcd_len = self.gcd(len(str1), len(str2))
        return str1[:gcd_len]

    def gcd(self, p, q):
        if p == 0 or q == 0:
            return max(p, q)
        if p > q:
            return self.gcd(p - q, q)
        else:
            return self.gcd(p, q - p)
