# Write a function that counts the number of times a given int occurs in a Linked List
# by using recursion
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None
		self.counter = 0

	def printLL(self):
		print("Given Linked List : ", end = "")
		temp = self.head
		while temp:
			print(temp.data, end = ' ')
			temp = temp.next
		print()

	def Add(self, new_data):
		if self.head is None:
			self.head = Node(new_data)
		else:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = Node(new_data)

	# by using linear search
	def countElement(self, li, key):
		if not li:
			return self.counter
		if li.data == key:
			self.counter = self.counter + 1

		return self.countElement(li.next, key)



if __name__ == '__main__':
	llist = LinkedList()
	llist.Add(1)
	llist.Add(2)
	llist.Add(1)
	llist.Add(9)
	llist.Add(1)

	llist.printLL()

	index = llist.countElement(llist.head, 1)

	print(f"{index} number of times a given int 1 occurs in a Linked List")
