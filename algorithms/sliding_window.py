## Strong hints:
## longest substring
## smallest subarray
## continuous
## consecutive
## at most K
## window
## range

# 1. Build initial window

# def slidingWindow(nums):
#     window_state = some_state(nums[:k])

#     answer = evaluate(window_state)

#     # 2. Slide the window

#     for right in range(k, len(nums)):

#         outgoing = nums[right - k]
#         incoming = nums[right]

#         # Remove old element
#         update_state_remove(outgoing)

#         # Add new element
#         update_state_add(incoming)

#         answer = update_answer(window_state)

#     return answer