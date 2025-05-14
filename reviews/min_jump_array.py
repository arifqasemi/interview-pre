def minJumpTo(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    jumps = arr[0]
    count_jump = 1
    for i in range(1,len(arr)):
        if jumps + arr[i] == n or jumps + arr[i] > n:
            count_jump +=1
            return count_jump
        else:
            count_jump +=1
            jumps +=arr[i]
    return -1
    


print(minJumpTo([2, 3, 1, 1, 4]))  # Output: 2
# [3, 4, 2, 1, 1, 100]
# [1, 3, 6, 8, 2, 7, 1, 2, 1, 2, 6, 1, 2, 1, 2]