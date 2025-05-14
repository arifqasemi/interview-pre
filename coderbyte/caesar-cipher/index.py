def CaesarCiphir(strArr,num):
    def nextChar(char):
        char_order = ord(char)
        next_char =chr(char_order +num)
        return next_char
    strArr = strArr.split()
    result = []
    
    for i in strArr:
        new_list = []
        for k in i:
            new_list.append(nextChar(k.lower()))
        result.append(''.join(new_list))
    return ' '.join(result)
        
            
        

print(CaesarCiphir('Caesar Cipher',2))