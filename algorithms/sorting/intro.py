# SORTING ALGORITHMS GUIDE - Python
# Intermediate Level | Understand how each algorithm works

# ============================================================================
# 1. BUBBLE SORT - Simple but Inefficient
# ============================================================================
# How it works: Repeatedly steps through the list, compares adjacent elements,
# and swaps them if they're in the wrong order. Like bubbles rising to the top.

def bubble_sort(arr):
    """
    Time: O(n²) average and worst case
    Space: O(1)
    Stable: Yes
    Best for: Educational purposes, nearly sorted small arrays
    """
    n = len(arr)
    for i in range(n):
        # Flag to optimize: if no swaps occur, array is sorted
        swapped = False
        for j in range(0, n - i - 1):
            print(arr[j],arr[j+1])
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example: [5, 2, 8, 1, 9]
# Pass 1: [2, 5, 1, 8, 9] - largest (9) bubbles to end
# Pass 2: [2, 1, 5, 8, 9] - second largest (8) in place
# Pass 3: [1, 2, 5, 8, 9] - done
bubble_sort([5, 2, 8, 1, 9])


# ============================================================================
# 2. SELECTION SORT - Find minimum repeatedly
# ============================================================================
# How it works: Divides array into sorted and unsorted regions. Repeatedly
# finds the minimum in the unsorted region and moves it to the sorted region.

def selection_sort(arr):
    """
    Time: O(n²) all cases (no early exit optimization)
    Space: O(1)
    Stable: No (can reverse order of equal elements)
    Best for: When memory write is costly (writes are minimized)
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example: [5, 2, 8, 1, 9]
# Find min in [5,2,8,1,9] → 1, swap with 5: [1, 2, 8, 5, 9]
# Find min in [2,8,5,9] → 2, already at position: [1, 2, 8, 5, 9]
# Find min in [8,5,9] → 5, swap with 8: [1, 2, 5, 8, 9]


# ============================================================================
# 3. INSERTION SORT - Build sorted array one item at a time
# ============================================================================
# How it works: Iterates through array, and for each element, inserts it into
# the correct position in the already-sorted left portion.

def insertion_sort(arr):
    """
    Time: O(n²) average/worst, O(n) best (already sorted)
    Space: O(1)
    Stable: Yes
    Best for: Small arrays, nearly sorted data, online sorting
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift all elements greater than key one position right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert key at correct position
        arr[j + 1] = key
    return arr

# Example: [5, 2, 8, 1, 9]
# [5] | [2, 8, 1, 9] → insert 2: [2, 5] | [8, 1, 9]
# [2, 5] | [8, 1, 9] → insert 8: [2, 5, 8] | [1, 9]
# [2, 5, 8] | [1, 9] → insert 1: [1, 2, 5, 8] | [9]
# [1, 2, 5, 8] | [9] → insert 9: [1, 2, 5, 8, 9]


# ============================================================================
# 4. MERGE SORT - Divide and conquer
# ============================================================================
# How it works: Recursively divide array in half until you have single elements.
# Then merge sorted subarrays back together.

def merge_sort(arr):
    """
    Time: O(n log n) all cases (guaranteed)
    Space: O(n) for temporary arrays
    Stable: Yes
    Best for: Guaranteed performance, linked lists, large datasets
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer (merge)
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    # Compare elements from left and right, add smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example: [5, 2, 8, 1, 9]
# Divide: [5, 2] | [8] | [1, 9]
# Further: [5] | [2] | [8] | [1] | [9]
# Merge: [2, 5] | [8] | [1, 9]
# Merge: [2, 5, 8] | [1, 9]
# Final: [1, 2, 5, 8, 9]


# ============================================================================
# 5. QUICK SORT - Divide and conquer with in-place partitioning
# ============================================================================
# How it works: Pick a pivot, partition array so elements < pivot are left
# and elements > pivot are right. Recursively sort both sides.

def quick_sort(arr):
    """
    Time: O(n log n) average, O(n²) worst case (bad pivot selection)
    Space: O(log n) average due to recursion stack
    Stable: No (basic implementation)
    Best for: Average case performance, in-place sorting, general purpose
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# In-place version (more efficient):
def quick_sort_inplace(arr, low=0, high=None):
    """In-place quick sort - more memory efficient"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)
    
    return arr

def partition(arr, low, high):
    """Partition around pivot"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example: [5, 2, 8, 1, 9]
# Pivot: 8
# Left: [5, 2, 1] | Middle: [8] | Right: [9]
# Left needs sorting: [1, 2, 5]
# Result: [1, 2, 5, 8, 9]


# ============================================================================
# 6. HEAP SORT - Using heap data structure
# ============================================================================
# How it works: Build a max heap, then repeatedly remove the root (largest)
# and place it at the end.

def heap_sort(arr):
    """
    Time: O(n log n) all cases
    Space: O(1)
    Stable: No
    Best for: Guaranteed O(n log n) with minimal space
    """
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move root (largest) to end
        heapify(arr, i, 0)  # Heapify reduced heap
    
    return arr

def heapify(arr, n, i):
    """Maintain heap property"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Example: [5, 2, 8, 1, 9]
# Build heap: [9, 5, 8, 1, 2]
# Extract 9: [8, 5, 2, 1] → [8, 1, 2, 5]
# Extract 8: [5, 1, 2] → [5, 2, 1]
# Continue...


# ============================================================================
# 7. COUNTING SORT - For non-comparative sorting (specific scenarios)
# ============================================================================
# How it works: Count frequency of each element, then reconstruct sorted array.
# Only works for integers in a known range.

def counting_sort(arr, max_val=None):
    """
    Time: O(n + k) where k is range of input
    Space: O(k)
    Stable: Yes
    Best for: Small range of integers, when range is known
    """
    if not arr:
        return arr
    
    if max_val is None:
        max_val = max(arr)
    min_val = min(arr)
    
    range_size = max_val - min_val + 1
    count = [0] * range_size
    
    # Count frequencies
    for num in arr:
        count[num - min_val] += 1
    
    # Reconstruct array
    result = []
    for i in range(range_size):
        result.extend([i + min_val] * count[i])
    
    return result

# Example: [5, 2, 8, 1, 9]
# Count: 1→1, 2→1, 5→1, 8→1, 9→1
# Reconstruct: [1, 2, 5, 8, 9]


