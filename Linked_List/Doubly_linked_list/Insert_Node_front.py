class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLL:

	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)

		new_node.data = data

		new_node.next = self.head

		if self.head is not None:
			self.head.prev = new_node

		self.head = new_node

	def pushFront(self, data):
		new_node = Node(data)

		new_node.next = self.head

		self.head.prev = new_node

		self.head = new_node


	def printDll(self):
		temp = self.head
		while temp:
			print(temp.data, end = ' ')
			temp = temp.next
		print()


if __name__ == '__main__':
	Dllist = DoublyLL()
	Dllist.push(1)
	Dllist.push(3)
	Dllist.push(5)
	Dllist.push(8)
	Dllist.push(7)

	print("Original linked list : ", end = '')
	Dllist.printDll()

	Dllist.pushFront(2)

	print("New linked list : ", end = '')
	Dllist.printDll()
