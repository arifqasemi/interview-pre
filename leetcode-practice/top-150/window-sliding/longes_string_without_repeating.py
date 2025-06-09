## Example 1:
## 
## Input: s = "abcabcbb"
## Output: 3
## Explanation: The answer is "abc", with the length of 3.
## Example 2:
## 
## Input: s = "bbbbb"
## Output: 1
## Explanation: The answer is "b", with the length of 1.
## Example 3:
## 
## Input: s = "pwwkew"
## Output: 3
## Explanation: The answer is "wke", with the length of 3.
## Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0

        result = set()

        for i in range(len(s)):
            while s[i] in result:
                result.remove(s[left])
                left +=1
            result.add(s[i])
            max_len = max(max_len, i - left +1)
            print(max_len)
        return max_len