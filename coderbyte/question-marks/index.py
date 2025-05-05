def QuestionsMarks(strParam):
    numbers = '1234567890'
    lastDigit = None
    answer = 'false'
    for i in range(0, len(strParam)):
        if strParam[i].isdigit():
            if lastDigit:
                if int(strParam[i]) + int(strParam[lastDigit]) == 10:
                    if strParam[lastDigit:i].count('?') == 3:
                        answer = 'true'
                    else:
                        return 'false'
            lastDigit = i
    
    return answer
# keep this function call here 
print(QuestionsMarks(input()))