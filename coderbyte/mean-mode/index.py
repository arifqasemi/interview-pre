def meanMode(strArr):
    average = sum(strArr) // len(strArr)
    repeated_num = 0
    single_num = []
    for i in strArr:
        if i in single_num and i == average:
            return True
        else:
            single_num.append(i)
    return False
    
    
print(meanMode([5, 3, 3, 3, 1]))