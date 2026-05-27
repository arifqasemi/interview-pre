# Algorithm Characteristics & Personality Guide
## Understand Each Algorithm Deeply to Match Problems Perfectly

---

## 🎯 WHAT THIS GUIDE DOES

You now have:
✅ Pattern Recognition Framework (detect algorithm from hints)
✅ Advanced Hint Analysis (catch subtle signals)

But you're missing:
❌ Deep understanding of EACH algorithm's "personality"
❌ Why algorithm X is better than Y for specific situations
❌ How algorithms fail when misused

This guide teaches you the **personality and characteristic** of each algorithm so you can:
1. Understand WHY it works
2. Know WHEN it fails
3. Recognize it in disguised problems
4. Choose between competing algorithms

---

## 🧩 ALGORITHM PERSONALITY PROFILES

### **ALGORITHM 1: TWO POINTERS**

**Personality:** "The Speedwalker"
- Fast, simple, elegant
- Works best in ORGANIZED (sorted) environment
- Naive but effective
- No extra memory needed

**Key Characteristics:**
```
WHEN IT THRIVES:
✓ Input is SORTED or can be sorted
✓ Need to find PAIRS/TRIPLETS
✓ Space is limited (O(1) required)
✓ Need SPEED over complexity

WHEN IT FAILS:
✗ Input is unsorted (need sort first)
✗ Need frequency counting
✗ Need to compare non-adjacent elements
✗ Order matters and can't be changed

TIME COMPLEXITY: O(n) if sorted, O(n log n) if need to sort first
SPACE COMPLEXITY: O(1) or O(log n) for sorting

PERSONALITY TRAITS:
- Simple and straightforward
- Can't handle complexity
- Needs organized input
- Returns immediately when found
```

**Real-World Analogy:**
"Looking for two people with specific heights in a LINE. If they're already in line (sorted), you use two pointers. If they're scattered (unsorted), you first line them up (sort), then use two pointers."

**Usage Patterns:**
```python
# PATTERN 1: Find pair that sums to target (SORTED array)
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum

# PATTERN 2: Remove duplicates in-place
def remove_duplicates(arr):
    left = 0  # Write pointer
    for right in range(1, len(arr)):  # Read pointer
        if arr[right] != arr[right - 1]:
            left += 1
            arr[left] = arr[right]
    return left + 1

# PATTERN 3: Container with most water
def max_area(heights):
    left, right = 0, len(heights) - 1
    max_area = 0
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        max_area = max(max_area, area)
        # Move the shorter pointer (to look for taller)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area
```

**Problems It Solves:**
- Two Sum (sorted)
- 3Sum
- Valid Palindrome
- Remove Duplicates
- Container With Most Water
- Merge Sorted Arrays

---

### **ALGORITHM 2: SLIDING WINDOW**

**Personality:** "The Window Shopper"
- Methodical, thorough
- Looks at problems piece by piece
- Keeps context of recent history
- Adjusts approach as it learns

**Key Characteristics:**
```
WHEN IT THRIVES:
✓ Problem involves SUBSTRING/SUBARRAY
✓ Need to find element based on CONDITION
✓ Condition applies to CONSECUTIVE elements
✓ Want to avoid nested loops

WHEN IT FAILS:
✗ Need random access to non-consecutive elements
✗ Can't maintain "window" context
✗ Problem asks for non-contiguous answer
✗ Window size is unknown and unbounded

TIME COMPLEXITY: O(n) - each element visited at most twice
SPACE COMPLEXITY: O(min(n, charset)) - for hash map

PERSONALITY TRAITS:
- Methodical and thorough
- Learns from recent context
- Adjusts window size dynamically
- Excellent memory (remembers what was in window)
```

**Real-World Analogy:**
"Reading a book through a small window in the wall. You can only see a few lines at a time. You slide the window down the page, remembering what you saw before, until you find what you're looking for."

**Usage Patterns:**
```python
# PATTERN 1: Fixed window size
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum

# PATTERN 2: Variable window size - expand when valid, shrink when invalid
def longest_substring_without_repeating(s):
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If char seen recently, move window start
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

# PATTERN 3: Shrink window until condition met
def min_window_substring(s, t):
    if not t or not s or len(t) > len(s):
        return ""
    
    required = {}
    for char in t:
        required[char] = required.get(char, 0) + 1
    
    formed = 0
    window_counts = {}
    left, right = 0, 0
    ans = float("inf"), None, None
    
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in required and window_counts[char] == required[char]:
            formed += 1
        
        while formed == len(required) and left <= right:
            char = s[left]
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[char] -= 1
            if char in required and window_counts[char] < required[char]:
                formed -= 1
            left += 1
        right += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
```

**Problems It Solves:**
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Maximum Sum Subarray of Size K
- All Anagrams in String
- Longest Repeating Character Replacement

---

### **ALGORITHM 3: HASH MAP**

**Personality:** "The Memorizer"
- Never forgets anything it's seen
- Excellent at quick lookups
- Trades memory for speed
- Works with unsorted data

**Key Characteristics:**
```
WHEN IT THRIVES:
✓ Need fast LOOKUP (O(1))
✓ Need to COUNT FREQUENCIES
✓ Input is UNSORTED
✓ Need to store RELATIONSHIPS
✓ Many queries on same data

WHEN IT FAILS:
✗ Memory is very limited (O(n) space required)
✗ Need SORTED order
✗ Need min/max of range
✗ Need to process in sequence

TIME COMPLEXITY: O(n) for lookup/insert/delete on average
SPACE COMPLEXITY: O(n) - stores all unique elements

PERSONALITY TRAITS:
- Never forgets what it's seen
- Instant recall (O(1) lookup)
- Memory-intensive
- Great for frequency problems
- Perfect for finding complements/pairs
```

**Real-World Analogy:**
"Having a personal assistant who remembers EVERYTHING they've seen. You can ask 'Have you seen a person with height 170cm?' and they instantly tell you. But they need a huge notebook to remember everything."

**Usage Patterns:**
```python
# PATTERN 1: Complement lookup (Two Sum)
def two_sum(arr, target):
    seen = {}
    for num in arr:
        complement = target - num
        if complement in seen:  # O(1) lookup
            return [seen[complement], arr.index(num)]
        seen[num] = arr.index(num)
    return []

# PATTERN 2: Frequency counting
def majority_element(arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)  # O(n) to find max

# PATTERN 3: Storing relationships
def group_anagrams(words):
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

# PATTERN 4: Finding duplicates
def contains_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:  # O(1) lookup
            return True
        seen.add(num)
    return False

# PATTERN 5: Intersection of two arrays
def intersection(arr1, arr2):
    set1 = set(arr1)
    return [x for x in arr2 if x in set1]  # O(1) membership test
```

**Problems It Solves:**
- Two Sum (unsorted)
- Contains Duplicate
- Valid Anagram
- Group Anagrams
- Majority Element
- Intersection of Arrays
- Word Pattern

---

### **ALGORITHM 4: BINARY SEARCH**

**Personality:** "The Divider"
- Extremely efficient
- Requires organized input
- Thinks logarithmically (divide & conquer)
- Precise and calculated

**Key Characteristics:**
```
WHEN IT THRIVES:
✓ Input is SORTED
✓ Need to find SPECIFIC element
✓ Need O(log n) speed
✓ Can DISCARD half of remaining elements

WHEN IT FAILS:
✗ Input is unsorted (would need sort first)
✗ Duplicate elements complicate things
✗ Need multiple elements (not just one)
✗ Can't discard half (like frequency counting)

TIME COMPLEXITY: O(log n) - eliminates half each iteration
SPACE COMPLEXITY: O(1) or O(log n) for recursion

PERSONALITY TRAITS:
- Extremely efficient
- Needs organized input
- Thinks in halves/divisions
- Good for single target search
- Struggles with duplicates
```

**Real-World Analogy:**
"Searching for a name in a phone book. You open to the middle, see if you're before or after the name you want, then discard half the book and repeat. Very efficient for sorted data."

**Usage Patterns:**
```python
# PATTERN 1: Find target in sorted array
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Not found

# PATTERN 2: Find first occurrence (leftmost)
def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# PATTERN 3: Find last occurrence (rightmost)
def find_last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# PATTERN 4: Find insertion position
def search_insert_position(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

# PATTERN 5: Search in rotated sorted array
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        
        # Determine which half is sorted
        if arr[left] <= arr[mid]:  # Left half sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Target in sorted half
            else:
                left = mid + 1  # Target in right half
        else:  # Right half sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1  # Target in sorted half
            else:
                right = mid - 1  # Target in left half
    
    return -1
```

**Problems It Solves:**
- Search in Sorted Array
- First Bad Version
- Search Insert Position
- Find Peak Element
- Search in Rotated Sorted Array
- Median of Two Sorted Arrays

---

### **ALGORITHM 5: DYNAMIC PROGRAMMING**

**Personality:** "The Planner"
- Thinks ahead and plans
- Remembers past decisions
- Builds solutions bottom-up or top-down
- Solves overlapping subproblems efficiently

**Key Characteristics:**
```
WHEN IT THRIVES:
✓ Problem has OVERLAPPING SUBPROBLEMS
✓ Problem has OPTIMAL SUBSTRUCTURE
✓ Need to track DECISIONS/CHOICES
✓ Multiple paths lead to same state
✓ "Count ways" or "find optimal"

WHEN IT FAILS:
✗ No overlapping subproblems
✗ Each subproblem is unique
✗ Solution is greedy (local optimal = global optimal)
✗ Problem too simple for memoization overhead

TIME COMPLEXITY: O(n) to O(n²) depending on states and transitions
SPACE COMPLEXITY: O(n) for memoization

PERSONALITY TRAITS:
- Foresight and planning
- Remembers past work (memoization)
- Builds incrementally
- Avoids redundant calculations
- Good for complex decision-making
```

**Real-World Analogy:**
"Planning a road trip. Instead of trying every possible route (exponential), you remember: 'I've already figured out the best way from City C to destination.' So when you reach City C from a different route, you reuse that calculation."

**Usage Patterns:**
```python
# PATTERN 1: Memoization (Top-Down)
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# PATTERN 2: Tabulation (Bottom-Up)
def fib_tab(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# PATTERN 3: Coin Change (minimum coins)
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# PATTERN 4: House Robber (can't rob adjacent)
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(
            dp[i-1],  # Don't rob current
            dp[i-2] + nums[i]  # Rob current
        )
    
    return dp[-1]

# PATTERN 5: Count ways
def count_ways(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # One way to make 0: take nothing
    
    for i in range(1, n + 1):
        # Choices: take 1 step, take 2 steps
        dp[i] = dp[i-1] + (dp[i-2] if i >= 2 else 0)
    
    return dp[n]
```

**Problems It Solves:**
- Fibonacci
- Coin Change
- House Robber
- Longest Increasing Subsequence
- Edit Distance
- Knapsack Problem
- Maximum Product Subarray

---

### **ALGORITHM 6: BACKTRACKING**

**Personality:** "The Explorer"
- Tries every possibility
- Abandons dead-ends quickly
- Systematic and thorough
- Can be slow but complete

**Key Characteristics:**
```
WHEN IT THRIVES:
✓ Need ALL solutions (not just one)
✓ Solutions have TREE/FOREST structure
✓ Can PRUNE dead branches
✓ Problem size is SMALL (n ≤ 20)
✓ "Generate all" or "find all"

WHEN IT FAILS:
✗ Only need ONE solution (use BFS/DFS instead)
✗ Problem size is LARGE (exponential time killer)
✗ Can't prune effectively
✗ Performance is critical

TIME COMPLEXITY: O(2^n) to O(n!) - exponential
SPACE COMPLEXITY: O(n) for recursion stack

PERSONALITY TRAITS:
- Explores systematically
- Commits and backtracks
- Good at pruning dead ends
- Complete but slow
- Good for small problems
```

**Real-World Analogy:**
"Exploring a maze. You try a path, if it's a dead end, you backtrack and try another. You continue until you've tried all paths or found the exit. If there are multiple exits, you find all of them."

**Usage Patterns:**
```python
# PATTERN 1: Permutations
def permute(nums):
    result = []
    
    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return
        
        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()  # Backtrack
    
    backtrack([], nums)
    return result

# PATTERN 2: Combinations
def combine(n, k):
    result = []
    
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()  # Backtrack
    
    backtrack(1, [])
    return result

# PATTERN 3: Subsets
def subsets(nums):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result

# PATTERN 4: N-Queens with pruning
def solve_nqueens(n):
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonals
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def backtrack(row):
        if row == n:
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(row, col):  # Pruning
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'  # Backtrack
    
    backtrack(0)
    return result
```

**Problems It Solves:**
- Permutations
- Combinations
- Subsets
- N-Queens
- Word Search
- Generate Parentheses
- Letter Combinations of Phone Number

---

### **ALGORITHM 7: BFS (Breadth-First Search)**

**Personality:** "The Explorer Who Explores Level by Level"
- Systematic and level-by-level
- Finds SHORTEST PATH in unweighted graph
- Uses queue (first in, first out)
- Good for "closest" or "nearest" problems

**Key Characteristics:**
```
WHEN IT THRIVES:
✓ Need SHORTEST PATH (unweighted)
✓ Need LEVEL-BY-LEVEL exploration
✓ Graph/Tree exploration
✓ Connected components
✓ "Nearest" or "closest"

WHEN IT FAILS:
✗ Weighted graph (use Dijkstra)
✗ Only need any path (DFS is simpler)
✗ Memory is limited (uses queue)
✗ Graph is very large and sparse

TIME COMPLEXITY: O(V + E) where V = vertices, E = edges
SPACE COMPLEXITY: O(V) for queue

PERSONALITY TRAITS:
- Methodical level-by-level
- Guarantees shortest path
- Uses extra memory (queue)
- Good for unweighted problems
- Fair to all directions (not biased)
```

**Real-World Analogy:**
"Flood fill. Water spreads level by level from a source. First reaches nearby cells, then farther cells. The first cell reached is always the closest."

**Usage Patterns:**
```python
from collections import deque

# PATTERN 1: Shortest path in grid
def shortest_path(grid, start, end):
    queue = deque([start])
    visited = {start}
    distance = {start: 0}
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            return distance[end]
        
        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    
    return -1  # No path

# PATTERN 2: Level order traversal
def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# PATTERN 3: Number of connected components
def count_components(graph):
    visited = set()
    count = 0
    
    for node in range(len(graph)):
        if node not in visited:
            count += 1
            queue = deque([node])
            visited.add(node)
            
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
    
    return count
```

**Problems It Solves:**
- Shortest Path in Grid
- Level Order Traversal
- Word Ladder
- Number of Islands
- Connected Components
- Binary Tree Level Order

---

### **ALGORITHM 8: DFS (Depth-First Search)**

**Personality:** "The Deep Explorer"
- Goes deep before going wide
- Explores one path completely
- Uses recursion or stack
- Good for "all paths" problems

**Key Characteristics:**
```
WHEN IT THRIVES:
✓ Need ALL PATHS (not just shortest)
✓ Memory is limited (uses less than BFS)
✓ Graph/Tree exploration
✓ Connected components
✓ Topological sorting
✓ Detecting cycles

WHEN IT FAILS:
✗ Need SHORTEST PATH (BFS is better)
✗ Stack overflow risk (very deep recursion)
✗ Graph is cyclic (need visited set)
✗ Problem needs level-by-level processing

TIME COMPLEXITY: O(V + E)
SPACE COMPLEXITY: O(V) for recursion stack

PERSONALITY TRAITS:
- Goes deep and commits
- Finds all paths
- Uses recursion naturally
- Good for cycle detection
- Can overflow on deep trees
```

**Real-World Analogy:**
"Exploring a cave system. You go deep into one tunnel, explore completely, backtrack, then try another tunnel. You eventually explore all tunnels."

**Usage Patterns:**
```python
# PATTERN 1: All paths DFS
def all_paths(graph, start, end):
    result = []
    
    def dfs(node, path):
        if node == end:
            result.append(path[:])
            return
        
        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()
    
    dfs(start, [start])
    return result

# PATTERN 2: Detect cycle
def has_cycle(graph):
    visited = set()
    rec_stack = set()
    
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:  # Back edge = cycle
                return True
        
        rec_stack.remove(node)
        return False
    
    for node in range(len(graph)):
        if node not in visited:
            if dfs(node):
                return True
    
    return False

# PATTERN 3: Topological sort
def topological_sort(graph):
    visited = set()
    stack = []
    
    def dfs(node):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        
        stack.append(node)
    
    for node in range(len(graph)):
        if node not in visited:
            dfs(node)
    
    return stack[::-1]
```

**Problems It Solves:**
- All Paths
- Clone Graph
- Detect Cycle in Graph
- Topological Sort
- Number of Islands (DFS variant)
- Valid Binary Search Tree

---

## 📊 ALGORITHM COMPARISON CHART

```
Algorithm      | Time      | Space    | Use When                      | Fails When
               |           |          |                               |
Two Pointers   | O(n)      | O(1)     | Need pairs, input sorted      | Input unsorted, need counting
Sliding Window | O(n)      | O(k)     | Substring with condition      | Non-contiguous elements
Hash Map       | O(n)      | O(n)     | Need fast lookup, counting    | Memory limited
Binary Search  | O(log n)  | O(1)     | Sorted input, single target   | Unsorted, need multiple
DP             | O(n-n²)   | O(n)     | Overlapping subproblems      | No overlapping, simple
Backtracking   | O(2^n)    | O(n)     | Generate all, small n        | Large n, need one answer
BFS            | O(V+E)    | O(V)     | Shortest path, level-order   | Need all paths, memory limit
DFS            | O(V+E)    | O(V)     | All paths, cycle detect      | Deep recursion, need shortest
```

---

## 🎯 MATCHING PROBLEMS TO ALGORITHMS

**When You See These CHARACTERISTICS, Use:**

```
"Fast lookup" + "Unsorted"
→ HASH MAP

"Find pairs" + "Sorted"
→ TWO POINTERS

"Substring" + "Condition"
→ SLIDING WINDOW

"Sorted" + "Single element"
→ BINARY SEARCH

"Overlapping subproblems" + "Optimization"
→ DYNAMIC PROGRAMMING

"Generate all" + "Small n"
→ BACKTRACKING

"Shortest path" + "Unweighted"
→ BFS

"All paths" + "Graph exploration"
→ DFS
```

---

## 💡 CHOOSING BETWEEN COMPETING ALGORITHMS

**Two Pointers vs Hash Map:**
```
Two Pointers:
- Data is sorted ✓
- Space is critical ✓
- Finding pairs ✓
→ Use Two Pointers

Hash Map:
- Data is unsorted ✓
- Space is available ✓
- Finding complement ✓
→ Use Hash Map
```

**BFS vs DFS:**
```
BFS:
- Need shortest path ✓
- Unweighted graph ✓
- Level-order matters ✓
→ Use BFS

DFS:
- Need all paths ✓
- Can handle weighted ✓
- Cycle detection ✓
→ Use DFS
```

**DP vs Greedy:**
```
DP:
- Overlapping subproblems ✓
- Multiple choices ✓
- Need to track decisions ✓
→ Use DP

Greedy:
- Local optimal = global ✓
- Only one choice at each step ✓
- Can't look ahead ✓
→ Use Greedy
```

---

## ✅ USE THIS CHECKLIST

Before choosing an algorithm:

```
□ What is the algorithm's PRIMARY STRENGTH?
  (fast lookup, all solutions, shortest path, optimal, etc.)

□ Does my problem NEED this primary strength?
  YES → Candidate
  NO → Eliminate

□ What does the algorithm REQUIRE?
  (sorted input, no duplicates, O(1) space, etc.)

□ Does my problem PROVIDE what's required?
  YES → Strong candidate
  NO → Eliminate or adapt

□ Are there COMPETING algorithms?
  Compare trade-offs (time vs space, correctness vs speed)

□ What would BREAK this algorithm?
  (unsorted for Two Pointers, large n for Backtracking)
  Does my problem have these breaking conditions?

□ Final answer: BEST algorithm for THIS problem
```

---

**Now you have:**
✅ Pattern Recognition Framework
✅ Advanced Hint Analysis
✅ Algorithm Characteristics & Personalities (THIS)

**Together = Complete System to Match ANY Problem to Algorithm! 🚀**