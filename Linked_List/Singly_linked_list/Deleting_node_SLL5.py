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

	def DeletingNode(self, position):
		temp = self.head

		if temp == None:
			return

		# If head node itself holds the key to be deleted
		if position == 0:
			self.head = temp.next
			temp = None
			return

		for i in range(position-1):
			temp = temp.next
			if temp is None:
				break

		if temp is None:
			return
		if temp.next is None:
			return

		next = temp.next.next

		temp.next = None

		temp.next = next



if __name__ == '__main__':
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	fourth = Node(4)
	fifth = Node(5)
	sixth = Node(6)

	llist.head.next = second
	second.next = third
	third.next = fourth
	fourth.next = fifth
	fifth.next = sixth

	print("Original LinkedList : ", end="")
	llist.printlist()

	llist.DeletingNode(3)

	print("LinkedList after Deleting node : ",end='')
	llist.printlist()
