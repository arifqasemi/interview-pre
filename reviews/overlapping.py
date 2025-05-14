def countWays(ranges):
    ranges.sort()
    count = 0
    stack = []
    for start,end in ranges:
        last_end = stack.pop() if stack else None
        if last_end:
            if last_end  > start:
                count +=1
        stack.append(end)
    return 2 ** count

print(countWays([[1,3],[10,20],[2,5],[4,8]]))