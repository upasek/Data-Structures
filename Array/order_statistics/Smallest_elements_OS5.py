# k largest(or smallest) elements in an array | added Min Heap method
# O(k log(n))

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


def Heapsort(arr, high, k):
	for i in range((high//2)-1, -1, -1):
		Heapify(arr, high, i)

	for i in range(high-1, (high-1)-k, -1):
		arr[0], arr[i] = arr[i], arr[0]
		Heapify(arr, i, 0)


def printarray(arr, low, high):
	for i in range(low, high):
		print(arr[i], end=' ')
	print()


def printsmallestelement(arr, low, high):
	for i in range(high-1, low-1, -1):
		print(arr[i], end = " ")
	print()

if __name__ == "__main__":
	arr = [1, 23, 12, 9, 30, 2, 50]
	l = len(arr)
	print("Give array : ",end="")
	printarray(arr, 0, l)
	k = int(input("Enter the value of k (k < size of array) : "))
	Heapsort(arr, l, k)
	print(f"First {k} smallest elements in array : ", end = "")
	printsmallestelement(arr, l-k,l)
