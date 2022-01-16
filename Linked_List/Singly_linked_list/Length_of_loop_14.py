# Find length of loop in linked list

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None


	def Add(self, new_data):
		if self.head is None:
			self.head = Node(new_data)
		else:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = Node(new_data)

	def createloop(self, n):
		LoopNode = self.head
		for i in range(n-1):
			LoopNode = LoopNode.next

		end = self.head
		while end.next:
			end = end.next

		end.next = LoopNode

	def LengthLoop(self):
		slow = self.head
		fast = self.head
		flag = 0
		while slow and slow.next and fast and fast.next and fast.next.next:
			if slow == fast and flag != 0:

				count = 1
				slow = slow.next
				while slow != fast:
					slow = slow.next
					count += 1
				return count

			slow = slow.next
			fast = fast.next.next
			flag = 1

		return 0 # no loop



if __name__ == '__main__':
	llist = LinkedList()
	llist.Add(1)
	llist.Add(2)
	llist.Add(5)
	llist.Add(9)
	llist.Add(8)

	llist.createloop(2)

	index = llist.LengthLoop()
	print("Length of loop in linked list : ", index)
