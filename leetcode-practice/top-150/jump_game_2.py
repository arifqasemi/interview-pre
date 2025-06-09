def jump(nums):
    n = len(nums)
    if n <= 1:
        return 0
    
    jumps = 0
    current = 0
    furthest = 0
    
    for i in range(n - 1):
        furthest = max(furthest, i + nums[i])
        if i == current:
            jumps += 1
            current = furthest
            if current >= n - 1:
                break
    
    return jumps