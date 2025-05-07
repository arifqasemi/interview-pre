from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    t_count = Counter(t)  # Count characters in t
    window_count = {}
    
    have, need = 0, len(t_count)
    res, res_len = [-1, -1], float('inf')
    left = 0

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in t_count and window_count[char] == t_count[char]:
            have += 1

        while have == need:
            # Update result if this window is smaller
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            # Try to shrink the window
            window_count[s[left]] -= 1
            if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                have -= 1
            left += 1

    l, r = res
    return s[l:r+1] if res_len != float('inf') else ""
