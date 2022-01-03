# Given an array and a number k where k is smaller than size of array,
# we need to find the k’th smallest element in the given array.
# It is given that ll array elements are distinct.
# QuickSort methode use
# O(nlog(n))

def partition(arr, low, high):
	i = low -1
	pivot = arr[high]

	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]

	return (i+1)


def QuickSort(arr, low, high):
	if low < high:
		pos = partition(arr, low, high)

		QuickSort(arr, low, pos-1)
		QuickSort(arr, pos+1, high)


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
	QuickSort(arr, 0, l-1)
	print(arr)
	print(f"{k} smallest element in the given array is : {arr[k-1]}")
