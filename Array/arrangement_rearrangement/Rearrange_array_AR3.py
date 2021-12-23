# rearrange the array such that elements at even positions are greater than all elements before it
# and elements at odd positions are less than all elements before it.

import array as arr

def rearrangearray(arr, n):
	num = []

	#no. of even position
	evenpos = (n//2)

	# no. of odd position
	oddpos = n - evenpos

	# copy all element
	for i in range(n):
		num.append(arr[i])

	# sort num array
	num.sort()

	# fill all odd position
	j = oddpos - 1

	for i in range(0, n, 2):
		arr[i] = num[j]
		j -= 1

	# fill all even position
	j = oddpos

	for i in range(1, n, 2):
		arr[i] = num[j]
		j += 1


def printarray(arr, n):
	for i in range(n):
		print(arr[i], end = " ")
	print()



arr = arr.array('i', [5, 4, 1, 2, 9, 8, 7, 6, 3])
size = len(arr)
print("Original array is : ",end = "")
printarray(arr, size)
rearrangearray(arr, size)
print("Array after rearrange : ",end = "")
printarray(arr, size)
