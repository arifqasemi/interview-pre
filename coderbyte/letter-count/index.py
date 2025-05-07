def LetterCountI(str): 
  for word in str.split():
    print(word)
    for i in range(len(word)):
      if word[i] in word[i+1:]:
        print(word[i])
        return word
  return -1  
    
# keep this function call here  
# to see how to enter arguments in Python scroll down

print(LetterCountI('today is the greatest day ever'))