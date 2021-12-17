# Positive elements at even and negative at odd positions
# Q22

def rearrange(arr, l):
	positive = 0
	negative = 1
	while True:
		while positive < l and arr[positive] >= 0:
			positive += 2

		while negative < l and arr[negative] <= 0:
			negative += 2

		if positive < l and negative < l:
			temp = arr[positive]
			arr[positive] = arr[negative]
			arr[negative] = temp
		else:
			break;


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [1, -3, 5, 6, -3, 6, -7, -4, 9, 10]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	rearrange(arr, l)
	print("Array after rearrangement : ", end = "")
	printarray(arr, l)
