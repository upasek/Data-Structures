# K-th Largest Sum Contiguous Subarray
# Input: a[] = {20, -5, -1}
# 20, 15, 14, -5, -6, -1
# O(n^2 log (k))

import heapq

def kthLargestSum(arr, l, k):
	sum = []
	sum.append(0)
	sum.append(arr[0])
	for i in range(2, l+1):
		sum.append(sum[i-1]+ arr[i-1])
	print(sum)

	Q = []
	heapq.heapify(Q)

	for i in range(1, l+1):
		for j in range(i, l+1):
			x = sum[j] - sum[i -1]

			if len(Q) < k:
				heapq.heappush(Q, x)
			else:
				if Q[0] < x:
					heapq.heappop(Q)
					heapq.heappush(Q, x)
			print(Q)

	return Q[0]


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == '__main__':
	arr = [10,-10,20,-40]
	l = len(arr)
	print("Given array : ", end = "")
	printarray(arr, l)
	k = int(input("Enter the value of k : "))
	index = kthLargestSum(arr, l, k)
	print(f"{k}-th Largest Sum Contiguous Subarray : ", index)
