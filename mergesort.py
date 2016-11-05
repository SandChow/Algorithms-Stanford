def mergesort(arr):
	if len(arr) < 2:
		return arr
	first_half, second_half = mergesort(arr[:len(arr)/2]), mergesort(arr[len(arr)/2:])
	return merge(first_half, second_half)

def merge(x, y):
	if len(x)*len(y) is 0:
		return x + y
	return [(x if x[0] < y[0] else y).pop(0)] + merge(x, y)

if __name__=="__main__":
	arr = [5,3,1,2,4,6,0, -1, -200000]
	print mergesort(arr)