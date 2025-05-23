#Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:
# 
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert_pos = 0
        for i in range(m):
            nums1[insert_pos] =nums1[i]
            insert_pos +=1
        for i in range(n):
            nums1[insert_pos] =nums2[i]
            insert_pos+=1
        for i in range(1,m+n):
            current = nums1[i]
            left = i -1
            while left >= 0 and nums1[left] > current:
                nums1[left + 1] = nums1[left]
                left -= 1            
            nums1[left +1] = current
