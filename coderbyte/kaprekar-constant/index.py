# Using the Python language, have the function KaprekarsConstant(num) take
# the num parameter being passed which will be a 4-digit number with at least
# two distinct digits.

# Your program should perform the following routine on the number:
# Arrange the digits in descending order and in ascending order
# subtract the smaller number from the bigger number. Then repeat the previous step.

# Performing this routine will always cause you to reach a fixed number: 6174.

# For example: if num is 3524 your program should return 3 because of the following steps:
# (1) 5432 - 2345 = 3087, (2) 8730 - 0378 = 8352, (3) 8532 - 2358 = 6174. 

# Assumes number with 4 digits given

def kaprekarConstant(nums):
    
    count = 0
    while nums !=6174:
        asc = int(''.join(sorted(str(nums))))
        dsc = int(''.join(sorted(str(nums),reverse=True)))
        nums = abs(asc - dsc)
        count +=1
        
    return count
    

print(kaprekarConstant(5432))