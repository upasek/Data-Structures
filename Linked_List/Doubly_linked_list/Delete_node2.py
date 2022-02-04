# Delete a node in a Doubly Linked List
# for Garbage collection
import gc
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

	def DeleteNode(self, current_node):
		if current_node.next is None:
			current_node.prev.next = None
			return

		if current_node.prev is None:
			self.head = current_node.next
			return

		current_node.prev.next = current_node.next

		current_node.next.prev = current_node.prev

		gc.collect()

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

	Dllist.DeleteNode(Dllist.head.next.next)

	print("New linked list : ", end = '')
	Dllist.printDll()
