# K maximum sum combinations from two arrays
# O(n * n log(n))
def MergeSort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		L = arr[:mid]
		R = arr[mid:]
		MergeSort(L)
		MergeSort(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] > R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

def findsum(arr, brr, l, k):
	sum = []
	for i in range(l):
		for j in range(l):
			sum.append(arr[i] + brr[j])

	return sum


def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()


if __name__ == '__main__':
	arr = [4, 2, 5, 1]
	brr = [8, 0, 5, 3]
	n = len(arr)
	l = len(brr)
	print("Given first array : ", end = "")
	printarray(arr, n)
	print("Given second array : ", end = "")
	printarray(brr, l)
	k = int(input("Enter the value of k : "))
	sum = findsum(arr, brr, l, k)
	MergeSort(sum)
	print("Maximum sum combinations from two arrays : ", end = "")
	printarray(sum, k)
