# Sorting the Linked List
# O(n) create a list
# O(nlog(n)) for sorting list
# O(n) Deleting data in list
# O(n) for put items in linked list from list

# O(n) space

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

	def sorting(self):
		listX = []
		# put data in list
		temp = self.head
		while temp:
			listX.append(temp.data)
			temp = temp.next

		# sort list in reverse order
		listX.sort(reverse=True)

		# deleting data in linked list
		temp = self.head
		while temp:
			prev = temp.next
			del temp.data
			temp = prev

		# enter the data in linked list
		self.head = None

		for i in listX:
			self.push(i)


if __name__ == '__main__':
	llist = LinkedList()
	llist.push(6)
	llist.push(7)
	llist.push(1)
	llist.push(4)
	llist.push(5)
	llist.push(10)
	llist.push(12)
	llist.push(8)
	llist.push(15)
	llist.push(17)

	print("Given linked list : ", end="")
	llist.printlist()

	llist.sorting()

	print("New linked list : ", end="")
	llist.printlist()
