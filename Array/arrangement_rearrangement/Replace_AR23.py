#Given an array of integers, update every element with multiplication of previous and next elements with following exceptions.
# a) First element is replaced by multiplication of first and second.
# b) Last element is replaced by multiplication of last and second last.
# Q23

def rearrange(arr, l):
	num = []
	for i in range(l):
		num.append(arr[i])

	for i in range(l):
		if i == 0 or i == l-1:
			if i == 0:
				arr[i] = num[i] * num[i+1]
			elif i == l-1:
				arr[i] = num[i] * num[i-1]
		else:
			arr[i] = num[i-1] * num[i+1]


def printarray(arr, l):
	for i in range(l):
		print(arr[i], end = " ")
	print()


if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6, 7, 8]
	l = len(arr)
	print("Original array : ", end = "")
	printarray(arr, l)
	rearrange(arr, l)
	print("Array after rearrangement : ", end = "")
	printarray(arr, l)
