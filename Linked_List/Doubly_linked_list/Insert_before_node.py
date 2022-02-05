# insert node before given node

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

	def InsertBefore(self, next_node, new_data):
		if next_node is None:
			print("The given Next node cannot be NULL")
			return

		new_node = Node(new_data)

		new_node.next = next_node

		new_node.prev = next_node.prev

		if next_node.prev is None:
			self.head = new_node
		else:
			next_node.prev.next = new_node

		return


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

	# insert 10 after 5
	Dllist.InsertBefore(Dllist.head.next.next, 10)

	print("New linked list : ", end = '')
	Dllist.printDll()
