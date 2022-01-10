# Python program for searching in unsorted array

def searching(arr, l, k):
	for i in range(l):
		if arr[i] == k:
			return i

	return -1


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [7, 10, 4, 3, 20, 15]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	k = int(input("Enter the element for searching : "))
	index = searching(arr, l, k)
	if index != -1:
		print(f"The element found at index {index}.")
	else:
		print("Element not found.")
