# Find all elements in array which have at-least two greater elements
# O(nlog(n))
# using sorting algo(merge sort)

def meregesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        meregesort(L)
        meregesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printarray(arr, l, h):
    for i in range(l, h):
        print(arr[i], end = " ")
    print()


if __name__ == '__main__':
    arr = [2, -6, 3, 5, 1, 8, 9]
    l = len(arr)
    print("Given array : ", end='')
    printarray(arr, 0, l)
    meregesort(arr)
    print("Elements in array which have at-least two greater elements : ", end = '')
    printarray(arr, 0, l-2)
