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

	def Reverse(self):
		# temp = self.head
		# count = 0
		# while temp:
		# 	count += 1
		# 	temp = temp.next
		# print(count)
		current = self.head
		prev = None
		while current:
			Next = current.next
			current.next = prev
			prev = current
			current = Next

		self.head = prev


if __name__ == '__main__':
	llist = LinkedList()
	llist.push(14)
	llist.push(20)
	llist.push(13)
	llist.push(12)
	llist.push(15)
	llist.push(10)


	print("Given linked list : ", end="")
	llist.printlist()

	llist.Reverse()

	print("New linked list : ", end="")
	llist.printlist()
