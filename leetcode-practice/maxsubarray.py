class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_sum = nums[0]  # Start with first element (handles all-negative arrays)
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):  # j starts at i to include full subarrays
                current_sum += nums[j]
                largest_sum = max(largest_sum, current_sum)
        return largest_sum