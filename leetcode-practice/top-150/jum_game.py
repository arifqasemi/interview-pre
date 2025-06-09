##  Example 1:
##  
##  Input: nums = [2,3,1,1,4]
##  Output: true
##  Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
##  Example 2:
##  
##  Input: nums = [3,2,1,0,4]
##  Output: false
##  Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                print(i,max_reach)
                return False
            max_reach = max(max_reach, i + nums[i])

        return True