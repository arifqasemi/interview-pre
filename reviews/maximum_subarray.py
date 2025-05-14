def MaximumSubarray(arr):
    result = arr[0]
    for i in range(len(arr)):
        sum_num = 0
        for j in range(i,len(arr)):
            sum_num +=  arr[j]
            result = max(result,sum_num)
    print(result)
            
        
        
nums = [-2,1,-3,4,-1,2,1,-5,4]
MaximumSubarray(nums)