## Example 1:
## 
## Input: strs = ["flower","flow","flight"]
## Output: "fl"
## Example 2:
## 
## Input: strs = ["dog","racecar","car"]
## Output: ""
## Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]