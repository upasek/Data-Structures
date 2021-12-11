# Given an array of n positive integers and a number k.
# Find the minimum number of swaps required to bring all the numbers less than or equal to k together.

# not complete

def countswap(arr, n, k):
	min = 0
	for i in range(n):
		cnt = 0
		if arr[i] <= k:




	return min;


def printarra(arr, size):
	for i in range(size):
		print(arr[i], end = " ")
	print()

arr = [2, 7, 9, 5, 8, 7, 4]
size = len(arr)
k = 5
print("Original array : ", end = "")
printarray(arr, size)
cnt = countswap(arr, size, k)
print("minimum swaps required is : ", cnt)
