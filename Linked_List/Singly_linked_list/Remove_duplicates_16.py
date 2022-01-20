# Remove duplicates from an sorted linked list
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
			print(temp.data, end = " ")
			temp = temp.next
		print()

	def push(self, new_data):
		new_node = Node(new_data)

		new_node.next = self.head

		self.head = new_node

	def remove(self):
		temp = self.head

		if temp is None:
			return

		while temp and temp.next:
			if temp.data == temp.next.data:
				temp.next = temp.next.next

			else:
				temp = temp.next


if __name__ == '__main__':
	llist = LinkedList()
	llist.push(21)
	llist.push(21)
	llist.push(20)
	llist.push(20)
	llist.push(13)
	llist.push(13)
	llist.push(12)
	llist.push(11)
	llist.push(11)
	llist.push(11)

	print("Given linked list : ", end='')
	llist.printlist()

	llist.remove()

	print("New linked list : ", end='')
	llist.printlist()
