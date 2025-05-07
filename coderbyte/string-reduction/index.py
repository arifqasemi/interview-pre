def stringReduction(strArr):
    stack = []
    count = 0
    for n in strArr:
        if stack and stack[-1] !=n and stack[-1] =='a' and n =='c':
            stack.pop()
            stack.append('b')
            count +=1
        elif stack and stack[-1] !=n and stack[-1] =='b' and n =='c':
            stack.pop()
            stack.append('a')
            count +=1
        elif stack and stack[-1] !=n and stack[-1] =='a' and n =='b':
            stack.pop()
            stack.append('c')
            count +=1
        elif stack and stack[-1] !=n and stack[-1] =='c' and n =='a':
            stack.pop()
            stack.append('c')
            count +=1
        else:
            stack.append(n)
    return count
            
print(stringReduction('cccca'))
            