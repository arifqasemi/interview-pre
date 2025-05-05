def ScaleBalancing(strArr):
    # Step 1: Parse input
    # strArr[0] = "[1, 2]" -> left=1, right=2
    # strArr[1] = "[3, 4, 5]" -> weights=[3, 4, 5]
    left, right = eval(strArr[0]) # Safely parse "[1, 2]" to (1, 2)
    weights = eval(strArr[1])      # Parse "[3, 4, 5]" to [3, 4, 5]
    print(weights)
    # Step 2: Calculate difference
    diff = abs(left - right)  # |1 - 2| = 1
    
    # Step 3: Create a set for O(1) lookups
    weight_set = set(weights)
    
    # Step 4: Check one weight
    if diff in weight_set:
        return str(diff)  # If diff (e.g., 1) is in weights, return it
    
    # Step 5: Check two weights
    for i, w1 in enumerate(weights):
        # Two weights on one side
        for w2 in weights[i+1:]:  # Avoid duplicate pairs
            if w1 + w2 == diff:
                return f"{min(w1, w2)},{max(w1, w2)}"  # Ascending order
        
        # One weight on each side
        # Need: left + w1 = right + w2 -> w1 - w2 = right - left
        target = right - left + w1 if left < right else left - right + w1
        if target in weight_set and target != w1:
            return f"{min(w1, target)},{max(w1, target)}"  # Ascending order
    
    # Step 6: No solution found
    return "not possible"

# Test the given input
print(ScaleBalancing(["[1, 2]", "[3, 4, 5]"]))  # Output: "3,4"

# Additional test cases
# print(ScaleBalancing(["[5, 9]", "[1, 2, 6, 7]"]))  # "2,6"
# print(ScaleBalancing(["[3, 4]", "[1, 2, 7, 7]"]))  # "1"
# print(ScaleBalancing(["[3, 7]", "[1, 2, 7]"]))     # "not possible"
# print(ScaleBalancing(["[13, 4]", "[1, 2, 3, 6, 14]"]))  # "3,6"
# print(ScaleBalancing(["[6, 1]", "[1, 10, 6, 5]"]))  # "5"