def food_distribution(hunger):
    n = len(hunger) // 2
    m = len(set(hunger))
    return min(n,m)

print(food_distribution([2, 2, 2, 1, 0]))