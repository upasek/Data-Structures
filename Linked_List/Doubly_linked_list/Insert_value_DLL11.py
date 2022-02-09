# Insert value in sorted way in a sorted doubly linked list

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLL:

	def __init__(self):
		self.head = None

	def SortedInsert(self, data):
		New_Node = Node(data)
		if self.head == None:
			self.head = New_Node

		elif self.head.data >= data:
			New_Node.next = self.head
			self.head.prev = New_Node
			self.head = New_Node
		else:
			temp = self.head
			while (temp.next is not None) and (temp.next.data < data):
				temp = temp.next

			New_Node.next = temp.next

			if temp.next.prev is not None:
				New_Node.next.prev = New_Node

			temp.next = New_Node
			New_Node.prev = temp


	def printDLL(self):
		temp = self.head
		while temp:
			print(temp.data, end = ' ')
			temp = temp.next
		print()



if __name__ == '__main__':
	Dll = DoublyLL()
	Dll.SortedInsert(8)
	Dll.SortedInsert(3)
	Dll.SortedInsert(7)
	Dll.SortedInsert(2)
	Dll.SortedInsert(5)

	print("Value in sorted way in a sorted doubly linked list : ", end = '')
	Dll.printDLL()
