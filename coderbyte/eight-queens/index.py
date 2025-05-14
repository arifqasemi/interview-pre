
###############  Have the function EightQueens(strArr) read strArr which will be an array consisting of the locations of eight Queens on a standard 8x8 chess board with no other pieces on the board. The structure of strArr will be the following: ["(x,y)", "(x,y)", ...] where (x,y) represents the position of the current queen on the chessboard (x and y will both range from 1 to 8 where 1,1 is the bottom-left of the chessboard and 8,8 is the top-right). Your program should determine if all of the queens are placed in such a way where none of them are attacking each other. If this is true for the given input, return the string true otherwise return the first queen in the list that is attacking another piece in the same format it was provided. 

###############  For example: if strArr is ["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(5,8)"] then your program should return the string true. The corresponding chessboard of queens for this input is below (taken from Wikipedia). 

#############![](https://i.imgur.com/zAT24ML.png)
 
#############Sample Test Cases:

############Input:["(2,1)", "(4,3)", "(6,3)", "(8,4)", "(3,4)", "(1,6)", "(7,7)", "(5,8)"]

#############Output:"(2,1)"


###################Input:["(2,1)", "(5,3)", "(6,3)", "(8,4)", "(3,4)", "(1,8)", "(7,7)", "(5,8)"]

######################Output:"(5,3)"

def EightQueens(strArr):
    # Step 1: Parse the input
    parsed_string =[eval(n) for n in strArr]
    columns = []
    rows = []
    for i,n in parsed_string:
        if i in columns:
            return [num for num in parsed_string if num[0] ==n][0]
        elif n in rows:
            return [num for num in parsed_string if num[1] ==n][0]
        columns.append(i)
        rows.append(n)
    
    for m,(k,j) in enumerate(parsed_string):
        for d in range(m+1,len(parsed_string)):
            x,y = parsed_string[d]
            if k - x == j -y:
                return parsed_string[m]
    return True
    

   

# Test cases
# print(EightQueens(["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(5,8)"]))  # Output: True
print(EightQueens(["(2,1)", "(4,3)", "(6,3)", "(8,4)", "(3,4)", "(1,6)", "(7,7)", "(5,8)"]))  # Output: "(4,3)"
# print(EightQueens(["(2,1)", "(5,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(4,8)"]))  # Output: "(5,2)"