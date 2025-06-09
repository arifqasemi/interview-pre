## Example 1:
## 
## Input: nums = [1,2,3,4]
## Output: [24,12,8,6]
## Example 2:
## 
## Input: nums = [-1,1,0,-3,3]
## Output: [0,0,9,0,0]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Prefix product
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

        