class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        prefix = []
        suffix = []
        temp = 1
        for num in nums:
            temp *= num
            prefix.append(temp)
        temp = 1
        for i in range(len(nums)):
            temp *= nums[len(nums) - i - 1]
            suffix.insert(0, temp)
        for i in range(len(nums)):
            product = 1
            if i > 0:
                product *= prefix[i - 1]
            if i < len(nums) - 1:
                product *= suffix[i + 1]
            ans.append(product)
        return ans
