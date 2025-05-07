def PrimeTime(num): 
	i = 2 
	while i < num:
		if num%i == 0:
			return 'false'
		else:
			i += 1
	return 'true' 

print(PrimeTime(3))
