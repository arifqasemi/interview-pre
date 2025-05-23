def sortVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = "aeiouAEIOU"
    s_list = list(s)
    
    # Step 1: Extract and sort vowels
    vowel_chars = sorted([c for c in s_list if c in vowels])
    print(vowel_chars)
    
    # Step 2: Replace vowels in order
    idx = 0
    for i in range(len(s_list)):
        if s_list[i] in vowels:
            s_list[i] = vowel_chars[idx]
            idx += 1

    return ''.join(s_list)
    
print(sortVowels("lEetcOde"))

        