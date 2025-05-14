def BinaryConverter(str_num):
    num = int(str_num)            # Convert string to integer
    binary = bin(num)[2:]         # Convert to binary and remove the '0b' prefix
    return binary

# Example:
print(BinaryConverter("213"))     # Output: "11010101"
