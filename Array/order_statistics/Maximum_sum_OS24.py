# Maximum sum such that no two elements are adjacent
# excl = max(incl, excl)
# incl = (excl + arr[i])
# o(n)

def maxsum(arr, l):
	incl = 0
	excl = 0

	for i in range(l):
		excl = max(incl, excl)
		incl = excl + arr[i]
		# print(incl, excl)

	return excl


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end=" ")
	print()


if __name__ == '__main__':
	arr = [5, 5, 10, 40, 50, 35]
	n = len(arr)
	print("Given array : ", end = '')
	printarray(arr, n)
	maxsum = maxsum(arr, n)
	print("Maximum sum such that no two elements are adjacent : ", maxsum)
