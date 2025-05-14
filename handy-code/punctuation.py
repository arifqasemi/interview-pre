import string

def checkPunctuation(strArr):
    
    punc = False
    num = False
    cap = False
    
    for p in strArr:
        if p in string.punctuation: ############## you can check punctuation like this
            punc = True
        if p.isupper():
            cap = True
        if p.isdigit():
            num = True
            
    return punc==num==cap
            
            
print(checkPunctuation('fsA1@'))