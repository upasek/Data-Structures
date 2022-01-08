# Python program for deleting
# an element in an sorted arr
def binarysearch(arr:int, low: int, high:int , k:int ) -> int :
	if low > high:
		return -1
	mid = (low + high) // 2
	if arr[mid] == k:
		return mid
	elif arr[mid] < k:
		return binarysearch(arr, mid+1, high, k)
	elif arr[mid] > k:
		return binarysearch(arr, low, mid-1, k)


def deleting(arr: int , k: int , l: int ) -> int:
	pos = binarysearch(arr, 0, l-1, k)
	if pos == -1:
		print("Element not found")
		return -1

	else:
		for i in range(pos, l-1):
			arr[i] = arr[i+1]

		return l-1

def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()

if __name__ == "__main__":
	arr = [12, 16, 20, 40, 50, 70]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	k = int(input("Enter the element for deleting : "))
	n = deleting(arr, k, l)
	if n != -1:
		print("Array after deleting element : ", end = "")
		printarray(arr, n)
