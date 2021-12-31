# Find k pairs with smallest sums in two arrays
# O(n1*n2 + (k log(k)) ) k is size of a[]
# space complexity = O(k)
# complexity of sort() in python = O(nlog(n))

def Kthsmallest(arr1, n1, arr2, n2):
	a = [0] * (n1*n2)
	k = 0
	for i in range(n1):
		for j in range(n2):
			sum = arr1[i] + arr2[j]
			a[k] = [arr1[i], arr2[j], sum]
			k += 1

	a.sort(key = lambda x:x[2])
	return a


def printelement(a, k):
	for i in range(k):
		print(f"({a[i][0]}, {a[i][1]})", end = " ")
	print()


def printarray(arr, l):
    for i in range(l):
        print(arr[i], end = " ")
    print()


if __name__ == '__main__':
	arr1 = [1, 3, 11]
	n1 = 3
	print("Given arr1 : ", end="")
	printarray(arr1, n1)
	arr2 = [2, 4, 8]
	n2 = 3
	print("Given arr2 : ", end="")
	printarray(arr2, n2)

	k = 4
	a = Kthsmallest(arr1, n1, arr2, n2)
	print(f"{k} pairs with smallest sums in two arrays : ", end='')
	printelement(a, k)
