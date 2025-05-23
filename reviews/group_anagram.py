from collections import defaultdict
##### Example 1:

###########Input: strs = ["eat","tea","tan","ate","nat","bat"]

##########Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagram =defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram[sorted_word].append(word)
    return list(anagram.values())
    


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))