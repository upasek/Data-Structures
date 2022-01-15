# Node class
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


# Linked List class contains a Node object
class LinkedList:
	""" This class is use to initialize the head"""
	# Function to initialize head
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


if __name__ == '__main__':
	# start with empty list

	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second # Link first node with second
	second.next = third # Link second node with the third node

	llist.printList()
