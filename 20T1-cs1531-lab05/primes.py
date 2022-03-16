import math
def factors(num):
	factor = []
	while num % 2 == 0: 
		factor.append(num) 
		num = num / 2
	for i in range(3,int(math.sqrt(num))+1,2): 
		while num % i== 0: 
			factor.append(i)
			num = num / i 
	if num > 2: 
		factor.append(num)

	return factor