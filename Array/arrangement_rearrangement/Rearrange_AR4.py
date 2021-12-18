# Rearrange positive and negative numbers in O(n) time and O(1) extra space

def rearrange(arr, n):
	i = -1
	for item in range(n):
		if arr[item] < 0:
			i += 1
			arr[i], arr[item] = arr[item], arr[i]

	pos, neg = i+1, 0

	while(pos < n and neg < pos and arr[neg] < 0):
		arr[neg], arr[pos] = arr[pos], arr[neg]
		neg += 2
		pos += 1



def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()


arr = [-1, 2, -3, -4, 5, 6, -7, 8, -9]
size = len(arr)
print("Original array is : ", end = "")
printarray(arr, size)
rearrange(arr, size)
print("Array after rearrangement : ", end = "")
printarray(arr, size)
