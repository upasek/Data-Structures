#Given a sorted array of positive integers,
#rearrange the array in maximum minimum form

def rearrange(arr, l):
	low = 0
	high = l-1
	temp = [None] * l

	for i in range(l):
		if i % 2 == 0:
			temp[i] = arr[high]
			high -= 1
		else:
			temp[i] = arr[low]
			low += 1

	for i in range(l):
		arr[i] = temp[i]



def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6, 7, 8]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	rearrange(arr, l)
	print("Array after rearrangement : ", end = "")
	printarray(arr, l)
