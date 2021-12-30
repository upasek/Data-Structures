# Program for Mean and median of an unsorted array
def mergesort(arr):
	if len(arr) > 1:
		mid = len(arr)  // 2
		L = arr[:mid]
		R = arr[mid:]
		mergesort(L)
		mergesort(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j +=1
			k +=1
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

def findmedian(arr, l):
	if l % 2 != 0:
		return float(arr[int(l/2)])
	else:
		return float((arr[int(l/2)] + arr[int((l-1) / 2)] ) / 2)

def findmean(arr, l):
	sum = 0
	for i in range(l):
		sum += arr[i]

	return sum / l


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end= " ")
	print()


if __name__ == "__main__":
	arr = [1, 3, 4, 2, 7, 5, 8, 6]
	l = len(arr)
	print("Given array : ", end = "")
	printarray(arr, l)
	print("Mean of an array : ", findmean(arr, l))
	# for median first we have to sort our array
	mergesort(arr)
	print("Median of an array : ", findmedian(arr, l))
