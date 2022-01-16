# Find Length of a Linked List (Recursive)
# Iterative
# O(n)
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

	def push(self, new_data):
		new_node = Node(new_data)

		new_node.next = self.head

		self.head = new_node

	def getcount(self, node):
		if (not node):
			return 0
		else:
			return 1 + self.getcount(node.next)

	def count(self):
		return self.getcount(self.head)

if __name__ == '__main__':
	llist = LinkedList()
	llist.push(1)
	llist.push(2)
	llist.push(5)
	llist.push(9)
	llist.push(8)

	print("Given linked list : ", end='')
	llist.printlist()

	count = llist.count()
	print("Length of a Linked List : ", count)
