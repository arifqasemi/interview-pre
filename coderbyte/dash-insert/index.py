def findOddNumer(num):
    if num % 2 !=0:
        return True

    return False
        


def dashInsert(nums):
    stack = [nums[0]]
    for i in nums:
        if findOddNumer(int(stack[-1])):
            stack.append('-')
            stack.append(i)
        else:
            stack.append(i)
    print(stack)

        
# print(findOddNumer(8))
print(dashInsert('454793'))
        
    