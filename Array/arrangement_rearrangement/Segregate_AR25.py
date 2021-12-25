# Given an array of integers, segregate even and odd numbers in the array.
#  All the even numbers should be present first, and then the odd numbers.

def rearrange(arr, l):
	temp = 0
	for i in range(l):
		if arr[i] % 2 == 0:
			arr[temp], arr[i] = arr[i], arr[temp]
			temp += 1


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [1, 3, 2, 4, 7, 6, 9, 10]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	rearrange(arr, l)
	print("Array after rearrange : ", end = "")
	printarray(arr, l)
