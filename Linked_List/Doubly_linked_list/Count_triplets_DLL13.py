# Count triplets in a sorted doubly linked list whose sum is equal to a given value x
# Time complexity = O(n3)
# Auxiliary Space: O(1)
class Node():
	"""docstring for ClassName"""
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLL:

	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)

		new_node.next = self.head

		if self.head is not None:
			self.head.prev = new_node

		self.head = new_node

	def CountTriplets(self, key):
		ptr1 = self.head
		ptr2 = None
		ptr3 = None

		while ptr1 != None:
			ptr2 = ptr1.next
			while ptr2 != None:
				ptr3 = ptr2.next
				while ptr3 != None:
					if (ptr1.data + ptr2.data + ptr3.data == key):
						print("(", ptr1.data, ",", ptr2.data,",", ptr3.data, ")", end=" ")

					ptr3 = ptr3.next
				ptr2 = ptr2.next
			ptr1 = ptr1.next
		print()

	def printLL(self):
		temp = self.head
		while temp:
			print(temp.data, end = " ")
			temp = temp.next
		print()


if __name__ == '__main__':
	Dll = DoublyLL()

	Dll.push(6)
	Dll.push(5)
	Dll.push(4)
	Dll.push(3)
	Dll.push(2)
	Dll.push(1)

	print("Given Doubly Linked List : ", end = "")
	Dll.printLL()

	print('Triplets in a sorted doubly linked list whose sum is equal to a given value x : ', end = "")
	Dll.CountTriplets(9)
