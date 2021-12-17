# Move all negative elements to end in order with extra space allowed
# Note: Order of elements is important here.
def rearrange(arr, n):
    temp = [0] * n
    j = 0
    for i in range(n):
        if arr[i] > 0:
            temp[j] = arr[i]
            j += 1

    for i in range(n):
        if arr[i] < 0:
            temp[j] = arr[i]
            j += 1

    for i in range(n):
        arr[i] = temp[i]


def printarray(arr, n):
    for i in range(n):
        print(arr[i], end = " ")
    print()

if __name__ == "__main__":
    arr = [1, -1, 3, 2, -7, -5, 11, 6]
    n = len(arr)
    print("Original array : ", end = "")
    printarray(arr, n)
    rearrange(arr, n);
    print ("Array after rearrange : ", end = "")
    printarray(arr, n)
