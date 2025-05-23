import string
def MultipleBracket(strArr):
    mapping = {")":"(","]":"["}
    stack = []
    for i in strArr:
        if i in mapping:
            top = stack.pop() if stack else '#'
            if mapping[i] !=top:
                return False
        else:
            stack.append(i)
    return True
            
print(MultipleBracket('([()])'))