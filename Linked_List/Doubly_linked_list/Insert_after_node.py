# insert node after given node

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

	def Insertafter(self, prev_node, new_data):

		if prev_node is None:
			print("The given previous node cannot be NULL")
			return

		new_node = Node(new_data)

		new_node.next = prev_node.next

		prev_node.next = new_node

		new_node.prev = prev_node

		if new_node.next:
			new_node.next.prev = new_node


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
	Dllist.Insertafter(Dllist.head.next.next, 10)

	print("New linked list : ", end = '')
	Dllist.printDll()
