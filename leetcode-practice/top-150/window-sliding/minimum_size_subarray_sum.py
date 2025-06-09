## Example 1:
## 
## Input: target = 7, nums = [2,3,1,2,4,3]
## Output: 2
## Explanation: The subarray [4,3] has the minimal length under the problem constraint.
## Example 2:
## 
## Input: target = 4, nums = [1,4,4]
## Output: 1
## Example 3:
## 
## Input: target = 11, nums = [1,1,1,1,1,1,1,1]
## Output: 0



from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            print(right)
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len


print(Solution().minSubArrayLen(7,[2,3,1,2,4,3]))