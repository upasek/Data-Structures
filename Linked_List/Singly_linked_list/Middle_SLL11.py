# Find the middle of a given linked list

# Method 1:
# Traverse the whole linked list and count the no. of nodes. Now traverse the list again till count/2 and return the node at count/2.
# O(n+m)
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
		count = 0
		temp = self.head
		while temp:
			count += 1
			temp = temp.next

		temp = self.head
		if count%2 != 0:
			for i in range(count//2):
				temp = temp.next
		else:
			for i in range(count//2):
				temp = temp.next

		print("Middle of a given linked list : ",temp.data)


if __name__ == '__main__':
	llist = LinkedList()
	for i in range(6, 0, -1):
		llist.push(i)
		llist.printLL()
		llist.Middle()
