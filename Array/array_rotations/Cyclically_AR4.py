#Given an array, cyclically rotate the array clockwise by one.

def rotate(arr, num, size):
	iter = size - 1
	for i in range(num):
		store = arr[iter]

		for j in range(size-1, 0, -1):
			arr[j] = arr[j - 1]

		arr[0] = store



def printarray(arr, size):

	for i in range(size):
		print(f"{arr[i]}", end = " ")

	print()




arr = [1, 2, 3, 4, 5, 6, 7]
size = len(arr)
print("Original array is : ",end = "")
printarray(arr, size)

num = int(input("Enter the number of rotation : "))
rotate(arr, num, size)

print("Array after rotation : ",end = "")
printarray(arr, size)
