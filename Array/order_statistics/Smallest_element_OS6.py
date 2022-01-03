# Kth smallest element in a row-wise and column-wise sorted 2D array | Set 1
# not complete

def heapify(hrr, n, j):
	smallest = j
	l = 2 * j + 1
	r = 2 * j + 2
	if l < n and hrr[smallest] > arr[l]:
		smallest = l
	if r < n and hrr[smallest] > arr[r]:
		smallest = l

	if smallest != j:
		heappify(arr, n, smallest)

	return smallest

def mainfunction(arr, n, k):
	hrr = [0] * n
	for i in range(n):
		hrr[i] = arr[i]

	for j in range(k):


def printarray(arr, n):
	for i in range(n):
		for j in range(n):
			print(arr[i][j], end = " ")
		print()
	print()

if __name__ == "__main__":
	arr = [[10, 20, 30, 40],
	[15, 25, 35, 45],
	[25, 29, 37, 48],
	[32, 33, 39, 50]]
	n = 4
	print("Given array : ", end = "\n")
	printarray(arr, n)
	k = int(input("Enter the value of k (k < size of array) : "))
	mainfunction(arr, n, k)
