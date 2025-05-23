def OffLineMinimum(strArr):
    stack = []
    result = []
    for i in strArr:
        if i =="E":
            min_num = min(stack)
            result.append(min_num)
            stack.remove(min_num)
        else:
            stack.append(int(i))
    return result
    
print(OffLineMinimum(["5","4","6","E","1","7","E","E","3","2"]))