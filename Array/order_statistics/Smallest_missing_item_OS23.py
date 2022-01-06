# Find the smallest missing number
# O(log(n))
# binary search

def smallestelement(arr, low, high):
	if low > high:
		return high+1

	if low != arr[low]:
		return low

	mid = (low + high)//2

	if arr[mid] == mid:
		return smallestelement(arr, mid+1, high)

	return smallestelement(arr, 0, mid)


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end=" ")
	print()


if __name__ == '__main__':
	arr = [0, 1, 2, 3, 4, 5, 6, 10]
	n = len(arr)
	print("Given array : ", end = '')
	printarray(arr, n)
	item = smallestelement(arr, 0, n-1)
	print("Smallest missing number :", item)

