#Still Buggy

def count(arr):
	if len(arr) < 2:
		return arr, 0
	left_half, left_count = count(arr[:len(arr)/2]) 
	right_half, right_count = count(arr[len(arr)/2:])
	sorted_array, split_count = merge_and_count(left_half, right_half)
	return sorted_array, left_count + right_count + split_count

def merge_and_count(x, y):
	count = 0
	sorted_array = []
	while len(x)*len(y) is not 0:
		if x[0] < y[0]:
			sorted_array.append(x.pop(0))
		else:
			print x[0]
			j = y.pop(0)
			print j
			sorted_array.append(j)
			count += 1
	if len(y) is 0:
		sorted_array += x
	else:
		sorted_array += y
	return sorted_array, count

if __name__=="__main__":
	arr = [1,3,5,2,4,6]
	print "total -> ",
	print count(arr)[1]