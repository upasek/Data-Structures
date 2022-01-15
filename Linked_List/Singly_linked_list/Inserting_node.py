class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	# This function prints contents of linked list
    # starting from head
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end = " ")
			temp = temp.next
		print()

	# push element in front of linkedList
	def push_front(self, new_data):
		new_node = Node(new_data)

		new_node.next = self.head

		self.head = new_node

	# insert element in linked list
	def Insert_middle(self, prev_node, new_data):
		if prev_node is None:
			print("Given previous node must in LinkedList")
			return
		new_node = Node(new_data)

		new_node.next = prev_node.next

		prev_node.next = new_node

	# append element at end of linkedList
	def append(self, new_data):
		new_node = Node(new_data)

		if self.head is None:
			self.head = new_node
			return

		last = self.head
		while (last.next):
			last = last.next

		last.next = new_node


if __name__ == '__main__':
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	fourth = Node(4)
	fifth = Node(5)

	llist.head.next = second
	second.next = third
	third.next = fourth
	fourth.next = fifth

	llist.printList()

	llist.push_front(10)    # push 10 in front of linkedlist

	llist.printList()

	llist.Insert_middle(third.next, 11) # insert 11 in between 4 and 5

	llist.printList()

	llist.append(50)     # append 50 at the end of linked list

	llist.printList()

	print(.data)

	print('Created linked list is : ', end = '')
	llist.printList()
