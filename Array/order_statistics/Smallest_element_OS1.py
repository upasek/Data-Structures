# Given an array and a number k where k is smaller than size of array,
# we need to find the k’th smallest element in the given array.
#  It is given that ll array elements are distinct.

def smallestelement(arr, l, k):
	min = None
	j = 0
	while j < k:
		min = arr[j]
		for i in range(j+1, l):
			if arr[i] < min:
				min = arr[i]
				temp = i
		arr[j], arr[temp] = arr[temp], arr[j]
		if j == k - 1:
			return arr[j]
		j += 1

	# we also use simple methode
	# arr.sort()
	# return arr[k-1]


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [7, 10, 4, 3, 20, 15]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	k = int(input("Enter the vslue of 'k' (k < size of array) : "))
	item = smallestelement(arr, l, k)
	print(f"{k} smallest element in the given array is : {item}")
