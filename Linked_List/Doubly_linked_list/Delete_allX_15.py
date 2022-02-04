# Delete all occurrences of a given key in a doubly linked list
# O(n)

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

	def RemoveKey(self, key):
		temp = self.head
		while temp:
			if (temp.data==key) and (temp.prev == None):
				self.head.next.prev = None
				self.head = temp.next
				temp = temp.next
			elif temp.data == key:
				temp.prev.next = temp.next
				if temp.next is not None:
					temp.next.prev = temp.prev
				temp = temp.next
			else:
				temp = temp.next

	def printLL(self):
		temp = self.head
		while temp:
			print(temp.data, end = " ")
			temp = temp.next
		print()


if __name__ == '__main__':
	Dll = DoublyLL()

	Dll.push(4)
	Dll.push(8)
	Dll.push(4)
	Dll.push(6)
	Dll.push(4)
	Dll.push(2)
	Dll.push(4)
	Dll.push(4)


	print("Given Doubly Linked List : ", end = "")
	Dll.printLL()

	Dll.RemoveKey(4)

	print("New Doubly Linked List : ", end = '')
	Dll.printLL()
