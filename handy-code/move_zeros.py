class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        insert_pos = 0
            
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[insert_pos] =nums[i]
                insert_pos +=1
        
            
        while insert_pos <= len(nums):
            nums.append(0)
            


        