# Function to check if a singly linked list is palindrome
# The time complexity of the above method is O(n).
# space : O(n)
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

	def palindrome(self):
		ispalin = True
		temp = self.head
		stack = []

		while temp:
			stack.append(temp.data)
			temp = temp.next

		temp = self.head
		while temp:
			i = stack.pop()
			if temp.data == i:
				ispalin = True
			else:
				ispalin = False
				break

			temp = temp.next
		return ispalin



if __name__ == '__main__':
	llist = LinkedList()
	llist.Add(1)
	llist.Add(2)
	llist.Add(1)
	llist.Add(2)
	llist.Add(1)

	llist.printLL()

	result = llist.palindrome()
	print("isPalindrome :", result)
