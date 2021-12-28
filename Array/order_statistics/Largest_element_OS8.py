# Program to find largest three elements in an array
# max heap
# O(klog(n)

def Heapify(arr, n, x):
	largest = x
	l = 2 * x + 1
	r = 2 * x + 2

	if l < n and arr[largest] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != x:
		arr[x], arr[largest] = arr[largest], arr[x]
		Heapify(arr, n, largest)


def HeapSort(arr, n, k):
	for i in range(n//2-1, -1, -1):
		Heapify(arr, n, i)

	for j in range(n-1, (n-1)-k, -1):
		arr[0], arr[j] = arr[j], arr[0]
		Heapify(arr, j, 0)

def printarray(arr, l, h):
	for i in range(l, h):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [3, 11, 12, 10, 9, 5, 4]
	n = len(arr)
	print("Given array : ", end = "")
	printarray(arr, 0, n)
	k = int(input("Enter the value of k (k < size of array) : "))
	HeapSort(arr, n, k)
	print(f"Largest {k} element in an array : ", end="")
	printarray(arr, n-k, n)
