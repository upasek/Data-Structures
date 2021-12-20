# Given an array A of n elements, sort the array according to the following relations :
# A[i] >= A[i-1]    if i is even.
# A[i] <= A[i-1]    if i is odd
# Rearrange_array_AR10.py

def rearrange(arr, n):

    for i in range (1, n):

        # if index is even
        if (i % 2 == 0):
            if (arr[i] > arr[i - 1]):
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

        # if index is odd
        else:
            if (arr[i] < arr[i - 1]):
                arr[i - 1], arr[i] = arr[i] , arr[i - 1]

def printarray(arr, n):
    for i in range(n):
        print(arr[i], end = " ")
    print()

if __name__ == "__main__":
    arr = [1, 3, 2, 2, 5]
    n = len(arr)
    print("Original array : ", end = "")
    printarray(arr, n)
    rearrange(arr, n);
    print ("Array after rearrange : ", end = "")
    printarray(arr, n)
