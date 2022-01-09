# Python program for inserting
# an element in an sorted array

def inserting(arr, k, index, l):
	for i in range(10):
		arr.append(0)

	if index >= l:
		print("Index is out of range")
		return

	for i in range(l, index, -1):
		arr[i] = arr[i-1]

	arr[index] = k

	return l+1


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()

if __name__ == "__main__":
	arr = [12, 16, 20, 40, 50, 70]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	k = int(input("Enter the element for inserting : "))
	index = int(input("Enter the index for inserting : "))
	n = inserting(arr, k, index, l)
	print("Array after inserting element : ", end = "")
	printarray(arr, n)
