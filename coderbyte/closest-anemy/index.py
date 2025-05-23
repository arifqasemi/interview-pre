def ClosestEnemyII(strArr):
    # Step 1: Parse the grid
    M = len(strArr)  # Number of rows
    N = len(strArr[0])  # Number of columns
    space = 0
    for i in range(len(strArr)):
        for k in range(1,len(strArr)):
            if '1' in strArr[i]  and '2' in strArr[k]:
                print(strArr[i],strArr[k])
                return abs(i -k)
            
    # player = None
    # enemies = []

    # # Find player and enemy positions
    # for y in range(M):
    #     for x in range(N):
    #         if strArr[y][x] == '1':
    #             player = (x, y)  # (x, y) coordinates
    #         elif strArr[y][x] == '2':
    #             enemies.append((x, y))

    # # Step 2: Calculate minimum Manhattan distance with wrap-around
    # min_distance = float('inf')
    # px, py = player

    # for ex, ey in enemies:
    #     # X-distance: min(|px - ex|, N - |px - ex|)
    #     dx = min(abs(px - ex), N - abs(px - ex))
    #     # Y-distance: min(|py - ey|, M - |py - ey|)
    #     dy = min(abs(py - ey), M - abs(py - ey))
    #     # Total Manhattan distance
    #     distance = dx + dy
    #     min_distance = min(min_distance, distance)

    # # Step 3: Return the result
    # return min_distance

# Test cases
# print(ClosestEnemyII(["0000", "1000", "0002", "0002"]))  # Output: 1
# print(ClosestEnemyII(["000", "100", "200"]))  # Output: 1
print(ClosestEnemyII(["0000", "2010", "0000", "2002"]))  # Output: 2