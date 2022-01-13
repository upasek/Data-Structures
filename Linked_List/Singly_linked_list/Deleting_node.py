class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def printlist(self):
		temp = self.head
		while temp:
			print(temp.data, end = ' ')
			temp = temp.next
		print()

	def DeletingNode(self, key):
		temp = self.head

		# If head node itself holds the key to be deleted
		if temp is not None:
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return

		while (temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		if temp == None:
			return

		prev.next = temp.next

		temp = None




if __name__ == '__main__':
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	fourth = Node(4)

	llist.head.next = second
	second.next = third
	third.next = fourth

	llist.printlist()

	llist.DeletingNode(1)

	llist.printlist()
