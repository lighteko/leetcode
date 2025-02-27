class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u"]
        existing_vowels = []
        string = list(s)

        for i in range(len(string)):
            if string[i].lower() in vowels:
                existing_vowels.append(string[i])
                string[i] = 0
        for i in range(len(string)):
            if string[i] == 0:
                string[i] = existing_vowels.pop()

        return "".join(string)
