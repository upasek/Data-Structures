# Python program for searching in
# sorted array

def searching(arr, low, high, k):
	if low > high:
		return -1
	mid = (low + high) // 2
	if arr[mid] == k:
		return mid
	elif arr[mid] < k:
		return searching(arr, mid+1, high, k)
	elif arr[mid] > k:
		return searching(arr, low, mid-1, k)

def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [ 5, 6, 7, 8, 9, 10 ]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	k = int(input("Enter the element for searching : "))
	index = searching(arr, 0, l-1, k)
	if index != -1:
		print(f"The element found at index {index}.")
	else:
		print("Element not found.")
