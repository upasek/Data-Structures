#Given an array, only rotation operation is allowed on array.
#We can rotate the array as many times as we want.
#Return the maximum possbile of summation of i*arr[i].

def sumofarray(arr, size):
	maxval = 0
	sum = 0
	for i in range(size):
		if arr[i] > maxval:
			maxval = arr[i]
			index = i

	back = index
	mul = size-1
	for j in range(index, -1, -1):
		sum = sum + (mul*arr[back])
		mul -= 1
		back -= 1

	mul2 = 0
	for k in range(index+1, size):
		sum = sum + (mul2*arr[k])
		mul2 += 1

	return sum, (size-1)-index;


def printarray(arr, size):
	for i in range(size):
		print(arr[i], end = " ")
	print()


arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9];
size = len(arr)
print("Given array is : ",end = "")
printarray(arr, size)
largesum, index = sumofarray(arr, size)
print("We can %d by rotating array %d times."%(largesum, index))
