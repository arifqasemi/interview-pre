import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s =  re.sub(r'[^a-z0-9]', '', s.lower())
        reversed_s = [n for n in new_s[::-1]]
        joined_s = ''.join(reversed_s)
        if new_s == joined_s:
            return True
        else:
            return False
        
        
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if re.match(r'[a-z0]',s[i]):
                break
                
        