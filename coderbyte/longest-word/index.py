def LongestWord(sen):
    longest = ""
    for word in sen.split():
        if word.isalpha():
            #if re.match('^[\w-]+$', word):
            longest = word if len(word) > len(longest) else longest
    return longest