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

		new_node.next = self.head

		if self.head is not None:
			self.head.prev = new_node

		self.head = new_node

	def DeleteNode(self, key):
		temp = self.head
		if key == 1:
			self.head = temp.next
			self.head.next.prev = None
			return

		for i in range(1, key):
			temp = temp.next
			if temp is None:
				print("Out of range")
				return

		temp.prev.next = temp.next

		if temp.next is not None:
			temp.next.prev = temp.prev


	def printLL(self):
		temp = self.head
		while temp:
			print(temp.data, end=' ')
			temp = temp.next
		print()


if __name__ == '__main__':
	Dll = DoublyLL()
	Dll.push(8)
	Dll.push(4)
	Dll.push(2)
	Dll.push(6)
	Dll.push(1)

	print("Given LinkedList : ", end="")
	Dll.printLL()

	Dll.DeleteNode(6)

	print("New LinkedList : ", end="")
	Dll.printLL()
