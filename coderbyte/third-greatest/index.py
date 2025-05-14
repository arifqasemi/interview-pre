def thirdGreatest(strArr):
    strArr = sorted(strArr,key=len)
    return strArr[2]
    
    
print(thirdGreatest(["hello", "world", "before", "all"]))