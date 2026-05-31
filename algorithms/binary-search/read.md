# 2-3 DAY BINARY SEARCH INTERVIEW CRASH COURSE
## Master Binary Search with Deep Understanding + Interview Problems

---

## OVERVIEW

| Day | Focus | Time | Outcome |
|-----|-------|------|---------|
| **Day 1** | Understand + Core Patterns | 3-4 hrs | Implement 5 patterns, understand concepts |
| **Day 2** | Practice + LeetCode Problems | 3-4 hrs | Solve 7 LeetCode problems |
| **Day 3** | Advanced + Mock Interview | 2-3 hrs | Binary search on answer, mixed problems |

---

## ✅ DAY 1: UNDERSTAND & PRACTICE BASICS

### Morning: Learn the Concept (1 hour)

**Step 1: Understand Core Idea (20 mins)**
- Read: `binary_search_guide.md` Part 1
- **Visualize on paper:**
  ```
  [1, 3, 5, 7, 9, 11, 13, 15]
  Find 7:
  
  Step 1: Check middle (9) → too large, search left
  [1, 3, 5, 7]
  
  Step 2: Check middle (5) → too small, search right
  [7]
  
  Step 3: Check middle (7) → FOUND!
  ```

**Step 2: Three Main Templates (30 mins)**
- Read: `binary_search_guide.md` Part 6 (Cheat Sheet)
- Copy these 3 templates into your notes:
  1. Basic binary search: `left <= right`
  2. Find first/last: `left <= right`, save result
  3. Find boundary: `left < right`, `right = len(arr)`
- Write them out by hand (not copy-paste!)

**Step 3: Key Insights (10 mins)**
- Binary search works because we **eliminate half the search space** each iteration
- The two-pointer approach (`left` and `right`) narrows the gap
- Time complexity is O(log n) because of this halving

### Afternoon: Implement & Practice (2.5-3 hours)

**Activity 1: Implement Patterns (3 times each - 2 hours)**

Do this three times for EACH pattern:
1. **First time**: With guide open, copy and understand
2. **Second time**: With guide closed, from memory
3. **Third time**: Timed (should take < 2 mins)

**The 5 Patterns to Master:**

Pattern 1: Basic Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

Test with:
- `[1, 3, 5, 7, 9]`, find 5 → 2
- `[1, 3, 5, 7, 9]`, find 2 → -1
- `[5]`, find 5 → 0

Pattern 2: Find First Occurrence
```python
def find_first(arr, target):
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
```

Test with:
- `[1, 2, 2, 2, 3]`, find 2 → 1
- `[1, 1, 1]`, find 1 → 0

Pattern 3: Find Last Occurrence
```python
def find_last(arr, target):
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
```

Test with:
- `[1, 2, 2, 2, 3]`, find 2 → 3
- `[1, 1, 1]`, find 1 → 2

Pattern 4: Find Boundary (Insertion Point)
```python
def find_boundary(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

Test with:
- `[1, 3, 5, 7]`, find 4 → 2 (insert at index 2)
- `[1, 3, 5, 7]`, find 0 → 0 (insert at start)
- `[1, 3, 5, 7]`, find 10 → 4 (insert at end)

Pattern 5: Find in Rotated Array
```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        
        if arr[left] <= arr[mid]:  # Left half sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

Test with:
- `[4, 5, 6, 7, 0, 1, 2]`, find 0 → 4
- `[4, 5, 6, 7, 0, 1, 2]`, find 7 → 3

**Activity 2: Trace by Hand (30 mins)**

Take these arrays and trace the ENTIRE binary search process on paper:

Example 1: `[1, 3, 5, 7, 9, 11]`, find 7
```
Step 1: left=0, right=5, mid=2
        arr[2]=5, 5<7, so left=3
Step 2: left=3, right=5, mid=4
        arr[4]=9, 9>7, so right=3
Step 3: left=3, right=3, mid=3
        arr[3]=7, FOUND!
```

Example 2: `[1, 2, 2, 2, 3]`, find_first of 2
```
Step 1: left=0, right=4, mid=2
        arr[2]=2, MATCH! result=2, right=1
Step 2: left=0, right=1, mid=0
        arr[0]=1, 1<2, left=1
Step 3: left=1, right=1, mid=1
        arr[1]=2, MATCH! result=1, right=0
Step 4: left=1, right=0, left > right, STOP
        Return result=1
```

Do this for:
- `[1, 3, 5, 7]`, find_boundary of 6
- `[4, 5, 6, 7, 0, 1]`, find 0 (rotated)

**Activity 3: Answer These Questions (15 mins)**

Write answers to these:
1. Q: Why is it `left <= right` for basic binary search but `left < right` for find_boundary?
2. Q: What's the time complexity and why?
3. Q: Can you binary search on unsorted data?
4. Q: Why must the middle be calculated as `(left + right) // 2`?
5. Q: What happens if you accidentally use `(left + right) / 2` (float division)?

### Evening: Review & Consolidate (30 mins)

- Write down all 5 patterns from memory
- Do you understand each one? If not, re-read that section
- Feeling confident? Move to Day 2. If not, practice one more time.

---

## ✅ DAY 2: PRACTICE & SOLVE LEETCODE PROBLEMS

### Morning: Quick Review (30 mins)

**Implement all 5 patterns one more time from scratch:**
- Basic binary search
- Find first
- Find last
- Find boundary
- Find in rotated array

If you can do all 5 in under 10 minutes total, you're ready for LeetCode.

### Afternoon: Solve LeetCode Problems (3-3.5 hours)

**Solve these 7 problems in order:**

#### Problem 1: LeetCode 704 - Binary Search ⭐
**Difficulty:** Easy | **Time:** 15 mins

```
Given a sorted array of integers nums and an integer target, 
return the index of target if it is in nums, or -1 otherwise.
```

**Approach:**
- This is literally the basic binary search pattern
- Directly implement what you learned

**My approach:**
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**After solving:** Ask yourself: "Is there a simpler way? Is there a worse approach?" (Yes: linear search O(n), but binary search O(log n) is better)

---

#### Problem 2: LeetCode 35 - Search Insert Position ⭐
**Difficulty:** Easy | **Time:** 20 mins

```
Given a sorted array and a target value, return the index if found.
If not, return the index where it would be if it were inserted in order.
```

**Approach:**
- This is the `find_boundary` pattern!
- Example: `[1,3,5,6]`, target=5 → 2
- Example: `[1,3,5,6]`, target=4 → 2 (insert position)

**Hint:** Use the `find_boundary` pattern:
```python
def searchInsert(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

**After solving:** Notice that both found and not-found cases return the same thing!

---

#### Problem 3: LeetCode 34 - Find First and Last Position ⭐⭐
**Difficulty:** Medium | **Time:** 25 mins

```
Given a sorted array nums of n integers, find the starting and ending 
position of a given target value. If not found, return [-1, -1].
```

**Approach:**
- Use `find_first` to find leftmost occurrence
- Use `find_last` to find rightmost occurrence
- Return `[first, last]`

**Example:** `[5,7,7,8,8,10]`, target=8 → `[3,4]`

**Hint:**
```python
def searchRange(nums, target):
    first = find_first(nums, target)
    if first == -1:
        return [-1, -1]
    last = find_last(nums, target)
    return [first, last]
```

**After solving:** This combines two patterns. Did you understand why we need two separate functions?

---

#### Problem 4: LeetCode 33 - Search in Rotated Sorted Array ⭐⭐
**Difficulty:** Medium | **Time:** 30 mins

```
Search for a target value in a rotated sorted array.
Example: [4,5,6,7,0,1,2], target=0 → 4
```

**Approach:**
- Determine which half is sorted
- Check if target is in the sorted half
- Recursively search the appropriate half

**Key insight:** One half is always sorted after rotation

**Hint:**
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:  # Left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target in left
            else:
                left = mid + 1   # Target in right
        else:  # Right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Target in right
            else:
                right = mid - 1  # Target in left
    return -1
```

**After solving:** Can you rotate the array mentally? Test with `[4,5,6,7,0,1,2]`

---

#### Problem 5: LeetCode 875 - Koko Eating Bananas ⭐⭐
**Difficulty:** Medium | **Time:** 35 mins

```
Koko eats piles of bananas. Each hour she chooses one pile and eats 
k bananas from it. She wants to finish all piles in h hours.
Find minimum speed k to finish in time.
```

**This is "BINARY SEARCH ON ANSWER" pattern - very important!**

**Approach:**
1. Binary search on the answer (speed k)
2. For each speed, check if she can finish in time
3. Find the minimum speed that works

**Example:** `piles=[1,1,1,1]`, hours=4 → 1
- Speed 1: finish in 4 hours ✓
- We can't go slower, so answer is 1

**Hint:**
```python
def minEatingSpeed(piles, h):
    def can_finish(speed):
        total = sum((pile + speed - 1) // speed for pile in piles)
        return total <= h
    
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if can_finish(mid):
            right = mid  # This speed works, try slower
        else:
            left = mid + 1  # Too slow, need faster
    return left
```

**After solving:** This is the KEY insight for binary search on answer! You're not searching an array, you're searching for the answer itself!

---

#### Problem 6: LeetCode 1011 - Capacity to Ship Packages ⭐⭐
**Difficulty:** Medium | **Time:** 35 mins

```
You need to ship packages in d days. Ship must have a capacity to hold 
all packages of a day. Find minimum capacity needed.
```

**This is also "BINARY SEARCH ON ANSWER"**

**Approach:**
1. Binary search on capacity
2. For each capacity, check if you can ship all packages in d days
3. Find minimum capacity

**Example:** `weights=[1,2,3,4,5,6,7,8,9,10]`, days=5 → 15
- Capacity 15: can ship in [1,2,3,4,5] [6,7] [8] [9] [10] = 5 days ✓
- Capacity 14: cannot fit in 5 days

**Hint:**
```python
def shipWithinDays(weights, days):
    def can_ship(capacity):
        current_day = 1
        current_weight = 0
        for weight in weights:
            if current_weight + weight > capacity:
                current_day += 1
                current_weight = weight
            else:
                current_weight += weight
        return current_day <= days
    
    left = max(weights)
    right = sum(weights)
    while left < right:
        mid = (left + right) // 2
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

**After solving:** Compare this with problem 875. Both use "binary search on answer"!

---

#### Problem 7: LeetCode 1095 - Find in Mountain Array ⭐⭐⭐
**Difficulty:** Hard | **Time:** 40 mins

```
A mountain array is an array that:
- Strictly increases, then strictly decreases
Find target in mountain array in O(log n)
```

**Approach:**
1. Find the peak (binary search)
2. Binary search in left half
3. If not found, binary search in right half

**This combines multiple binary search calls!**

**Hint:**
```python
def findInMountainArray(target, arr):
    # Find peak
    def find_peak():
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
    
    # Binary search on left (increasing)
    def search_left(left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    # Binary search on right (decreasing)
    def search_right(left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    peak = find_peak()
    result = search_left(0, peak, target)
    if result != -1:
        return result
    return search_right(peak + 1, len(arr) - 1, target)
```

**After solving:** This problem combines concepts! Did you understand each part?

---

### Evening: Review (30 mins)

- Which patterns did you use most?
- Which problem was hardest?
- Do you understand "binary search on answer" concept?
- Could you solve each problem again from scratch?

---

## ✅ DAY 3: ADVANCED & MOCK INTERVIEW

### Morning: Binary Search on Answer Deep Dive (1 hour)

**Read:** `binary_search_guide.md` Part 4 & 5

**Key Insight:** Binary search isn't just for arrays!
- You can binary search on ANY monotonic property
- If you can check "is this condition true/false", you can binary search

**Pattern:**
```python
def binary_search_on_answer(target_condition):
    # Define range of possible answers
    left = min_possible_answer
    right = max_possible_answer
    
    while left < right:
        mid = (left + right) // 2
        
        if satisfies_condition(mid):
            right = mid  # This works, try smaller
        else:
            left = mid + 1  # Doesn't work, need larger
    
    return left  # or right, they're equal now
```

**Practice writing a helper function:**
- First: define what you're checking
- Second: implement the check
- Third: binary search on it

---

### Afternoon: Solve More Problems & Mock Interview (2 hours)

**Solve these additional problems:**

1. **LeetCode 1157 - Online Majority Element in Subarray** ⭐⭐⭐
   - More complex binary search
   - Combines binary search with other techniques

2. **LeetCode 410 - Split Array Largest Sum** ⭐⭐⭐
   - Another "binary search on answer"
   - Find minimum largest sum when splitting array

3. **LeetCode 1231 - Divide Chocolate** ⭐⭐⭐
   - Binary search for sweetness threshold

**Then do a Mock Interview (1 hour):**

**Problem:** LeetCode 875 or 1011 (pick one)

**Steps:**
1. Read problem carefully (5 mins)
2. Identify the pattern (5 mins)
   - "Is this basic binary search?"
   - "Is this find first/last?"
   - "Is this binary search on answer?"
3. Implement solution (10 mins)
4. Trace through example (5 mins)
5. Test edge cases (5 mins)
6. Explain out loud (10 mins)
   - "What pattern did I use?"
   - "Why is it O(log n)?"
   - "What are the edge cases?"
   - "Could I optimize further?"

---

## 📋 CHEAT SHEET - QUICK REFERENCE

### Template 1: Basic Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Template 2: Find First/Last
```python
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Search left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```

### Template 3: Find Boundary
```python
def find_boundary(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

### Template 4: Binary Search on Answer
```python
def binary_search_answer(min_val, max_val, check_func):
    left, right = min_val, max_val
    while left < right:
        mid = (left + right) // 2
        if check_func(mid):
            right = mid  # Works, try smaller
        else:
            left = mid + 1  # Doesn't work, try larger
    return left
```

---

## DECISION TREE FOR INTERVIEWS

When you see a problem, ask yourself:

```
Is the data SORTED?
├─ YES → Do you need to FIND something?
│        ├─ Find exact value → Basic binary search
│        ├─ Find first/last → find_first/find_last
│        └─ Find insertion point → find_boundary
│
├─ Is it ROTATED or MODIFIED?
│  └─ Use rotated array pattern
│
└─ Can you CHECK A CONDITION for different values?
   └─ Binary search on answer!
```

---

## CONFIDENCE CHECKLIST

Before the interview, you should be able to:
- [ ] Implement basic binary search in < 2 mins
- [ ] Implement find_first in < 2 mins
- [ ] Implement find_last in < 2 mins
- [ ] Implement find_boundary in < 2 mins
- [ ] Understand binary search on answer
- [ ] Identify which pattern to use
- [ ] Trace an example by hand
- [ ] Explain time/space complexity
- [ ] Handle all edge cases
- [ ] Know when binary search works (must be sorted)

---

## KEY INSIGHTS TO REMEMBER

1. **Binary search requires sorted data** (except when searching on answer)
2. **Three loop types:**
   - `while left <= right` for exact search
   - `while left < right` for boundary search
3. **Time is O(log n)** because you eliminate half each time
4. **The power move:** Binary search on the answer (not the array!)
5. **Always test edge cases:** empty, single element, not found, etc.

---

## FINAL TIPS FOR INTERVIEW

1. **If you forget a pattern:**
   - Use basic binary search template
   - Most interviewers accept any O(log n) solution

2. **Always explain:**
   - What pattern you're using
   - Why it's O(log n)
   - Handle edge cases

3. **Binary search on answer is impressive:**
   - Shows deep understanding
   - Not everyone knows this pattern
   - Use it when you can!

4. **Test your code:**
   - Always trace through example
   - Always test edge cases
   - Ask: "What if target not found?"

Good luck! You've got this! 🎯