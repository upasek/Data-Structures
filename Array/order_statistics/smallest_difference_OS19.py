# k-th smallest absolute difference of two elements in an array

from bisect import bisect as upper_bound

def countpairs(arr, l, mid):
	res = 0
	for i in range(l):
		res += upper_bound(arr, arr[i]+mid)

	return res


def findDifference(arr, l, k):
	arr.sort()

	low = arr[1] - arr[0]
	for i in range(1, l-1):
		low = min(low, arr[i+1]-arr[i])

	high = arr[l-1] - arr[0]
	while low < high:
		mid = (low + high) >> 1
		if (countpairs(arr, l, mid) < k):
			low = mid + 1
		else:
			high = mid

	return mid


def printarray(arr, l):
    for i in range(l):
        print(arr[i], end = " ")
    print()

if __name__ == '__main__':
	arr = [1, 2, 3, 4]
	l = len(arr)
	k = 5
	print("Given array : ", end ="")
	printarray(arr, l)
	index = findDifference(arr, l, k)
	print("Second largest element in an array :", index)
