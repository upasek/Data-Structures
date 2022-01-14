# Detect loop in a linked list
# Time complexity: O(n).
# Only one traversal of the loop is needed.
# Auxiliary Space: O(n).
# n is the space required to store the value in hashmap.
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

	def DetectLoop(self):
		s = set()
		temp = self.head

		while temp:
			if temp in s:
				return True

			s.add(temp)
			temp = temp.next

		return False



if __name__ == '__main__':
	llist = LinkedList()
	llist.push(1)
	llist.push(2)
	llist.push(5)
	llist.push(9)
	llist.push(8)

	llist.head.next.next.next.next.next = llist.head
	# print(llist.head.next.next.next.next.next.data)
	# print("Given linked list : ", end='')
	# llist.printlist()

	if (llist.DetectLoop()):
		print("Loop found")
	else:
		print("No Loop")
