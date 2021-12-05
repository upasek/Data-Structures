#Given an array that is sorted and then rotated around an unknown point.
#Find if the array has a pair with a given sum ‘x’. It may be assumed that all elements in the array are distinct.

def findpair(arr, size, num):
	print("There is a pair with sum 16 : ", end = "")
	for i in range(size):
		if arr[i] > num:
			continue;
		else:
			for j in range(i+1,size):
				if (arr[i] + arr[j]) == num:
					print(f"({arr[i]}, {arr[j]})", end = " ")

	print()


def printarray(arr, size):
	for i in range(size):
		print(f"{arr[i]}",end = " ")
	print()



arr = [11, 15, 2, 3, 7, 8]
size = len(arr)

print("Original array is :", end = " ")
printarray(arr, size)

num = 10
findpair(arr, size, num)
