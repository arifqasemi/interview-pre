def numberAddition(strArr):
    for n in range(len(strArr)):
        if strArr[n].isalpha():
            strArr =strArr.replace(strArr[n],' ')
    list1 = strArr.split(' ')
    new_list = []
    for k in list1:
        if k.isdigit():
            new_list.append(int(k))
    return sum(new_list)
    
            
print(numberAddition('88Hello 3World!'))