class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLL:

	def __init__(self):
		self.head = None

	def append(self, data):

		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		last = self.head
		while last.next:
			last = last.next

		last.next = new_node

		new_node.prev = last

		return

	def printDLL(self):
		temp = self.head
		while temp:
			print(temp.data, end = ' ')
			temp = temp.next
		print()


if __name__ == '__main__':
	Dllist = DoublyLL()
	Dllist.append(6)
	Dllist.append(5)
	Dllist.append(9)
	Dllist.append(8)
	Dllist.append(2)

	print("Linked List after append element at end : ", end = "")
	Dllist.printDLL()
