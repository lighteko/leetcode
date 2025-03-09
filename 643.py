class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        avg = float("-inf")
        sum_nums = 0
        for i in range(len(nums) - k + 1):
            if i == 0:
                sum_nums = sum(nums[0: k])
            else:
                sum_nums -= nums[i - 1]
                sum_nums += nums[i + k - 1]
            avg = max(float(sum_nums) / k, avg)
        return avg
