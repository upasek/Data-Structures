# Find the middle of a given linked list
# Method 2:
# Traverse linked list using two pointers. Move one pointer by one and
# the other pointers by two. When the fast pointer reaches the end slow pointer will reach the middle of the linked list.

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_Node = Node(new_data)

		new_Node.next = self.head

		self.head = new_Node

	def printLL(self):
		print("Given Linked List : ", end = "")
		temp = self.head
		while temp:
			print(temp.data, end = ' ')
			temp = temp.next
		print()

	def Middle(self):
		slow = self.head
		fast = self.head

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		print("Middle of a given linked list : ",slow.data)



if __name__ == '__main__':
	llist = LinkedList()
	for i in range(6, 0, -1):
		llist.push(i)
		llist.printLL()
		llist.Middle()
