def PowersofTwo(num):

  # code goes here
  return num > 0 and (num & (num - 1)) == 0
    


# keep this function call here 
print(PowersofTwo(input()))