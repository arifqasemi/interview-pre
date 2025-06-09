## Input: height = [1,8,6,2,5,4,8,3,7]
## Output: 49
## Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
## Example 2:
## 
## Input: height = [1,1]
## Output: 1


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current area
            h = min(height[left], height[right])
            width = right - left
            area = h * width

            # Update max area if needed
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
