# Search an element in a sorted and rotated array

def binarysearch(arr, low, high, element):
	if low > high:
		return " ";

	mid = (low+high) // 2
	if arr[mid] == element:
		return mid;
	elif element > arr[mid]:
		return binarysearch(arr, mid+1, high, element)
	elif element < arr[mid]:
		return binarysearch(arr, low, mid-1, element)


def pivotelement(arr, low, high, size):
	mid = (low + high) // 2

	if arr[mid] > arr[mid+1]:
		return mid+1;
	if arr[mid] < arr[mid-1]:
		return mid;
	else:
		if arr[mid] < arr[high]:
			return minimumelement(arr, low, mid - 1, n);
		elif arr[mid] > arr[low]:
			return minimumelement(arr, mid + 1, high, n)


def printarray(arr, size):
	for i in range(size):
		print(f"{arr[i]}", end = " ")
	print()




arr = [4, 6, 1, 2, 3]
size = len(arr)

print("Original array is : ", end = "")
printarray(arr, size)

num = int(input("Enter the element for searching : "))
element = int(pivotelement(arr,0, size-1, size - 1))
index = 0
if num >= arr[0]:
	index = binarysearch(arr, 0, element-1, num)
elif num <= arr[size-1]:
	index = binarysearch(arr, element, size-1, num)

if index != " ":
	print("Element found at index ", index)
elif index == " ":
	print("Element not found")
