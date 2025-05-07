def BitwiseOne(strArr):
    bin1 = strArr[0]
    bin2 = strArr[1]
    result = ''

    for i in range(len(bin1)):
        if bin1[i] == '1' or bin2[i] == '1':
            result += '1'
        else:
            result += '0'

    return result

# Example
print(BitwiseOne(["1001", "0100"]))  # Output: 1101
