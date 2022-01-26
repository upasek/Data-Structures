# Pairwise swap elements of a given linked list
# Input : 1->2->3->4->5->6->NULL
# Output : 2->1->4->3->6->5->NULL
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

	def swapdata(self):
		temp = self.head

		while temp and temp.next:
			if temp.data == temp.next.data:
				temp = temp.next.next
			else:
				temp.data, temp.next.data = temp.next.data, temp.data
				temp = temp.next.next



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

	llist.swapdata()

	print("New linked list : ", end="")
	llist.printlist()
