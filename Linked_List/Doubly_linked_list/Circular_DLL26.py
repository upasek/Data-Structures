class Node:
	"""docstring for ClassName"""
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLL:
	"""docstring for ClassName"""
	def __init__(self):
		self.head = None

	def insertFront(self, data):
		new_node = Node(data)
		temp = self.head
		if temp == None:
			self.head = new_node
			self.head.next = new_node
			self.head.prev = new_node
			return

		new_node.next = self.head
		new_node.prev = self.head.prev

		self.head.prev.next = new_node

		self.head.prev = new_node

		self.head = new_node


	def insertEnd(self, data):
		temp = self.head
		new_node = Node(data)

		if temp == None:
			self.head = new_node
			self.head.next = new_node
			self.head.prev = new_node
			return

		last = self.head.prev

		last.next = new_node
		new_node.prev = last

		new_node.next = self.head
		self.head.prev = new_node

	def insertAfter(self, prev, data):
		new_node = Node(data)

		temp = self.head
		while temp.data != prev:
			temp = temp.next

		new_node.next = temp.next
		temp.next.prev = new_node

		temp.next = new_node
		new_node.prev = temp


	def printDLL(self):
		temp = self.head
		it = temp
		print ("Traversal in forward direction : ", end="")
		while temp.next != it:
			print(temp.data, end = ' ')
			temp = temp.next
		print(temp.data)

		temp = self.head.prev
		it = temp
		print ("Traversal in reverse direction : ", end = '')
		while temp.prev != it:
			print(temp.data, end = ' ')
			temp = temp.prev
		print(temp.data)


if __name__ == '__main__':
	Dll = DoublyLL()
	Dll.insertEnd(5)
	Dll.insertEnd(7)
	Dll.insertFront(9)
	Dll.insertFront(1)
	Dll.insertEnd(8)
	Dll.insertEnd(3)
	Dll.insertAfter(5, 6)
	Dll.insertAfter(3, 10)

	Dll.printDLL()
