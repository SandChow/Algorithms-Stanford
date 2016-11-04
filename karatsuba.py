def karatsuba(num1, num2):
	if num2 < 10 or num1 < 10:
		return num1 * num2

	# calculates the size of the numbers
	m = max(len(str(num1)), len(str(num2)))
	m2 = m / 2

	# split the digit sequences about the middle
	high1, low1 = num1 / 10**(m2), num1 % 10**(m2)
	high2, low2 = num2 / 10**(m2), num2 % 10**(m2)

	# debug
	print "num1 -> ",; print high1, low1 
	print "num2 -> ",; print high2, low2
	print

	# 3 calls made to numbers approximately half the size
	z0 = karatsuba(low1, low2)
	z1 = karatsuba(low1+high1, low2+high2)
	z2 = karatsuba(high1, high2)
	return z2 * 10**(2*m2) + (z1-z2-z0) * 10**m2 + z0

if __name__=="__main__":
	print karatsuba(2400000, 52)