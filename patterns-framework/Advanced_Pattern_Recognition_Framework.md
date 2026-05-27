# Advanced Pattern Recognition Framework
## Expert-Level Algorithm Detection from Problem Hints

---

## 🎯 THE PROBLEM WITH BASIC FRAMEWORKS

Your current framework is good, but it **only catches obvious keywords**. Real interviews use subtle hints:

**Obvious:** "Find substring" → Sliding Window ✓  
**Subtle:** "Efficiently access elements" → Hash Map / Binary Search (depends on context)

This advanced framework teaches you to **read between the lines** and catch the hidden signals.

---

## 🔥 LEVEL 1: PRIMARY HINT CATEGORIES

Instead of just keywords, look for these **hint categories**:

### **CATEGORY A: Order/Sequence Hints**

These hint at **sorting, searching, or sequence-based algorithms**:

```
🔍 Primary Hints:
- "sorted"
- "ascending" / "descending"
- "order matters"
- "in sequence"
- "before/after"
- "position"

→ Algorithm Family: TWO POINTERS, BINARY SEARCH, MERGING

Deep Dive Questions:
1. Is the array ALREADY sorted? 
   YES → Two Pointers or Binary Search (O(n) or O(log n))
   NO → Do you need to sort first? (adds O(n log n))

2. Are you looking for a SINGLE element or PAIRS?
   SINGLE → Binary Search
   PAIRS/TRIPLETS → Two Pointers (after sorting)

3. Is the sorted order part of the PROBLEM or just OPTIMIZATION?
   PART OF PROBLEM → Preserve sorting (Two Pointers)
   OPTIMIZATION → Sort if needed (Binary Search)

Example Problems:
- "Two numbers that sum to target" (sorted array) → Two Pointers
- "First and last position of target" (sorted array) → Binary Search (run twice)
- "Median of two sorted arrays" (sorted arrays) → Binary Search or Merge
```

### **CATEGORY B: Window/Range Hints**

These hint at **sliding window, prefix sum, or range queries**:

```
🔍 Primary Hints:
- "substring" / "subarray"
- "consecutive"
- "contiguous"
- "window"
- "within range"
- "max/min of every k elements"
- "all subarrays of size k"

→ Algorithm Family: SLIDING WINDOW, PREFIX SUM, MONOTONIC DEQUE

Deep Dive Questions:
1. Is the window SIZE FIXED or VARIABLE?
   FIXED → Simple Sliding Window
   VARIABLE → Shrink/expand based on condition

2. Do you need MAXIMUM/MINIMUM in window?
   YES → Monotonic Deque (O(n)) or Heap (O(n log n))
   NO → Regular Sliding Window (O(n))

3. Is it a SUBSTRING (needs condition) or just any SUBARRAY?
   SUBSTRING → Usually Sliding Window with hash map
   SUBARRAY → Could be Sliding Window or Prefix Sum

Example Problems:
- "Longest substring without repeating" → Sliding Window (variable size)
- "Maximum sum of subarray of size k" → Sliding Window (fixed size) or Deque
- "Minimum window substring" → Sliding Window (variable size)
- "Longest subarray with sum < k" → Prefix Sum or Sliding Window
```

### **CATEGORY C: Constraint Hints**

These hint at **data structure choice and complexity trade-offs**:

```
🔍 Primary Hints - For SPACE:
- "O(1) extra space"
- "in-place"
- "without extra data structure"
- "modify original"

→ Algorithm Family: TWO POINTERS, BIT MANIPULATION, SWAP

🔍 Primary Hints - For TIME:
- "as fast as possible"
- "optimal time"
- "minimize operations"

→ Algorithm Family: HASH MAP (O(n)), BINARY SEARCH (O(log n)), GREEDY

Deep Dive Questions:
1. O(1) space requirement?
   YES → Two Pointers, no hash maps allowed
   NO → Can use extra data structures

2. What's the constraint on n?
   n ≤ 20 → Backtracking, Bitmask DP (exponential fine)
   n ≤ 1000 → O(n²) algorithms okay (DP, nested loops)
   n ≤ 10⁶ → MUST be O(n) or O(n log n) (Hash Map or Sort)

3. "Find answer for EVERY element"?
   YES → Usually O(n) with hash map or monotonic stack
   NO → Can be slower

Example Problems:
- "Find duplicates in array (O(1) space)" → Fast & Slow Pointers or Bit Manipulation
- "Remove duplicates (in-place)" → Two Pointers
- "Next greater element for EACH element" → Monotonic Stack (O(n))
```

### **CATEGORY D: Generation Hints**

These hint at **backtracking, recursion, or combinatorics**:

```
🔍 Primary Hints:
- "all combinations"
- "all permutations"
- "all subsets"
- "generate all possible"
- "list all"
- "enumerate"

→ Algorithm Family: BACKTRACKING, DFS, RECURSION

Deep Dive Questions:
1. What are you generating?
   COMBINATIONS (order doesn't matter) → Backtracking with index
   PERMUTATIONS (order matters) → Backtracking with swap or used set
   SUBSETS (power set) → Backtracking or Bit Manipulation

2. Do you need ALL or just VALID ones?
   ALL → Backtracking with all branches
   VALID → Backtracking with early pruning

3. Any constraints?
   Sum equals X → Backtracking with pruning
   No duplicates → Backtracking with set
   Length exactly K → Backtracking with length check

Example Problems:
- "All combinations of length k" → Backtracking (combinations)
- "All permutations" → Backtracking (permutations)
- "All subsets" → Backtracking or Bit Manipulation
- "All paths in tree" → DFS/Backtracking
```

### **CATEGORY E: Optimization Hints**

These hint at **dynamic programming, greedy, or divide & conquer**:

```
🔍 Primary Hints:
- "minimum/maximum"
- "count ways"
- "best way"
- "optimal"
- "can you reach"
- "cost"
- "profit"

→ Algorithm Family: DYNAMIC PROGRAMMING, GREEDY, DIVIDE & CONQUER

Deep Dive Questions:
1. Can you solve SUBPROBLEMS independently?
   YES → Dynamic Programming (overlapping subproblems)
   NO → Greedy (make best local choice)

2. Do you need to TRACK DECISIONS or just the RESULT?
   TRACK → DP (build up solution)
   JUST RESULT → Greedy (one pass)

3. Can local optimal = global optimal?
   YES → Greedy (activity selection, huffman coding)
   NO → DP (knapsack, coin change)

4. Do you see OVERLAPPING SUBPROBLEMS?
   YES → DP with memoization
   NO → Could be greedy or recursion

5. DECISION at each step?
   YES → DP (multiple choices)
   NO → Greedy (obvious choice)

Example Problems:
- "Minimum coins to make amount" → DP (multiple choices)
- "Activity selection (max activities)" → Greedy (local optimal = global)
- "House robber (can't rob adjacent)" → DP (overlapping subproblems)
- "Jump game (can you reach end)" → DP or Greedy
```

### **CATEGORY F: Graph/Structure Hints**

These hint at **BFS, DFS, or topological sort**:

```
🔍 Primary Hints:
- "tree" / "graph" / "network"
- "connected" / "component"
- "path" / "shortest path"
- "level" / "depth"
- "cycle" / "loop"
- "visited" / "reachable"

→ Algorithm Family: BFS, DFS, TOPOLOGICAL SORT, UNION-FIND

Deep Dive Questions:
1. What do you need to find?
   SHORTEST PATH → BFS
   ALL PATHS → DFS
   ANY PATH → DFS or Backtracking
   CONNECTED COMPONENTS → DFS or Union-Find

2. Is it WEIGHTED or UNWEIGHTED graph?
   UNWEIGHTED → BFS (shortest path)
   WEIGHTED → Dijkstra's or Bellman-Ford

3. Do you need FULL TRAVERSAL or just finding ONE thing?
   FULL → BFS or DFS (both work)
   JUST ONE → Can stop early, DFS often better

4. Is order important (level-by-level)?
   YES → BFS (queue)
   NO → DFS (stack or recursion)

5. DIRECTED or UNDIRECTED?
   DIRECTED → Watch edge direction
   UNDIRECTED → Simpler, any direction

Example Problems:
- "Number of connected components" → DFS/BFS with visited
- "Shortest path in unweighted graph" → BFS
- "All paths from A to B" → DFS or Backtracking
- "Is there a cycle?" → DFS with recursion stack
```

---

## 🔑 LEVEL 2: INDIRECT HINT ANALYSIS

Sometimes the hints are **hidden in what the problem DOESN'T say**:

### **Hidden Hint 1: "Find elements without showing comparisons"**
```
Typical wording: "Find [answer] in O(n) time"

What this means:
- Can't sort (O(n log n))
- Can't use nested loops (O(n²))
- → Must use Hash Map or direct indexing

Example:
"Find duplicate in array in O(n) time, O(1) space"
- Can't use hash map (O(1) space requirement!)
- → Must use Fast & Slow Pointers
```

### **Hidden Hint 2: "Modify and track simultaneously"**
```
Typical wording: "Do this while [constraint]"

What this means:
- Can't pre-process (would change data)
- Must handle in single pass
- → Likely Sliding Window or One-Pass Algorithm

Example:
"Remove duplicates from sorted array in-place"
- Can't use extra space
- Must do in single pass
- → Two Pointers (left = read, right = write)
```

### **Hidden Hint 3: "Multiple queries on same data"**
```
Typical wording: "Preprocess the data, then answer multiple queries"

What this means:
- Setup phase: expensive preprocessing okay
- Query phase: must be FAST
- → Build Index (Hash Map, Segment Tree, etc.)

Example:
"Given array, answer multiple range sum queries"
- Preprocess: build prefix sum array (O(n))
- Query: answer instantly (O(1))
- → Prefix Sum Array pattern
```

### **Hidden Hint 4: "Compare with alternating constraint"**
```
Typical wording: "Can do X but not Y"

What this means:
- The forbidden thing is the obvious approach
- Must find clever alternative
- → Often a pattern you wouldn't normally think of

Example:
"Find majority element without hash map"
- Hash map is obvious (O(n) space)
- Forbidden → Must use Moore's Voting Algorithm (O(1) space)

"Kth largest without sorting"
- Sorting is obvious (O(n log n))
- Must use Heap (O(n log k)) or Quick Select (O(n))
```

---

## 🎯 LEVEL 3: COMBINATION ANALYSIS

**Real problems combine multiple hint categories. Use this to detect complex patterns:**

### **Pattern Combination 1: Sorted Array + Pairs + In-Place**
```
Hints Present:
- "sorted array"
- "find two numbers"
- "in-place" or "O(1) space"

Algorithm: TWO POINTERS

Why?
- Sorted → Two Pointers is fastest
- Pairs → Natural for Two Pointers
- In-place → No extra space needed

Example: Remove duplicates from sorted array
```

### **Pattern Combination 2: Unsorted Array + Pairs + Speed Critical**
```
Hints Present:
- "unsorted array"
- "find two numbers"
- "O(n) time"

Algorithm: HASH MAP

Why?
- Unsorted → Can't use Two Pointers (would need sort first)
- Pairs → Hash map for complement lookup
- O(n) time → Can't afford sorting (O(n log n))

Example: Two Sum (unsorted array)
```

### **Pattern Combination 3: Substring + Condition + Minimize/Maximize**
```
Hints Present:
- "substring" or "subarray"
- "without [constraint]"
- "longest" or "shortest"

Algorithm: SLIDING WINDOW

Why?
- Substring → Sliding Window signature
- Condition → Window changes based on condition
- Min/Max → Track best while sliding

Example: Longest substring without repeating characters
```

### **Pattern Combination 4: Tree/Graph + Shortest + Not Weighted**
```
Hints Present:
- "tree" or "graph"
- "shortest path"
- No mention of weights

Algorithm: BFS

Why?
- Unweighted → BFS guaranteed shortest
- Tree/Graph → Need traversal
- Shortest → BFS explores level-by-level

Example: Shortest path in grid
```

### **Pattern Combination 5: Any Structure + All Paths + Count Ways**
```
Hints Present:
- "all paths"
- "count ways"
- "combinations of"

Algorithm: DFS + MEMOIZATION (DP)

Why?
- All paths → Need DFS exploration
- Count ways → Same subproblems repeat
- Memoization → Avoid recalculation

Example: Number of paths in grid with obstacles
```

---

## 🚀 LEVEL 4: ADVANCED HINT DECODING

### **Hint Type 1: "Efficient Access" Phrases**

When you see:
- "efficiently access"
- "quickly find"
- "instant lookup"

Think: **What structure gives instant access?**
- Hash Map → O(1) lookup by key
- Balanced Binary Search Tree → O(log n) sorted access
- Heap → O(1) access to min/max
- Array index → O(1) if you know index

### **Hint Type 2: "Multiple Operations" Phrases**

When you see:
- "support multiple operations"
- "query and update"
- "insert, delete, search"

Think: **What structure is good at multiple ops?**
- Hash Map → insert O(1), delete O(1), search O(1)
- Binary Search Tree → all O(log n)
- Heap → insert O(log n), delete O(log n), max O(1)
- Segment Tree → range query O(log n), update O(log n)

### **Hint Type 3: "Relationship Between Elements" Phrases**

When you see:
- "elements are related"
- "parent-child relationship"
- "connected elements"
- "pairs of elements"

Think: **Graph/Tree structure hints**
- Parent-child → Tree (DFS/BFS)
- Connected elements → Graph (DFS/BFS/Union-Find)
- Pairs → Often needs sorting or Two Pointers

### **Hint Type 4: "Forbidden Operation" Phrases**

When you see:
- "can't use [X]"
- "without [X]"
- "except [X]"
- "O(1) space" (no extra structures allowed)

This **eliminates obvious approaches**. Think of alternatives:
- Can't sort → Hash Map or original order must work
- Can't use extra space → Two Pointers or Bit Manipulation
- Can't modify input → Usually backtracking or DFS

---

## 📋 ADVANCED DETECTION FLOWCHART

```
START: Read problem carefully

│
├─ STEP 1: What is the DATA STRUCTURE?
│   ├─ Array/List/String → Continue
│   ├─ Tree → Graph Algorithms (BFS/DFS)
│   ├─ Graph → Graph Algorithms (BFS/DFS/Topological)
│   └─ Linked List → Pointer Manipulation (Two Pointers, Fast&Slow)
│
├─ STEP 2: What CONSTRAINTS are given?
│   ├─ O(1) space? → Two Pointers or Bit Manipulation
│   ├─ O(n) time? → No nesting, Hash Map or Sliding Window
│   ├─ O(log n) time? → Binary Search or Tree traversal
│   └─ n ≤ 20? → Backtracking/Bitmask DP
│
├─ STEP 3: What OPERATION are you doing?
│   ├─ Finding pairs/triplets → Two Pointers or Hash Map
│   ├─ Finding substring/subarray → Sliding Window
│   ├─ Generating all → Backtracking
│   ├─ Finding optimal → DP or Greedy
│   ├─ Traversing structure → BFS/DFS
│   └─ Counting frequencies → Hash Map or Counter
│
├─ STEP 4: Are there SPECIAL CONSTRAINTS?
│   ├─ "Find element that appears once" → XOR trick or Hash Map
│   ├─ "Find missing number" → Sum formula or XOR
│   ├─ "Find duplicate" → Fast & Slow or Hash Map
│   ├─ "Find intersection/union" → Hash Map or Sort
│   └─ "Merge/combine" → Sort or Two Pointers
│
└─ STEP 5: Check COMBINATIONS
    └─ Combine answers from steps 1-4
        → Final algorithm choice
```

---

## 🎓 PRACTICE PROBLEMS WITH HINT ANALYSIS

### **Problem 1: "Given an unsorted array, find two numbers that add to target"**

```
Hint Analysis:
1. Data: Array (unsorted) → Can't use Two Pointers directly
2. Constraint: Typically O(n) expected
3. Operation: Find pairs that sum to target
4. Combination: Unsorted + Pairs + O(n)

→ Algorithm: HASH MAP

Code insight:
for num in arr:
    complement = target - num
    if complement in hash_set:  # O(1) lookup
        return [num, complement]
    hash_set.add(num)
```

### **Problem 2: "Find the longest substring without repeating characters"**

```
Hint Analysis:
1. Data: String (array of chars)
2. Operation: Substring with condition
3. Constraint: Maximize/minimize → "longest"
4. Pattern: "without repeating" = condition

→ Algorithm: SLIDING WINDOW (variable size)

Key insight:
- Window expands when no repeats
- Window contracts when repeating character found
- Use hash map to track last seen position
```

### **Problem 3: "Find if linked list has a cycle"**

```
Hint Analysis:
1. Data: Linked List
2. Operation: Detect cycle
3. Constraint: O(1) space mentioned? (usually)
4. Pattern: "cycle" = pointer relationship hint

→ Algorithm: FAST & SLOW POINTERS

Key insight:
- Can't use hash map (would be O(n) space)
- Pointers moving at different speeds will meet if cycle
- Two pointers naturally detect cycles
```

### **Problem 4: "Count the number of ways to climb stairs (1 or 2 steps)"**

```
Hint Analysis:
1. Operation: "count ways" → DP signature
2. Constraint: "choices at each step" (1 or 2)
3. Pattern: Overlapping subproblems (f(n) = f(n-1) + f(n-2))
4. Key phrase: "ways" = DP

→ Algorithm: DYNAMIC PROGRAMMING

Key insight:
- Each position can be reached from 2 previous positions
- Memoization: solve f(n) once, reuse result
- Bottom-up: build from f(1), f(2) to f(n)
```

---

## ✅ ADVANCED DETECTION CHECKLIST

Before coding, verify you caught ALL hints:

```
Data Structure Hints:
 ☐ Is it array/list/string/linked-list/tree/graph?
 ☐ Is it sorted or unsorted?
 ☐ Is there a specific structure (pairs, nodes)?

Operation Hints:
 ☐ Am I finding, generating, optimizing, or traversing?
 ☐ What exactly am I looking for (element, path, count, optimal)?
 ☐ Do multiple subproblems exist?

Constraint Hints:
 ☐ What's the time requirement (O(n), O(log n), O(n²))?
 ☐ What's the space requirement (O(1), O(n))?
 ☐ What's the value of n (small/large)?
 ☐ Are there forbidden operations ("without X", "in-place")?

Combination Hints:
 ☐ Does this problem combine hints?
 ☐ Do multiple hints point to same algorithm? (confidence check)
 ☐ Are there contradictory hints? (might need clever approach)

Pattern Recognition:
 ☐ Have I seen a similar problem?
 ☐ Do known patterns apply?
 ☐ What's the least obvious algorithm that fits?
```

---

## 💡 KEY INSIGHTS FOR MASTERY

### **Insight 1: Forbidden Operations = Hint**
When problem says "can't do X", it's telling you X is the obvious (slow) approach.
→ Find the clever alternative.

### **Insight 2: Multiple Constraints = Narrowing**
More constraints = fewer possible algorithms.
- "O(1) space" eliminates Hash Map
- "Sorted" hints at Two Pointers or Binary Search
- Both together = Very specific algorithm

### **Insight 3: Problem Wording Matters**
- "Find A number" → Might be any, first one okay
- "Find THE number" → Specific, usually unique
- "Find ALL numbers" → Backtracking/DFS
- "Find BEST number" → Optimization (DP/Greedy)

### **Insight 4: Hidden Complexity Hints**
- "Find kth" → Heap or Quick Select
- "Median" → Two Pointers or Binary Search
- "Rank" → Sorted order implied
- "Frequency" → Hash Map implied

---

## 🎯 FINAL FRAMEWORK: 60-SECOND PATTERN DETECTION

```
[0-10 seconds] Read problem, identify data structure and operation

[10-20 seconds] Highlight all HINTS:
- Constraints (time, space, O(n))
- Special phrases ("without", "all", "ways")
- Forbidden operations

[20-40 seconds] Match hints to patterns:
- Does data suggest algorithm family?
- Do constraints eliminate algorithms?
- Do operations confirm choice?

[40-50 seconds] Verify with combination analysis:
- Do multiple hints point to same algorithm?
- Is there contradiction? (might need clever approach)

[50-60 seconds] Start coding with confidence
```

---

**This advanced framework lets you detect algorithms even when they're hidden in subtle wording!**

Use this alongside your pattern recognition PDF for maximum coverage. 🚀