# Find all elements in array which have at-least two greater elements
# O(n)
# using sys module
import sys

def findelement(arr, l):
    first = -sys.maxsize
    second = -sys.maxsize
    for i in range(l):
        if arr[i] > first:
            second = first
            first = arr[i]

        elif arr[i] > second:
            second = arr[i]

    return second


def printelements(arr, l, index):
    for i in range(l):
        if arr[i] < index:
            print(arr[i], end = " ")
    print()


def printarray(arr, l):
    for i in range(l):
        print(arr[i], end = " ")
    print()


if __name__ == '__main__':
    arr = [2, -6, 3, 5, 1, 8, 9]
    l = len(arr)
    print("Given array : ", end='')
    printarray(arr, l)
    index = findelement(arr, l)
    print("Elements in array which have at-least two greater elements : ", end = '')
    printelements(arr, l, index)
