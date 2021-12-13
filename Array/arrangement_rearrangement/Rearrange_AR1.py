# Rearrange an array such that arr[i] = i
# and if i is not present, display -1 at that place.

def rearrangement(arr, n):
	for i in range(n):
		for j in range(n):
			if i == arr[j]:
				arr[i], arr[j] = arr[j], arr[i]

	for i in range(n):
		if arr[i] != i:
			arr[i] = -1

def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()


arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
size = len(arr)
print("Original array is : ", end = "")
printarray(arr, size)
rearrangement(arr, size)
print("Array after rearrangement : ", end = "")
printarray(arr, size)
