from collections import Counter
def CorrectPath(str):
    counter = Counter(str)
    down = counter.get('d')
    up  = counter.get('u')
    row_position = down -up
    column_position = counter.get('r') - counter.get('l') if counter.get('l') else counter.get('r') 
    result = []
    splited_arr = [s for s in str]
    for i in splited_arr:
        if i =='?':
            if row_position < 4:
                result.append('d')
                row_position +=1
        else:
            result.append(i)
    return ''.join(result)
        

    



# Test cases
print(CorrectPath("???rrurdr?"))  # Output: "dddrrurdrd"
# print(CorrectPath("drdr??rrddd?"))  # Output: "drdruurrdddd"
# print(CorrectPath("r?d?drdd"))  # Output: "rrdrdrdd"