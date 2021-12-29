# K maximum sums of non-overlapping contiguous sub-arrays
# O( k * n)

def findelements(arr, n, k):

	for i in range(k):
		max_so_far = -float('inf')
		max_here = 0
		start = 0
		end = 0
		s = 0

		for j in range(n):
			max_here += arr[j]
			# print(max_here)
			if max_so_far < max_here:
				max_so_far = max_here
				start = s
				end = j

			if max_here < 0:
				max_here = 0
				s = j + 1

		print("Maximum non-overlapping sub-array sum",
               i + 1, ": ", max_so_far, ", starting index: ",
               start, ", ending index: ", end, ".", sep = "")


        # Replace all elements of the maximum subarray
        # by -infinity. Hence these places cannot form
        # maximum sum subarray again.
		for l in range(start, end+1):
			arr[l] = -float("inf")

		# print(arr)


def printarray(arr, l, h):
	for i in range(l, h):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [4, 1, 1, -1, -3, -5, 6, 2, -6, -2]
	n = len(arr)
	print("Given array : ", end = "")
	printarray(arr, 0, n)
	k = 3
	findelements(arr, n, k)
