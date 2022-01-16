# Find Length of a Linked List (Iterative )
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

	def count(self):
		temp = self.head
		count = 0
		while temp:
			temp = temp.next
			count += 1

		return count

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
