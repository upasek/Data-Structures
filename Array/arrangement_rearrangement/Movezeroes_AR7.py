# Move all zeroes to end of array
def movezeroes(arr, n):
	count = 0
	for i in range(n):
		if arr[i] != 0:
			arr[i], arr[count] = arr[count], arr[i]
			count += 1

def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()



arr = [0, 0, 0, 4, 3, 0, 0, 0, 5, 9, 6, 8, 0]
size = len(arr)
print("Original array : ", end = "")
printarray(arr, size)
movezeroes(arr, size)
print("Array after move all zeroes : ", end ="")
printarray(arr, size)
