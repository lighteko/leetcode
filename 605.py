class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(0, len(flowerbed)):
            left = flowerbed[i - 1] if i > 0 else 0
            right = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
            if flowerbed[i] == 0 and left == 0 and right == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
