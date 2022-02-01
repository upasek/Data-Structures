# Count triplets in a sorted doubly linked list whose sum is equal to a given value x
# Time complexity = O(n2)

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

	def countpairs(self, first, second, val, current):

		while first!=None and second!=None and first!=second and second.next!=first:

			if first.data + second.data == val:
				print("(",current.data, ',', first.data, ",",second.data, ")", end = " ")
				second = second.prev
				first = first.next

			elif (first.data + second.data) > val:
				second = second.prev
			else:
				first = first.next


	def CountTriplets(self, key):
		current, first, last = self.head, None, None

		last = self.head
		while last.next != None:
			last = last.next

		while current != None:

			first = current.next

			count, current = self.countpairs(first, last, key-current.data, current), current.next

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
