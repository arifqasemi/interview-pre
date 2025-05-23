def countWays(ranges):
    ranges.sort()
    count = 0
    max_end = -1

    for start, end in ranges:
        if start > max_end:
            count += 1
        max_end = max(max_end, end)

    return 2**count


print(countWays([[1,3],[10,20],[2,5],[4,8]]))