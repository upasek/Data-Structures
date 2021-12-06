# Given an array of size n and multiple values around which we need to left rotate the array.
# How to quickly print multiple left rotations?
# Print left rotation of array in O(n) time and O(1) space

def rotatearray(arr, n, k):
	for i in range(n):
		print(arr[(k + i) % n], end = " ")
	print()


def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()

arr = [1, 3, 5, 7, 9]
n = len(arr)
print("Original array is : ", end = "")
printarray(arr, n)
k = int(input("Enter the number of rotation : "))
print("Array after rotation : ", end = "")
rotatearray(arr, n, k)
