# Swap nodes in a linked list without swapping data
# O(n)

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

	def swapnode(self, key1, key2):
		if key1 == key2:
			return

		prevX = prevY = None
		curX = curY = self.head
		temp = self.head

		while temp and temp.next:
			if temp.next.data == key1:
				# print(temp.next.data)
				prevX = temp
				curX = temp.next
			if temp.next.data == key2:
				prevY = temp
				curY = temp.next
			temp = temp.next

		if curX == None or curY == None:
			return

		if prevX is not None:
			prevX.next = curY
		else:
			self.head = curY

		if prevY is not None:
			prevY.next = curX
		else:
			self.head = curX

		curX.next, curY.next = curY.next, curX.next


		# print(self.head.data, self.head.next.data, self.head.next.next.data)


if __name__ == '__main__':
	llist = LinkedList()
	llist.push(14)
	llist.push(20)
	llist.push(13)
	llist.push(12)
	llist.push(15)
	llist.push(10)


	print("Given linked list : ", end='')
	llist.printlist()

	llist.swapnode(14, 10)

	print("New linked list : ", end='')
	llist.printlist()

