# Write a function to get Nth node in a Linked List
# Time Complexity: O(n)
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

	def searching(self, position):
		temp = self.head
		for i in range(position):
			temp = temp.next
			if temp is None:
				print(f"Index {position} Doesn\'t exist")
				return

		return temp.data


if __name__ == '__main__':
	llist = LinkedList()
	llist.push(1)
	llist.push(2)
	llist.push(5)
	llist.push(9)
	llist.push(8)

	print("Given linked list : ", end='')
	llist.printlist()

	index = llist.searching(2)
	k = 2
	if index is not None:
		print(f"Element at index {k} is :",index)

	index = llist.searching(6)
	k = 4
	if index is not None:
		print(f"Element at index {k} is :",index)
