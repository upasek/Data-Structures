# Delete a node in a Circular Doubly Linked List
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

	def DeleteNode(self, data):
		temp = self.head
		it = temp

		while temp.data != data:
			temp = temp.next
			if temp == it:
				print("Not present")
				return

		if temp.data == data:
			temp.prev.next = temp.next
			temp.next.prev = temp.prev
			return

		gc.collect()

	def printDll(self):
		temp = self.head
		it = temp
		while temp.next != it:
			print(temp.data, end = ' ')
			temp = temp.next
		print(temp.data)



if __name__ == '__main__':
	Dllist = DoublyLL()
	Dllist.push(1)
	Dllist.push(3)
	Dllist.push(5)
	Dllist.push(8)
	Dllist.push(7)

	print("Original linked list : ", end = '')
	Dllist.printDll()

	print("List after deleton 5 : ", end = "")
	Dllist.DeleteNode(5)
	Dllist.printDll()

	print("List after deleton 8 : ", end = "")
	Dllist.DeleteNode(8)
	Dllist.printDll()

	print("List after deleton 1 : ", end = "")
	Dllist.DeleteNode(1)
	Dllist.printDll()

	print("List after deleton : ", end = "")
	Dllist.DeleteNode(9)
	Dllist.printDll()
