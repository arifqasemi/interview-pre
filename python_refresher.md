# Python Refresher for Backend Engineer Interview
## Quick Reference Guide for Production Python

---

## 🎯 YOUR SITUATION

You're a **backend engineer with 3+ years experience**. You don't need to learn Python basics. You need to:

✅ Refresh syntax you haven't used in a while  
✅ Remember quick idioms for interview speed  
✅ Know Python's built-in data structures cold  
✅ Write clean, efficient code fast  

**This is NOT a beginner guide. This is a cheat sheet for experienced developers.**

---

## ⚡ SECTION 1: MUST-KNOW DATA STRUCTURES

### **Lists (Arrays)**

```python
# Create
arr = [1, 2, 3]
arr = list(range(5))  # [0, 1, 2, 3, 4]

# Access
arr[0]      # First element
arr[-1]     # Last element
arr[1:3]    # Slice [1, 2] (not including 3)
arr[::-1]   # Reverse [3, 2, 1]

# Add/Remove
arr.append(4)           # Add to end: O(1)
arr.pop()              # Remove last: O(1)
arr.insert(0, 0)       # Insert at index: O(n)
arr.remove(2)          # Remove value: O(n)

# Useful operations
len(arr)               # Length
arr.sort()             # Sort in-place: O(n log n)
sorted(arr)            # Return sorted copy
arr.reverse()          # Reverse in-place

# Slicing tricks
arr[::2]               # Every 2nd element
arr[1::2]              # Every 2nd element starting at 1
arr[:3]                # First 3 elements
arr[-3:]               # Last 3 elements

# List comprehension (fast, readable)
[x*2 for x in arr]     # Double each element
[x for x in arr if x > 2]  # Filter
```

### **Dictionaries (Hash Maps)**

```python
# Create
d = {'a': 1, 'b': 2}
d = dict()  # Empty dict

# Access
d['a']              # Get value: O(1)
d.get('a', 0)       # Get with default: O(1)
'a' in d            # Check key exists: O(1)

# Modify
d['c'] = 3          # Add/update: O(1)
d.pop('a')          # Remove: O(1)
d.pop('a', None)    # Remove with default

# Iterate
for key in d:                   # Iterate keys
for key, val in d.items():      # Iterate key-value
for val in d.values():          # Iterate values

# Dict operations
d.keys()            # Get all keys
d.values()          # Get all values
d.items()           # Get all key-value pairs

# Dict comprehension
{x: x*2 for x in range(3)}  # {0: 0, 1: 2, 2: 4}

# Useful patterns
from collections import defaultdict
d = defaultdict(int)    # Auto-create missing keys as 0
d['count'] += 1        # Works even if key doesn't exist

from collections import Counter
counts = Counter(['a', 'b', 'a', 'c', 'a'])
# Counter({'a': 3, 'b': 1, 'c': 1})
counts.most_common(2)  # [('a', 3), ('b', 1)]
```

### **Sets**

```python
# Create
s = {1, 2, 3}
s = set()  # Empty set

# Operations: O(1) for all
s.add(4)            # Add element
s.remove(1)         # Remove (error if not found)
s.discard(1)        # Remove (no error if not found)
1 in s              # Check membership: O(1)

# Set operations
s1 | s2             # Union
s1 & s2             # Intersection
s1 - s2             # Difference
s1 ^ s2             # Symmetric difference

# Useful for deduplication
duplicates = [1, 2, 2, 3, 3, 3]
unique = set(duplicates)  # {1, 2, 3}
```

### **Strings**

```python
# Basic operations
s = "hello world"

# Access
s[0]                # 'h'
s[-1]               # 'd'
s[0:5]              # 'hello'
s[::-1]             # Reverse 'dlrow olleh'

# Useful methods
s.split()           # Split by whitespace: ['hello', 'world']
s.split(',')        # Split by comma
''.join(['a', 'b']) # Join list: 'ab'
s.replace('l', 'x') # Replace: 'hexxo worxd'
s.strip()           # Remove whitespace
s.lower()           # Lowercase
s.upper()           # Uppercase
s.startswith('he')  # True
s.endswith('ld')    # True
s.find('o')         # Index of 'o': 4
s.count('l')        # Count occurrences: 3

# f-strings (modern Python)
name = "Arif"
age = 25
f"My name is {name} and I'm {age}"  # 'My name is Arif and I'm 25'

# String formatting
"{}".format("hello")        # 'hello'
"{:.2f}".format(3.14159)    # '3.14' (2 decimals)
```

### **Tuples**

```python
# Immutable, faster than lists
t = (1, 2, 3)
t = ()  # Empty tuple

# Access like lists
t[0]        # 1
t[1:2]      # (2,)

# Useful for dictionary keys (lists can't be keys)
d = {(1, 2): "pair"}  # Tuple as key

# Unpacking
x, y, z = (1, 2, 3)
a, *rest = [1, 2, 3, 4]  # a=1, rest=[2,3,4]

# Multiple return values (tuples)
def get_min_max(arr):
    return min(arr), max(arr)

min_val, max_val = get_min_max([1, 5, 3])
```

---

## 🔢 SECTION 2: COMMON ALGORITHMS IN PYTHON

### **Sorting**

```python
# Basic sort
arr = [3, 1, 4, 1, 5, 9]
sorted(arr)                      # [1, 1, 3, 4, 5, 9]
arr.sort()                       # Sort in-place
sorted(arr, reverse=True)        # Descending
sorted(arr, key=lambda x: -x)    # Descending (same)

# Sort by custom key
students = [('Alice', 25), ('Bob', 20), ('Charlie', 23)]
sorted(students, key=lambda x: x[1])  # Sort by age

# Sort dict by values
d = {'a': 3, 'b': 1, 'c': 2}
sorted(d.items(), key=lambda x: x[1])  # [('b', 1), ('c', 2), ('a', 3)]
```

### **Searching**

```python
# Linear search (O(n))
5 in [1, 2, 3, 4, 5]            # True
[1, 2, 3, 4, 5].index(3)        # 2 (index of element)

# Binary search (O(log n)) - for sorted arrays
import bisect
arr = [1, 3, 3, 3, 5, 7, 9]
bisect.bisect_left(arr, 3)   # Leftmost position of 3: 1
bisect.bisect_right(arr, 3)  # Rightmost position of 3: 4
bisect.insort(arr, 4)        # Insert in sorted position
```

### **Iteration & Enumeration**

```python
# Enumerate (get index and value)
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)
    # 0 a
    # 1 b
    # 2 c

# Zip (pair up lists)
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)
    # Alice 25
    # Bob 30

# Range
for i in range(5):           # 0, 1, 2, 3, 4
for i in range(1, 5):        # 1, 2, 3, 4
for i in range(0, 10, 2):    # 0, 2, 4, 6, 8
```

### **Map, Filter, Reduce**

```python
# Map (apply function to each element)
result = map(lambda x: x*2, [1, 2, 3])  # [2, 4, 6]
result = list(map(lambda x: x*2, [1, 2, 3]))  # Convert to list

# Filter (keep elements where condition is true)
result = filter(lambda x: x > 2, [1, 2, 3, 4])  # [3, 4]
result = list(filter(lambda x: x > 2, [1, 2, 3, 4]))

# Better: Use list comprehension (more Pythonic)
[x*2 for x in [1, 2, 3]]           # Map
[x for x in [1, 2, 3, 4] if x > 2] # Filter

# Reduce (fold/accumulate)
from functools import reduce
reduce(lambda a, b: a + b, [1, 2, 3, 4])  # 10 (sum)
```

---

## 🏗️ SECTION 3: IMPORTANT MODULES

### **Collections**

```python
from collections import Counter, defaultdict, deque

# Counter (frequency count)
c = Counter(['a', 'b', 'a', 'c', 'a', 'b', 'b'])
c['a']              # 3
c.most_common(2)    # [('a', 3), ('b', 3)]

# defaultdict (auto-create missing keys)
d = defaultdict(int)
d['count'] += 1     # Works even if 'count' doesn't exist

d = defaultdict(list)
d['items'].append(1)  # Works with lists too

# deque (efficient queue)
from collections import deque
q = deque()
q.append(1)         # Add to right
q.appendleft(0)     # Add to left
q.pop()             # Remove from right: O(1)
q.popleft()         # Remove from left: O(1)
```

### **Itertools**

```python
from itertools import combinations, permutations, product

# Combinations (order doesn't matter)
combinations([1, 2, 3], 2)  # (1,2), (1,3), (2,3)

# Permutations (order matters)
permutations([1, 2, 3], 2)  # (1,2), (1,3), (2,1), (2,3), (3,1), (3,2)

# Cartesian product
product([1, 2], ['a', 'b'])  # (1,'a'), (1,'b'), (2,'a'), (2,'b')
```

### **Heapq (Priority Queue)**

```python
import heapq

# Min heap
heap = [3, 1, 4, 1, 5, 9]
heapq.heapify(heap)         # Convert to heap: O(n)
heapq.heappush(heap, 2)     # Add element: O(log n)
heapq.heappop(heap)         # Remove smallest: O(log n)

# Get k largest elements
heap = [3, 1, 4, 1, 5, 9]
heapq.nlargest(3, heap)     # [9, 5, 4]
heapq.nsmallest(3, heap)    # [1, 1, 3]

# Max heap (negate values)
heap = []
heapq.heappush(heap, -5)
heapq.heappush(heap, -2)
-heapq.heappop(heap)        # 5 (largest)
```

---

## 🔄 SECTION 4: COMMON PATTERNS

### **Two Pointers**

```python
# Example: Two Sum (sorted array)
def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# O(n) time, O(1) space
```

### **Sliding Window**

```python
# Example: Longest substring without repeating characters
def longest_substring(s):
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

# O(n) time, O(min(n, charset)) space
```

### **Hash Map for Counting**

```python
# Example: Group anagrams
def group_anagrams(words):
    anagrams = {}
    for word in words:
        # Sort letters to get key
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())

# O(n * k log k) where k is max word length
```

### **Stack**

```python
# Example: Valid parentheses
def is_valid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0

# O(n) time, O(n) space
```

### **BFS (Breadth-First Search)**

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
# bfs(graph, 'A')  # A B C D
```

### **DFS (Depth-First Search)**

```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Same graph, same result
```

### **Dynamic Programming (Memoization)**

```python
# Example: Fibonacci with memoization
def fib(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

# O(n) time, O(n) space (instead of O(2^n) without memo)

# Decorator syntax (cleaner)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

---

## ⚡ SECTION 5: QUICK PYTHON IDIOMS

### **String/List Operations**

```python
# Check if palindrome
s = "racecar"
s == s[::-1]  # True

# Flatten list
nested = [[1, 2], [3, 4]]
flat = [item for sublist in nested for item in sublist]  # [1, 2, 3, 4]

# Remove duplicates (keep order)
def remove_duplicates(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Or: list(dict.fromkeys(arr))  # Python 3.7+ dicts maintain order

# Count occurrences
from collections import Counter
counts = Counter([1, 2, 2, 3, 3, 3])
counts[3]  # 3
```

### **Common Math Operations**

```python
# Absolute value
abs(-5)        # 5

# Max/Min
max([1, 5, 3])  # 5
min([1, 5, 3])  # 1
max(1, 5, 3)    # 5

# Power
2 ** 3         # 8
pow(2, 3)      # 8

# Floor division
7 // 2         # 3
-7 // 2        # -4 (floor toward negative infinity)

# Modulo
7 % 2          # 1
-7 % 2         # 1 (same sign as divisor)

# Sum
sum([1, 2, 3])  # 6
sum([1, 2, 3], 10)  # 16 (start with 10)
```

### **Type Checking**

```python
# Check type
isinstance(5, int)         # True
isinstance([1, 2], list)   # True
type(5) == int            # Also works but isinstance is preferred

# Convert types
int("5")        # 5
str(5)          # "5"
list((1, 2))    # [1, 2]
tuple([1, 2])   # (1, 2)
```

### **Error Handling**

```python
# Try-except
try:
    result = int("not a number")
except ValueError:
    result = 0

# Try-except-else
try:
    result = int("5")
except ValueError:
    result = 0
else:
    result *= 2  # Runs if no error

# Try-except-finally
try:
    result = 1 / 0
except ZeroDivisionError:
    result = 0
finally:
    print("Always runs")  # Cleanup code
```

---

## 🎯 SECTION 6: INTERVIEW SPEED TIPS

### **Write Pythonic Code Fast**

```python
# ❌ Slow and verbose
result = []
for i in range(len(arr)):
    if arr[i] > 5:
        result.append(arr[i] * 2)
return result

# ✅ Fast and Pythonic
return [x * 2 for x in arr if x > 5]

# ❌ Slow
count = 0
for item in items:
    if item == target:
        count += 1
return count

# ✅ Fast
return sum(1 for item in items if item == target)

# Or just use Counter
from collections import Counter
return Counter(items)[target]
```

### **Avoid Common Mistakes**

```python
# ❌ Mutable default argument
def add_item(item, items=[]):
    items.append(item)
    return items

# ✅ Use None
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# ❌ Forgetting O(n) operations
if element in large_list:  # O(n)
    pass

# ✅ Use set for O(1) lookup
if element in large_set:  # O(1)
    pass

# ❌ Modifying list while iterating
for item in arr:
    if bad_condition(item):
        arr.remove(item)  # ❌ Skips elements!

# ✅ Filter instead
arr = [item for item in arr if not bad_condition(item)]
```

---

## 📝 SECTION 7: ALGORITHM TEMPLATES

### **Two Pointers Template**

```python
def two_pointers(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current = arr[left] + arr[right]
        
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    
    return []
```

### **Sliding Window Template**

```python
def sliding_window(s, pattern):
    window_size = len(pattern)
    max_length = 0
    
    for i in range(len(s) - window_size + 1):
        current_window = s[i:i + window_size]
        # Process window
        max_length = max(max_length, len(current_window))
    
    return max_length
```

### **BFS Template**

```python
from collections import deque

def bfs_template(start, goal, get_neighbors):
    queue = deque([start])
    visited = {start}
    
    while queue:
        node = queue.popleft()
        
        if node == goal:
            return True
        
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False
```

### **DFS Template**

```python
def dfs_template(node, goal, visited, get_neighbors):
    if node == goal:
        return True
    
    visited.add(node)
    
    for neighbor in get_neighbors(node):
        if neighbor not in visited:
            if dfs_template(neighbor, goal, visited, get_neighbors):
                return True
    
    return False

# Call with:
dfs_template(start, goal, set(), neighbors_func)
```

### **DP Memoization Template**

```python
def dp_memoization(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = dp_memoization(n - 1, memo) + dp_memoization(n - 2, memo)
    return memo[n]
```

---

## 🚀 SECTION 8: BEFORE INTERVIEW CHECKLIST

Day before assessment:
- [ ] Run through data structures (5 mins each)
- [ ] Practice one problem from each pattern (20 mins)
- [ ] Review common mistakes section
- [ ] Make sure you can write sliding window/two pointers without thinking
- [ ] Test your Python syntax is fast (type a simple solution, time yourself)

Day of assessment:
- [ ] Start with identifying pattern (60 seconds)
- [ ] Write pseudocode (3 minutes)
- [ ] Code solution (10 minutes)
- [ ] Test with examples (5 minutes)

---

## 💡 REMEMBER

You're not learning Python. You're **remembering** how to use Python quickly under pressure.

Focus on:
✅ **Speed** (write solutions fast)
✅ **Accuracy** (correct algorithms)
✅ **Clarity** (readable code)

Not on:
❌ Fancy tricks
❌ One-liners
❌ Optimization edge cases

---

**You've got 3+ years backend experience. You know Python. This is just a refresh.**

Go crush it! 🚀
