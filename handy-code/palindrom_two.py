####Using the JavaScript language, have the function PalindromeTwo(str)
####take the str parameter being passed and return the string true if the parameter is a palindrome, 
####(the string is the same forward as it is backward) otherwise return the string false. 
####The parameter entered may have punctuation and symbols but they should not affect whether the string is in fact a palindrome.
####For example: "Anne, I vote more cars race Rome-to-Vienna" should return true. */

def PalindromeTwo(strArr):
    splited_arr = []
    for i in strArr:
        if i.isalpha():
            splited_arr.append(i.lower())
    if splited_arr == splited_arr[::-1]:
        return True
    return False
            
            

print(PalindromeTwo('Anne, I vote more cars race Rome-to-Vienna'))############### converting to list and then converting