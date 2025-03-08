class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        num_dict = {}
        for num in nums:
            if not num_dict.get(num, 0):
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        for num in nums:
            if num_dict.get(k - num, 0):
                amount = min(num_dict[num], num_dict[k - num]) if num != k - \
                    num else min(num_dict[num], num_dict[k - num]) // 2
                count += amount
                num_dict[k - num] -= amount
                num_dict[num] -= amount
        return count


print(Solution().maxOperations([3, 1, 3, 4, 3], 6))
