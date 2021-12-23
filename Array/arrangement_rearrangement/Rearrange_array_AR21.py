# Rearrange array such that even index elements are smaller and odd index elements are greater
# iterate over the array


def rearrange(arr, l):
	for i in range(l-1):
		if (i % 2 == 0 and arr[i] > arr[i+1]):
			arr[i], arr[i+1] = arr[i+1], arr[i]

		elif (i % 2 != 0 and arr[i] < arr[i+1]):
			arr[i], arr[i+1] = arr[i+1], arr[i]



def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [6, 4, 2, 1, 8, 3]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	rearrange(arr, l)
	print("Array after rearrangement : ", end = "")
	printarray(arr, l)
