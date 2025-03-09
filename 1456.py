class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_count = 0
        vowel_count = 0
        string = list(s)
        for i in range(len(string) - k + 1):
            if i == 0:
                vowel_count = self.count_vowels(string[0: k])
            else:
                vowel_count -= 1 if self.is_vowel(string[i - 1]) else 0
                vowel_count += 1 if self.is_vowel(string[i + k - 1]) else 0
            max_count = max(vowel_count, max_count)
        return max_count
    
    def is_vowel(self, char):
        return char in ["a", "e", "i", "o", "u"]
    
    def count_vowels(self, string):
        count = 0
        for char in string:
            if char in ["a", "e", "i", "o", 'u']:
                count += 1
        return count
