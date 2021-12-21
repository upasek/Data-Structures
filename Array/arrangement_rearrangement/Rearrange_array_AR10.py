# Given an array A of n elements, sort the array according to the following relations :
# A[i] >= A[i-1]    if i is even.
# A[i] <= A[i-1]    if i is odd
# Rearrange_array_AR.py

def rearrange(arr, n):
	evenpos = (n//2)
	oddpos = n-evenpos
	num = []
	for i in range(n):
		num.append(arr[i])

	num.sort()

	j = 0
	for i in range(0, n, 2):
		arr[i] = num[j]
		j += 1

	j = n-1
	for i in range(1, n, 2):
		arr[i] = num[j]
		j -= 1




def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [1, 3, 2, 2, 5]
	size = len(arr)
	print("Original array : ", end = "")
	printarray(arr, size)
	rearrange(arr, size)
	print("Array after rearrange : ", end = "")
	printarray(arr, size)
