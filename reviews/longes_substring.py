def longest_unique_substring(s):
    start = max_len = 0
    used = {}
    for i, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_len = max(max_len, i - start + 1)
        used[char] = i
    return used

print(longest_unique_substring("pwwkew")) 
