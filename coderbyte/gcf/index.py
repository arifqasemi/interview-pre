def GCF(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
        print(num1,num2)
    return num1

# Example
print(GCF(12, 18))  # Output: 6
