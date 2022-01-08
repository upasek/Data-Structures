# Python program for deleting an element in an unsorted arr

def deleting(arr, k):
	arr.remove(k)

def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()

if __name__ == "__main__":
	arr = [7, 10, 4, 3, 20, 15]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	k = int(input("Enter the element for inserting : "))
	deleting(arr, k)
	j = len(arr)
	print("Array after inserting element : ", end = "")
	printarray(arr, j)
