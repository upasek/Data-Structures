# Given an array (or string), the task is to reverse the array/string.
def reversearray(arr, low, high):
	while(low <= high):
		arr[low], arr[high] = arr[high], arr[low]
		low += 1
		high -= 1


def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()


arr = [4, 5, 1, 2, 9]
size = len(arr)
print("original array : ",end = "")
printarray(arr, size)
reversearray(arr, 0, size-1)
print("Array after reversing : ")
printarray(arr, size)
