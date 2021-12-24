# Rearrange array in alternating positive & negative items with O(1) extra space | Set 1
#  maintaining the order of appearance.

# not complete

def Rearrange(arr, n):
	for i in range(n):






def printarray(arr, size):
	for i in range(size):
		print(arr[i], end = " ")
	print()


arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
size = len(arr)
print("Original array : ", end = "")
printarray(arr, size)
Rearrange(arr, size)
print("Array after Rearrangement : ",end = "")
printarray(arr, size)
