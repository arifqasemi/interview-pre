def countWays(ranges):
    ranges.sort()
    count = 0
    max_end = -1

    for start, end in ranges:
        if start > max_end:
            count += 1
        max_end = max(max_end, end)  # instead of if check the prev record we use max

    return 2**count


print(countWays([[1,3],[2,5],[6,8],[9,10]]))