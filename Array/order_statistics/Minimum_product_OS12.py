# Minimum product of k integers in an array of positive Integers
# O(k log(n))
# use heapify algo

def Heapify(arr, l, x):
	smallest = x
	L = 2 * x + 1
	R = 2 * x + 2
	if L < l and arr[smallest] > arr[L]:
		smallest = L
	if R < l and arr[smallest] > arr[R]:
		smallest = R

	if smallest != x:
		arr[smallest], arr[x] = arr[x], arr[smallest]
		Heapify(arr, l, smallest)


def Heapsort(arr, l, k):
	count = 1
	for i in range(l//2 -1, -1 , -1):
		Heapify(arr, l, i)

	for i in range(l-1, (l-1)-k, -1):
		count *= arr[0]
		arr[0], arr[i] = arr[i], arr[0]
		Heapify(arr, i, 0)

	return count


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end= " ")
	print()


if __name__ == "__main__":
	arr = [198, 76, 544, 123, 154, 675]
	l = len(arr)
	print("Given array : ", end = "")
	printarray(arr, l)
	k = int(input("Enter the value of k ( k < size of array ) : "))
	print("Median of an array : ", Heapsort(arr, l, k))
