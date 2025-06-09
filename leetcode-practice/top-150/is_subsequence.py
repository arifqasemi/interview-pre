## Example 1:
## 
## Input: s = "abc", t = "ahbgdc"
## Output: true
## Example 2:
## 
## Input: s = "axc", t = "ahbgdc"
## Output: false


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer for s

        for char in t:
            if i < len(s) and s[i] == char:
                i += 1

        return i == len(s)