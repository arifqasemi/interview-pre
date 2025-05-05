def minJumpTo(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    jumps = 1
    max_reach = arr[0]
    step = arr[0]

    for i in range(1, n):
        if i == n - 1:
            return jumps

        max_reach = max(max_reach, i + arr[i])
        step -= 1

        if step == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            step = max_reach - i

    return -1

print(minJumpTo([2, 3, 1, 1, 4]))  # Output: 2
# [3, 4, 2, 1, 1, 100]
# [1, 3, 6, 8, 2, 7, 1, 2, 1, 2, 6, 1, 2, 1, 2]