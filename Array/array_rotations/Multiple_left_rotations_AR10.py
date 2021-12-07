# Given an array of size n and multiple values around which we need to left rotate the array.
# How to quickly find multiple left rotations?

def preprocess(arr, n):
    size = n
    temp = []
    for i in range(n):
        temp.append(arr[i])

    temp.extend(temp)
    return temp


def leftRotate(arr, n, k, temp):
    start = k % n
    for i in range(start, start+n):
        print(temp[i], end = " ")
    print()

def printarray(arr, n):
    for i in range(n):
        print(arr[i], end = " ")
    print()


arr = [1, 3, 5, 7, 9]
print("Original array is : ",end = "")
n = len(arr)
printarray(arr, n)
temp = preprocess(arr, n)

k = 2
print(f"{k} times array rotation : ",end = "")
leftRotate(arr, n, k, temp)

k = 9
print(f"{k} times array rotation : ",end = "")
leftRotate(arr, n, k, temp)

k = 5
print(f"{k} times array rotation : ",end = "")
leftRotate(arr, n, k, temp)
