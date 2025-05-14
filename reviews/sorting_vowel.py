###  Example 1:

######### Input: s = "lEetcOde"
######### Output: "lEOtcede"
######### Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
######### 
#

class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        s_list = list(s)
        
        vowel_chars = sorted([c for c in s_list if c in vowels])
        print(vowel_chars)
        
        idx = 0
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                print(s_list[i])
                s_list[i] = vowel_chars[idx]
                idx += 1

        return ''.join(s_list)