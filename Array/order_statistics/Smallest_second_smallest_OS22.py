# Find the smallest and second smallest elements in an array
# O(n)
# using sys module
# another methode is sort array and print 1st two element( O(nlog(n)) )
import sys

def findelement(arr, l):
    first = sys.maxsize
    second = sys.maxsize
    for i in range(l):
        if arr[i] < first:
            second = first
            first = arr[i]

        elif arr[i] < second and arr[i] != first:
            second = arr[i]

    return first, second


def printarray(arr, l):
    for i in range(l):
        print(arr[i], end = " ")
    print()


if __name__ == '__main__':
    arr = [12, 13, 1, 10, 34, 1]
    l = len(arr)
    print("Given array : ", end='')
    printarray(arr, l)
    index1, index2 = findelement(arr, l)
    print("Smallest elements in an array : ", index1)
    print("Second smallest elements in an array : ", index2)
