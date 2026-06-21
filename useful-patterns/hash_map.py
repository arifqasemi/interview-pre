from collections import defaultdict
d = defaultdict(int)    # Auto-create missing keys as 0
d['count'] += 1        # Works even if key doesn't exist

from collections import Counter
counts = Counter(['a', 'b', 'a', 'c', 'a'])
# Counter({'a': 3, 'b': 1, 'c': 1})
counts.most_common(2)  # [('a', 3), ('b', 1)]


import heapq

counts = Counter(apple=10, banana=2, orange=5, grape=1, pear=4)

# Find the 2 elements with the lowest counts
two_smallest = heapq.nsmallest(2, counts.items(), key=lambda x: x[1])

print(two_smallest)
# Output: [('grape', 1), ('banana', 2)]



counts = Counter(apple=10, banana=2, orange=5, grape=1, pear=4)

# Sort items by frequency (index 1 of the tuple) and take the first two
two_smallest = sorted(counts.items(), key=lambda x: x[1])[:2]

print(two_smallest)
# Output: [('grape', 1), ('banana', 2)]
