# Find k numbers with most occurrences in the given array
# Auxiliary Space: O(d)
# Time Complexity: O(d log d), where d is the count of distinct elements in the array

def findNumbers(arr, n):
	brr = {} # dictionaries to store element and their number of count
	for i in range(n):
		if arr[i] in brr:
			brr[arr[i]] += 1
		else:
			brr[arr[i]] = 1

	a = [0] * len(brr) # a = [] a is list of list
	j = 0
	for i in brr:
		a[j] = [i, brr[i]]
		j += 1
	a.sort(key = lambda x: x[0], reverse=True)
	a.sort(key = lambda x: x[1], reverse=True)
	return a


def printarray(arr, l):
    for i in range(l):
        print(arr[i], end = " ")
    print()


def printelement(a, k):
	for i in range(k):
		print(a[i][0], end=" ")
	print()


if __name__ == '__main__':
	arr = [3, 1, 4, 4, 5, 2, 6, 1]
	n = len(arr)
	k = 2
	print("Given array : ", end="")
	printarray(arr, n)
	a = findNumbers(arr, n)
	print("k numbers with most occurrences in the given array : ", end="")
	printelement(a, k)
