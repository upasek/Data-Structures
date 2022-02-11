class Node:

	def __init__(self, data):
		self.next = None
		self.prev = None
		self.data = data


def push(head_ref, new_data):
	new_node = Node(new_data)

	new_node.data = new_data

	new_node.next = head_ref

	new_node.prev = None

	if head_ref != None:
		head_ref.prev = new_node

	head_ref = new_node

	return head_ref


def printll(node):
	last = None
	print("Traversal in forward direction : ", end = "")
	while (node):
		print(node.data, end  = ' ')
		last = node
		node = node.next
	print()

	print("Traversal in reverses direction : ", end = "")
	while last != None:
		print(last.data, end = ' ')
		last = last.prev
	print()



if __name__ == '__main__':
	head = None
	head = push(head, 1)
	head = push(head, 3)
	head = push(head, 4)

	printll(head)
