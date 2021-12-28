# Maximum and minimum of an array using minimum number of comparisons
# O(n)

def maxmin(arr, l):
	max = min = arr[0]
	for i in range(1, l):
		if arr[i] > max:
			max = arr[i]
		if arr[i] < min:
			min = arr[i]

	return max, min


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end=" ")
	print()


if __name__ == '__main__':
	arr = [1000, 11, 445, 1, 330, 3000]
	n = len(arr)
	print("Given array : ", end = '')
	printarray(arr, n)
	max, min = maxmin(arr, n)
	print("Maximum value of an array : ", max)
	print("Minimum value of an array : ", min)
