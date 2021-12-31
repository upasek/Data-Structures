# Find Second largest element in an array
# using sys module
# O(n)

import sys

def findelement(arr, l):
	first = -sys.maxsize
	second = -sys.maxsize
	for i in range(l):
		if arr[i] > first:
			second = first
			first = arr[i]
		if arr[i] > second and arr[i] != first:
			second = arr[i]

	return second

def printarray(arr, l):
    for i in range(l):
        print(arr[i], end = " ")
    print()

if __name__ == '__main__':
	arr = [12, 35, 1, 10, 1, 36]
	l = len(arr)
	print("Given array : ", end ="")
	printarray(arr, l)
	index = findelement(arr, l)
	print("Second largest element in an array :", index)
