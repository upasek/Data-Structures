# Given an array and a number k where k is smaller than size of array,
# we need to find the k’th smallest element in the given array.
# It is given that ll array elements are distinct.
# Heap Sort methode use (max heap)
# O(nlog(n))

def heapify(arr, l, x):
	largest = x
	L = 2 * x + 1
	R = 2 * x + 2

	if L < l and arr[largest] < arr[L]:
		largest = L

	if R < l and arr[largest] < arr[R]:
		largest = R

	if largest != x:
		arr[largest], arr[x] = arr[x], arr[largest]
		heapify(arr, l, largest)


def Heapsort(arr, l):
	for i in range(l//2-1, -1, -1):
		heapify(arr, l, i)

	for i in range(l-1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)

def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [7, 10, 4, 3, 20, 15]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	k = int(input("Enter the vslue of 'k' (k < size of array) : "))
	Heapsort(arr, l)
	print(f"{k} smallest element in the given array is : {arr[k-1]}")
