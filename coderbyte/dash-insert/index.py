def findEvenNumber(num):
    while num >= 1:
        if num == 1:
            return True
        num = num / 2
    
    return False
        


def dashInsert(strArr):
    stack = []
    result = []
    for n in strArr:
        if findEvenNumber(int(n)):
            result.append(n)
            stack.append(n)
        elif not findEvenNumber(int(n)):
            top = stack.pop() if stack else None
            if top and not findEvenNumber(int(top)):
                result.append('-')
            result.append(n)
            stack.append(n)
    return ''.join(result)
        
print(dashInsert('454793'))
        
    