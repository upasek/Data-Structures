# Reversal algorithm for right rotation of an array

def rightRotate(arr, low, high):
	while low <= high:
		arr[low], arr[high] = arr[high], arr[low]
		low += 1
		high -= 1

def printarray(arr, n):
    for i in range(n):
        print(arr[i], end = " ")
    print()


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)-1
print("Original array is : ", end = "")
printarray(arr, n+1)

k = int(input("Enter the number of rotation : "))

start = (n-k)+1
rightRotate(arr, 0, n-k)
rightRotate(arr, start, n)
rightRotate(arr, 0, n)
print("Array after rotation : ", end = "")
printarray(arr, n+1)
