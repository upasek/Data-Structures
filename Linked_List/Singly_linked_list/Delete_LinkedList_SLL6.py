# Write a function to delete a Linked List
# Time Complexity: O(n)
# Auxiliary Space: O(1)

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


	def DeletingLL(self):
		temp = self.head
		while temp:
			prev = temp.next

			del temp.data

			temp = prev




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

	llist.DeletingLL()

	print("Linked list deleted")
