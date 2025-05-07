def LetterChanges(sen):
    newWord = ''
    newChar = 0
    for i in range(len(sen)):
        if sen[i] == chr(32):
            newWord += sen[i]
        elif sen[i].isalnum() and not sen[i].isdigit():
            newChar = ord(sen[i])
            print(newChar)
            newChar += 1
            newWord += chr(newChar)
            print(newWord)
        else:
            newWord += sen[i]
    return newWord

print(LetterChanges('hello'))