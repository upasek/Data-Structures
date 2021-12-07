# A sorted array is rotated at some unknown point, find the minimum element in it.
# The following solution assumes that all elements are distinct.


def minimumelement(arr, low, high, n):
	mid = (low + high) // 2
	if arr[mid] > arr[mid+1]:
		return arr[mid+1];
	if arr[mid] < arr[mid-1]:
		return arr[mid];
	else:
		if arr[mid] < arr[high]:
			return minimumelement(arr, low, mid - 1, n);
		elif arr[mid] > arr[low]:
			return minimumelement(arr, mid + 1, high, n)


def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()


arr = [15, 1, 2, 5, 6, 7, 8, 9, 10]
n = len(arr)
print("Original array is : ",end = "")
printarray(arr, n)
print("Minimum element in given array : ",end = "")
inv = minimumelement(arr, 0, n-1, n)
print(inv)
