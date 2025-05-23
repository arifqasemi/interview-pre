def numberAddition(strArr):
    result = 0
    for i in range(len(strArr)):
        if strArr[i].isalpha():
            strArr = strArr.replace(strArr[i],' ')
    strArr = strArr.split(' ')
    for k in strArr:
        if k.isdigit():
            result +=int(k)
    return result

    
            
print(numberAddition('88Hello 3World!'))