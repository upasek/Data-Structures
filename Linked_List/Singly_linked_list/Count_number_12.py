# Write a function that counts the number of times a given int occurs in a Linked List
# Time Complexity: O(n)
# Auxiliary Space: O(1)
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None

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
	def countElement(self, key):
		total = 0
		temp = self.head
		while temp:
			if temp.data == key:
				total += 1
			temp = temp.next
		return total



if __name__ == '__main__':
	llist = LinkedList()
	llist.Add(1)
	llist.Add(2)
	llist.Add(1)
	llist.Add(9)
	llist.Add(1)

	llist.printLL()

	index = llist.countElement(1)

	print(f"{index} number of times a given int 1 occurs in a Linked List")
