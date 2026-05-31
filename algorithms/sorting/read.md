### “sort”, “order”, “rank”, “merge”, or “rearrange by value” → think sorting algorithms.



# SORTTING ALGORITHMS - PRACTICE CODE
# Run this file daily to practice implementations

import time
import random

# ============================================================================
# MERGE SORT - Implement from scratch
# ============================================================================

def merge_sort(arr):
    """
    Implement this without looking at code first!
    
    Steps:
    1. If array length <= 1, return it (base case)
    2. Find middle index
    3. Recursively sort left half
    4. Recursively sort right half
    5. Merge the two sorted halves
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted arrays
    
    Key insight: Use two pointers, compare elements
    """
    result = []
    i = j = 0
    
    # Compare and add smaller element
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


# ============================================================================
# QUICK SORT - Implement from scratch
# ============================================================================

def quick_sort(arr, low=0, high=None):
    """
    Implement this without looking at code first!
    
    Steps:
    1. If high is None, set it to len(arr) - 1
    2. If low < high:
       a. Call partition to get pivot index
       b. Recursively sort left side (low to pivot-1)
       c. Recursively sort right side (pivot+1 to high)
    3. Return arr
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    Partition array around pivot
    
    Key insight: 
    - Choose pivot (we use last element)
    - Move all smaller elements to left
    - Move pivot to correct position
    - Return pivot's final position
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ============================================================================
# HEAP SORT - Implement from scratch
# ============================================================================

def heap_sort(arr):
    """
    Implement this without looking at code first!
    
    Steps:
    1. Build max heap (bottom-up from n//2-1 to 0)
    2. For each element from end to 1:
       a. Swap arr[0] with arr[i]
       b. Heapify from index 0 with reduced size
    3. Return arr
    """
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr


def heapify(arr, n, i):
    """
    Maintain max heap property
    
    Key insight:
    - Find largest among i, left child (2*i+1), right child (2*i+2)
    - If largest is not i, swap and recursively heapify
    """
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


# ============================================================================
# TEST CASES
# ============================================================================

def run_tests():
    """Test all three sorting algorithms"""
    
    print("=" * 70)
    print("SORTING ALGORITHMS TEST SUITE")
    print("=" * 70)
    
    # Test cases
    test_cases = [
        ("Empty", []),
        ("Single element", [1]),
        ("Two elements", [2, 1]),
        ("Already sorted", [1, 2, 3, 4, 5]),
        ("Reverse sorted", [5, 4, 3, 2, 1]),
        ("With duplicates", [3, 1, 4, 1, 5, 9, 2, 6, 5]),
        ("All same", [1, 1, 1, 1]),
        ("Random", [5, 2, 8, 1, 9, 3, 7, 4, 6]),
        ("Large", list(range(100, 0, -1))),
    ]
    
    algorithms = {
        "Merge Sort": merge_sort,
        "Quick Sort": lambda arr: quick_sort(arr.copy()),
        "Heap Sort": heap_sort,
    }
    
    for algo_name, algo_func in algorithms.items():
        print(f"\n{'='*70}")
        print(f"{algo_name}")
        print(f"{'='*70}")
        
        for test_name, test_arr in test_cases:
            arr_copy = test_arr.copy()
            result = algo_func(arr_copy)
            expected = sorted(test_arr)
            
            status = "✓ PASS" if result == expected else "✗ FAIL"
            print(f"{status} | {test_name:20} | {result}")
            
            if result != expected:
                print(f"       Expected: {expected}")


def trace_example():
    """
    Trace through examples step-by-step
    This helps you understand the algorithms
    """
    print("\n" + "=" * 70)
    print("STEP-BY-STEP TRACE EXAMPLE")
    print("=" * 70)
    
    arr = [5, 2, 8, 1, 9]
    
    print(f"\nOriginal array: {arr}")
    
    print("\n--- MERGE SORT TRACE ---")
    print("Step 1: Divide")
    print("  [5, 2, 8, 1, 9]")
    print("     /          \\")
    print("  [5, 2]      [8, 1, 9]")
    print("   / \\          / \\")
    print(" [5] [2]    [8] [1, 9]")
    print("              / \\")
    print("            [1] [9]")
    
    print("\nStep 2: Merge")
    print("  [5] [2] → [2, 5]")
    print("  [1] [9] → [1, 9]")
    print("  [8] → [8]")
    print("  [2, 5] + [8] → [2, 5, 8]")
    print("  [2, 5, 8] + [1, 9] → [1, 2, 5, 8, 9]")
    
    result = merge_sort(arr.copy())
    print(f"\nResult: {result}")
    
    print("\n--- QUICK SORT TRACE ---")
    print(f"Original array: {arr}")
    print("Choose pivot = 9 (last element)")
    print("Partition: [5, 2, 8, 1] | 9 | []")
    print("Continue partitioning left side with pivot = 1")
    print("And so on...")
    
    result = quick_sort(arr.copy())
    print(f"Result: {result}")


def performance_test():
    """
    Test performance on larger arrays
    This shows why O(n log n) matters!
    """
    print("\n" + "=" * 70)
    print("PERFORMANCE TEST")
    print("=" * 70)
    
    sizes = [100, 1000, 5000]
    
    for size in sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        
        print(f"\nArray size: {size}")
        
        # Test merge sort
        start = time.time()
        merge_sort(arr.copy())
        merge_time = time.time() - start
        print(f"  Merge Sort: {merge_time:.6f} seconds")
        
        # Test quick sort
        start = time.time()
        quick_sort(arr.copy())
        quick_time = time.time() - start
        print(f"  Quick Sort: {quick_time:.6f} seconds")
        
        # Test heap sort
        start = time.time()
        heap_sort(arr.copy())
        heap_time = time.time() - start
        print(f"  Heap Sort:  {heap_time:.6f} seconds")


# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

def practice_merge():
    """
    Exercise 1: Implement merge_sort from scratch (no peeking!)
    
    Try this:
    1. Close this file
    2. Open a new file
    3. Implement merge_sort from memory
    4. Test it with: [5, 2, 8, 1, 9]
    5. Compare with this file
    """
    print("\nEXERCISE 1: Implement Merge Sort")
    print("-" * 70)
    print("Instructions:")
    print("1. Create a new Python file")
    print("2. Implement merge_sort from scratch (don't copy!)")
    print("3. Test with: [5, 2, 8, 1, 9]")
    print("4. Expected: [1, 2, 5, 8, 9]")


def practice_quick():
    """
    Exercise 2: Implement quick_sort from scratch
    """
    print("\nEXERCISE 2: Implement Quick Sort")
    print("-" * 70)
    print("Instructions:")
    print("1. Create a new Python file")
    print("2. Implement quick_sort and partition from scratch")
    print("3. Test with: [5, 2, 8, 1, 9]")
    print("4. Expected: [1, 2, 5, 8, 9]")
    print("\nKey: partition() function is critical!")


def practice_heap():
    """
    Exercise 3: Implement heap_sort from scratch
    """
    print("\nEXERCISE 3: Implement Heap Sort")
    print("-" * 70)
    print("Instructions:")
    print("1. Create a new Python file")
    print("2. Implement heap_sort and heapify from scratch")
    print("3. Test with: [5, 2, 8, 1, 9]")
    print("4. Expected: [1, 2, 5, 8, 9]")
    print("\nKey: heapify() function is critical!")


# ============================================================================
# COMPARISON QUESTIONS
# ============================================================================

def comparison_questions():
    """
    Questions to test your understanding
    Write answers in a notebook
    """
    questions = [
        "Q1: What's the time complexity of merge sort and why?",
        "Q2: What's the time complexity of quick sort (average and worst)?",
        "Q3: Why does merge sort need O(n) extra space?",
        "Q4: Why is quick sort faster than merge sort on average?",
        "Q5: When would you use heap sort over quick sort?",
        "Q6: Is merge sort stable? Why?",
        "Q7: Is quick sort stable? Why?",
        "Q8: What happens if you always pick smallest element as pivot in quick sort?",
        "Q9: Can you implement quick sort in-place? How?",
        "Q10: Why is heap sort O(n log n) guaranteed?",
    ]
    
    print("\nCOMPARISON QUESTIONS - Answer these!")
    print("-" * 70)
    for q in questions:
        print(q)


# ============================================================================
# MAIN - RUN ALL TESTS
# ============================================================================

if __name__ == "__main__":
    
    # Run tests
    run_tests()
    
    # Trace example
    trace_example()
    
    # Performance comparison
    performance_test()
    
    # Exercises
    practice_merge()
    practice_quick()
    practice_heap()
    
    # Questions
    comparison_questions()
    
    print("\n" + "=" * 70)
    print("PRACTICE PLAN")
    print("=" * 70)
    print("""
DAY 1-2: MERGE SORT
- Run this file to see merge sort work
- Implement merge_sort 3 times from scratch
- Trace through examples by hand
- Answer comparison questions 1, 2, 6

DAY 3: QUICK SORT
- Implement quick_sort 3 times from scratch
- Focus on partition() function
- Trace through examples by hand
- Answer comparison questions 3, 4, 8, 9

DAY 4: HEAP SORT + PRACTICE
- Implement heap_sort from scratch
- Understand heapify() function
- Solve 5 LeetCode problems with each algorithm
- Answer ALL comparison questions

DAY 5: REVIEW + MOCK
- Implement all 3 from scratch without peeking
- Solve mixed problems and choose algorithm
- Explain trade-offs out loud
- Time yourself: < 15 mins per algorithm

YOU GOT THIS! 💪
    """)