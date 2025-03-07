class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) < 2:
            return len(chars)
        
        target = (1, chars[0])
        i = 1
        while i < len(chars):
            if chars[i] == target[1]:
                if i == target[0]:
                    chars[i] = str(2)
                else:
                    count = int(chars[target[0]]) + 1
                    chars[target[0]] = str(count)
                    chars.pop(i)
                    i -= 1
            else: target = (i + 1, chars[i])
            i += 1
        i = 1
        while i < len(chars):
            if len(chars[i]) > 1:
                num = chars[i]
                chars.pop(i)
                x = i
                for n in num:
                    chars.insert(x, n)
                    x += 1
            i += 1
        return len(chars)
    
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))