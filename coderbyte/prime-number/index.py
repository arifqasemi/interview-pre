def PrimeTime(num): 
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
print(PrimeTime(8))
        
        

