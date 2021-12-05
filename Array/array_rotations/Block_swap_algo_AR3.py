# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
#



def swaparray(arr, fi, si, d):
	for i in range(d):
		temp = arr[fi + i]
		arr[fi + i] = arr[si + i]
		arr[si + i] = temp



def leftrotate(arr, d, n):
	i = d
	j = n - d
	if (d == 0 or d == n):
		return;

	while i != j:
		if i < j:
			swaparray(arr, d - i, d + j - i, i)
			j -= 1
		else:
			swaparray(arr, d - i, d, j)
			i -= j
	swaparray(arr, d - i, d, i)

arr = [1, 2, 3, 4, 5, 6, 7]
leftrotate(arr, 3, 7)
print(arr)
