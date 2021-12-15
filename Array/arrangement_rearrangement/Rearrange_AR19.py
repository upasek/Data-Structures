#Move all negative numbers to beginning and positive to end with constant extra space
# Note: Order of elements is not important here.


def rearrange(arr, l):
	temp = 0
	for i in range(l):
		if arr[i] < 0:
			arr[temp], arr[i] = arr[i], arr[temp]
			temp += 1



def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	rearrange(arr, l)
	print("Array after rearrangement : ", end = "")
	printarray(arr, l)
