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
    
    for m,(k,j) in enumerate(parsed_string):  ############  looping through tuple inside list of tuples
        for d in range(m+1,len(parsed_string)): ##############  compare with next tuple
            x,y = parsed_string[d]
            if k - x == j -y:
                return parsed_string[m]
    return True
    

   

# Test cases
# print(EightQueens(["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(5,8)"]))  # Output: True
print(EightQueens(["(2,1)", "(4,3)", "(6,3)", "(8,4)", "(3,4)", "(1,6)", "(7,7)", "(5,8)"]))  # Output: "(4,3)"
# print(EightQueens(["(2,1)", "(5,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(4,8)"]))  # Output: "(5,2)"