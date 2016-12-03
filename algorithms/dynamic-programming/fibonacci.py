def fibonacci(n):
	""" Time complexity: O(N) """

	table = [0, 1] + [0] * (n-1)
	for i in xrange(2, n+1):
		table[i] = table[i-1] + table[i-2]
	return table[n] 

def optimized_fibonacci(n):
	""" Time complexity: O(logN) """

	matrix = [[1,1],[1,0]]
	if n == 0:
		return
	power(matrix, n-1)
	return matrix[0][0]

def power(matrix, n):
	if n == 0 or n == 1:
		return    
	power(matrix, n/2)
	multiply_2x2(matrix, matrix)
	if n % 2 != 0:
		initial_matrix = [[1,1],[1,0]]
		multiply_2x2(matrix,initial_matrix)

def multiply_2x2(A, B):
	""" Multiply two 2x2 matrices"""

	w = A[0][0] * B[0][0] + A[0][1] * B[1][0]
	x = A[0][0] * B[0][1] + A[0][1] * B[1][1]
	y = A[1][0] * B[0][0] + A[1][1] * B[1][0]
	z = A[1][0] * B[0][1] + A[1][1] * B[1][1]

	A[0][0] = w
	A[0][1] = x
	A[1][0] = y
	A[1][1] = z

if __name__ == '__main__':
	print fibonacci(4)
	print optimized_fibonacci(10000000000)