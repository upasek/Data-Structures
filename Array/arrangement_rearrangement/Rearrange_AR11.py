# Rearrange an array in order – smallest, largest, 2nd smallest, 2nd largest, ..
# Time complexity O(n2).

def rearrange(arr, n):
	temp = 0
	for i in range(n):
		if (i % 2 == 0):
			min = arr[i]
			for j in range(i, n):
				if arr[j] < min:
					min = arr[j]
					temp = j
			arr[i], arr[temp] = arr[temp], arr[i]

		else:
			max = arr[i]
			for k in range(i, n):
				if arr[k] > max:
					max = arr[k]
					temp = k
			arr[i], arr[temp] = arr[temp], arr[i]



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
