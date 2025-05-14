def StringZigZag(strArr, num):
    rowsNum = [''] * num
    current_row = 0
    going_down = False  # start going down

    for n in strArr:
        rowsNum[current_row] +=n
        if going_down:
            if current_row !=0:
                current_row -=1
            if current_row == 0:
                current_row = 0
                going_down =False
            
        else:
            if current_row != num -1:
                current_row +=1
            elif current_row == num -1:
                going_down = True
                current_row -=1
    return ''.join(rowsNum)

print(StringZigZag('coderbyte', 3))
