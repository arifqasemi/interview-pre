def food_distribution(hunger):
    n = len(hunger)
    food = [1] * n

    # Left to right pass
    for i in range(1, n):
        if hunger[i] > hunger[i - 1]:
            food[i] = food[i - 1] + 1

    # Right to left pass
    for i in range(n - 2, -1, -1):
        if hunger[i] > hunger[i + 1] and food[i] <= food[i + 1]:
            food[i] = food[i + 1] + 1

    return sum(food)
