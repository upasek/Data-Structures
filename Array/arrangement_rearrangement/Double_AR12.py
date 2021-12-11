def rearrange(arr, n):
	for i in range(n-1):
		if arr[i] == arr[i+1]:
			arr[i] += arr[i]
			arr[i+1] = 0

	cnt = 0
	for i in range(n):
		if arr[i] != 0:
			arr[cnt], arr[i] = arr[i], arr[cnt]
			cnt += 1


def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()



arr = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8]
n = len(arr)
print("Original array : ", end = "")
printarray(arr, n)
rearrange(arr, n)
print("Array after rearrange : ", end = "")
printarray(arr, n)
