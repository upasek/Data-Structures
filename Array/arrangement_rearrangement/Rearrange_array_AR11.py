# Rearrange an array in order – smallest, largest, 2nd smallest, 2nd largest, ..
# Time complexity O(n).


def rearrange(arr, n):
	num = []
	for i in range(n):
		num.append(arr[i])

	num.sort()
	i, j = 0, n-1
	for k in range(n):
		if (k % 2 == 0):
			arr[k] = num[i]
			i += 1
		else:
			arr[k] = num[j]
			j -= 1



def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()



arr = [5, 8, 1, 4, 2, 9, 3, 7, 6]
n = len(arr)
print("Original array : ", end = "")
printarray(arr, n)
rearrange(arr, n)
print("Array after rearrange : ", end = "")
printarray(arr, n)
