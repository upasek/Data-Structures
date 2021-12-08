#Write a function rotate(arr[], d, n) that rotates arr[] of size n by d elements.
# revesaal algorithm for array rotation
# Let the array be arr[] = [1, 2, 3, 4, 5, 6, 7], d =2 and n = 7
# A = [1, 2] and B = [3, 4, 5, 6, 7]
# Reverse A, we get ArB = [2, 1, 3, 4, 5, 6, 7]
# Reverse B, we get ArBr = [2, 1, 7, 6, 5, 4, 3]
# Reverse all, we get (ArBr)r = [3, 4, 5, 6, 7, 1, 2]


def Reversearray(arr, low, high):
	while low <= high:
		arr[low], arr[high] = arr[high], arr[low]
		low += 1
		high -= 1

def printarray(arr, size):
	for i in range(size):
		print(f"{arr[i]}", end = " ")

	print()



arr = [1, 2, 3, 4, 5, 6, 7]
size = len(arr)
print("Original array is :", end = " ")
printarray(arr, size);

num = int(input("Enter the number of rotation : "))

Reversearray(arr, 0, num-1)
Reversearray(arr, num, size-1)
Reversearray(arr, 0, size-1)
print("Array after rotation : ", end = "")
printarray(arr, size)
