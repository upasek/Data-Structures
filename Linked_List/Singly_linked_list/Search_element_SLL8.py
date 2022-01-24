# Search an element in a Linked List (Iterative )
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

	def searching(self, key):
		temp = self.head
		while temp:
			if (temp.data == key):
				print(f"{key} are in Linked List")
				return
			temp = temp.next

		else:
			print(f"{key} are not in linked list")
			return


if __name__ == '__main__':
	llist = LinkedList()
	llist.push(1)
	llist.push(2)
	llist.push(5)
	llist.push(9)
	llist.push(8)

	print("Given linked list : ", end='')
	llist.printlist()

	llist.searching(9)

	llist.searching(100)
