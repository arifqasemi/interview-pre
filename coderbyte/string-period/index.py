######### For this challenge you will need to find the smallest repeating substring.
##########
##############have the function StringPeriods(str) take the str parameter being passed 
# and determine if there is some substring K that can be repeated N > 1 times to produce
# the input string exactly as it appears. Your program should return the longest substring K,
# and if there is none it should return the string -1.

##########For example: if str is "abcababcababcab" then your program should return abcab
# because that is the longest substring that is repeated 3 times to create the final string.
# Another example: if str is "abababababab" then your program should return ababab because
# it is the longest substring. If the input string contains only a single character,
# your program should return the string -1.
##########


def StringPeriod(s):
    n = len(s)
   
    for i in range(1,(n // 2) +1):
        if n % i ==0:
            period_char = s[:i]
            if period_char * (n // i) == s:
                return period_char
                
            
    return s

print(StringPeriod('abcabcabc'))