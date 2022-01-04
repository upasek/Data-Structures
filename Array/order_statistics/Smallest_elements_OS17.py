# k smallest elements in same order using O(1) extra space
# min heap
# O(k*n)
# but not in same order

def findelements(arr, n, k):
	for i in range(k):
		min_val = arr[i]
		pos = i
		for j in range(i, n):
			if arr[j] < min_val:
				min_val = arr[j]
				pos = j
		arr[i], arr[pos] = arr[pos], arr[i]


def printarray(arr, l, h):
	for i in range(l, h):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [1, 5, 8, 9, 6, 7, 3, 4, 2, 0]
	n = len(arr)
	print("Given array : ", end = "")
	printarray(arr, 0, n)
	k = int(input("Enter the value of k : "))
	findelements(arr, n, k)
	print("k smallest elements : ", end='')
	printarray(arr, 0, k)
