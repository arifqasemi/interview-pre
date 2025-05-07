strArr = ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]


def splitWord(s):
    first_element = s[0]
    second_element = s[1]
    
    for i in range(len(first_element)):
        first_word = first_element[:i]
        second_word = first_element[i:]
        
        if second_word in second_element and first_word in second_element:
            print(first_word,second_word)
        
        
        
        
splitWord(strArr)