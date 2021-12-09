# Find the Rotation Count in Rotated Sorted array
# Consider an array of distinct numbers sorted in increasing order.
# The array has been rotated (clockwise) k number of times.
# Given such an array, find the value of k.

def rotatearray(arr, size):
	index = 0
	for i in range(size):
		index += 1
		if arr[i] > arr[i+1]:
			return index

def printarray(arr, size):
	for i in range(size):
		print(arr[i],end = " ")
	print()

arr = [7, 9, 11, 12, 5]
size = len(arr)
print("The given array is : ",end = "")
printarray(arr, size)
index = rotatearray(arr,size)
print(f"{index} times clockwise array rotation is required.")
