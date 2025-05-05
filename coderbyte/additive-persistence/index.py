def additive_persistence(num):
    count = 0
    while num >= 10:
        print(num)
        num = sum(int(digit) for digit in str(num))
        count += 1
    return count

# Example usage
print(additive_persistence(2718))  # Output: 2
# print(additive_persistence(4))     # Output: 0
