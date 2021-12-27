# Program to find largest element in an array
# max heap
# O(log(n)

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


def HeapSort(arr, n):
	for i in range(n//2-1, -1, -1):
		Heapify(arr, n, i)

def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [3, 11, 12, 10, 9, 5, 4]
	n = len(arr)
	print("Given array : ", end = "")
	printarray(arr, n)
	HeapSort(arr, n)
	print(f"largest element in an array is : {arr[0]}")
