from collections import Counter
def CorrectPath(str):
    counter = Counter(str)
    print(counter)

# Test cases
print(CorrectPath("???rrurdr?"))  # Output: "dddrrurdrd"
# print(CorrectPath("drdr??rrddd?"))  # Output: "drdruurrdddd"
# print(CorrectPath("r?d?drdd"))  # Output: "rrdrdrdd"