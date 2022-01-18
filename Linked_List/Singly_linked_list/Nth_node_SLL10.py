# Write a function to get Nth node from the end of a Linked List
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
		count = 0
		while temp:
			count += 1
			temp = temp.next

		if position > count:
			print("Location is greater than the length of LinkedList")
			return
		temp = self.head
		for i in range(0, count-position):
			temp = temp.next

		print(f"Element at index {position} from the end of a Linked List is :", temp.data)



if __name__ == '__main__':
	llist = LinkedList()
	llist.push(1)
	llist.push(2)
	llist.push(5)
	llist.push(9)
	llist.push(8)

	print("Given linked list : ", end='')
	llist.printlist()

	llist.searching(1)
	llist.searching(3)
	llist.searching(5)
