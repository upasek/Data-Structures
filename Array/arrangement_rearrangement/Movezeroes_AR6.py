# Move all zeroes to end of array
def movezeroes(arr, n):
	temp = n-1
	a = 0
	#for i in range(temp):
	while a <= temp:
		if arr[a] == 0:
			for j in range(a, temp):
				arr[j] = arr[j+1]
			arr[temp] = arr[a]
			temp -= 1
		else:
			a += 1


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
