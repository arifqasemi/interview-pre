def VowelSquare(strArr):
    l = list([[x for x in s] for s in strArr])
    row = len(strArr)
    col = len(strArr[0])
    for i in range(0,row-1):
        for j in range(0, col-1):
            if l[i][j] in 'aeiou' and l[i][j+1] in 'aeiou' and l[i+1][j] in 'aeiou' and l[i+1][j+1] in 'aeiou':
                return str(i) + '-' + str(j)
    return 'not found'
    
# keep this function call here  
