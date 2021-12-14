# Given an array of size n where all elements are distinct and in range from 0 to n-1,
# change contents of arr[] so that arr[i] = j is changed to arr[j] = i.

def rearrange(arr, l):
	num = [0] * l
	for i in range(l):
		num[arr[i]] = i

	for i in range(l):
		arr[i] = num[i]


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [1, 3, 0, 2]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	rearrange(arr, l)
	print("Array after rearrangement : ", end = "")
	printarray(arr, l)
