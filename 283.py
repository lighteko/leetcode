class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        moved = 0
        while i + moved < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                i -= 1
                moved += 1
            i += 1
