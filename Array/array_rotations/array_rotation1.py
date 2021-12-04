# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

def arrayrotation(arr, num):
	size = len(arr)
	for i in range(0, num):
		store = arr[0]
		for j in range(len(arr)-1):
			arr[j] = arr[j+1]

		arr[len(arr) - 1] = store

def printarray(arr, size):
	for i in range(len(arr)):
		print(f"{arr[i]}",end = " ")



arr = [1, 2, 3, 4, 5, 6, 7]
size = len(arr)

print("Original array is :",end = " ")
printarray(arr, size)

num = int(input("\nEnter the number of rotation : "))
arrayrotation(arr, num)

print("Array after rotation :", end = " ")
printarray(arr, size)
print()
