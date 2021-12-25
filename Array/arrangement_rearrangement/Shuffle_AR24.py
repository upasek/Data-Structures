# Shuffle a given array using Fisher–Yates shuffle Algorithm
# randomaly pick up element
# Q24

import random

def rearrange(arr, l):
	for i in range(l-1, 0, -1):
		j = random.randint(0, i)
		arr[i], arr[j] = arr[j], arr[i]



def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6, 7, 8]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	rearrange(arr, l)
	print("Array after rearrange : ", end = "")
	printarray(arr, l)
