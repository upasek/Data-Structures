# Given two integer arrays of same size, “arr[]” and “index[]”,
# reorder elements in “arr[]” according to given index array.
# It is not allowed to given array arr’s length.

def rearrange(arr, index, n):
	temp = [0] * n
	for i in range(n):
		temp[index[i]] = arr[i]

	for j in range(n):
		arr[j] = temp[j]
		index[j] = j

def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [50, 40, 70, 60, 90, 66, 55, 11]
	index = [3,  0,  4,  1,  2, 5, 7, 6]
	n = len(arr)
	print("Original array : ", end = "")
	printarray(arr, n)
	print("Orinal index array : ", end = "")
	printarray(index, n)

	rearrange(arr, index, n)

	print("Array after rearrange : ", end = "")
	printarray(arr, n)
	print("Index array after rearrange : ", end = "")
	printarray(index, n)
