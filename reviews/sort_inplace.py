######### Input: nums = [2,0,2,1,1,0]
######### Output: [0,0,1,1,2,2]
def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    for i in range(1,len(nums)):
        current = nums[i]
        left = i -1
        while left >= 0 and nums[left] > current:
            nums[left + 1] = nums[left]
            left -= 1            
        nums[left +1] = current



        