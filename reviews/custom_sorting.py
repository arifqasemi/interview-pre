from collections import Counter

def customSortString(order, s):
    count = Counter(s)  # {'a': 1, 'b': 1, 'c': 1, 'd': 1}
    result = []

    # Add characters in the order defined by `order`
    for char in order:
        if char in count:
            result.append(char * count[char])
            del count[char]

    # Add remaining characters (not in order)
    for char, freq in count.items():
        result.append(char * freq)

    return ''.join(result)

# Example
print(customSortString("cba", "abcd"))  # Output: "cbad"
