# Segregate even and odd nodes in a Linked List

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

	def length(self):
		temp = self.head
		count = 0
		while temp:
			count += 1
			temp = temp.next

		return count

	def Segregate(self, count):
		end = self.head
		while end.next:
			end = end.next

		end.next = None
		temp = self.head
		prev = self.head
		while count > 0:
			# print(temp.data)
			if (temp.data % 2) != 0:
				# print("*")
				end.next = temp
				print("->", end.data, end.next.data)
				prev = temp.next
				temp.next = None
				end = temp
				prev.next = temp
				count -= 1
				# temp = temp.next
			elif (temp.data % 2) == 0:
				# print("#")
				count -= 1
				prev = temp.next
				temp = temp.next
			# temp = temp.next



if __name__ == '__main__':
	llist = LinkedList()
	llist.push(6)
	llist.push(7)
	llist.push(1)
	llist.push(4)
	llist.push(5)
	llist.push(10)
	llist.push(12)
	llist.push(8)
	llist.push(15)
	llist.push(17)

	print("Given linked list : ", end="")
	llist.printlist()

	count = llist.length()

	llist.Segregate(count)

	print("New linked list : ", end="")
	llist.printlist()
