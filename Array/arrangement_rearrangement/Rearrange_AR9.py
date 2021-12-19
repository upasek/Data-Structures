# Rearrange positive and negative numbers
# Q9 and Q14

def rearrange(arr, n):
	cnt = 0
	for i in range(n):
		if arr[i] < 0:
			temp = arr[i]
			for j in range(i, cnt, -1):
				arr[j] = arr[j-1]
			arr[cnt] = temp
			cnt += 1


def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()


arr = [1, -2, 5, 3, -9, -8, 7]
size = len(arr)
print("Original array : ", end = "")
printarray(arr,size)
rearrange(arr, size)
print("Array after rearrange : ", end = "")
printarray(arr, size)
