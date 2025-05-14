## Question: Have the function RunLength(str) take the str parameter being passed and return a compressed version
## of the string using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each 
## repeating character and outputting that number along with a single character of the repeating sequence. For 
## example: "wwwggopp" would return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols. 


def RunLength(strArr):
    hash_map = {}
    result = []
    for i in strArr:
        if i not in hash_map:
            hash_map[i] =1
        else:
            hash_map[i] +=1
            
    for k in hash_map:
        result.append(str(hash_map[k]))
        result.append(k)
    return ''.join(result)

print(RunLength('wwwggopp'))