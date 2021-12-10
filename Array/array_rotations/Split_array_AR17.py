# There is a given an array and split it from a specified position,
# and move the first part of array add to the end.


def splitarray(arr, n, k):
	for j in range(k):
		temp = arr[0]
		for i in range(n-1):
			arr[i] = arr[i+1]
		arr[n-1] = temp


def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()


arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
print("Original array is : ",end = "")
printarray(arr, n)
k = int(input("Enter the size of sub array : "))
splitarray(arr, n, k)
print("Array after split : ", end = "")
printarray(arr, n)
