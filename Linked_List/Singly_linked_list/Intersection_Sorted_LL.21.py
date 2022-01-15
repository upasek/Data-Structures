# Intersection of two Sorted Linked Lists

class Node:
	def __init__(self):
		self.data = 0
		self.next = None

def printlist(node):
	while node:
		print(node.data, end = " ")
		node = node.next
	print()

def push(head_ref, new_data):

    ''' allocate node '''
    new_node = Node()

    ''' put in the data  '''
    new_node.data = new_data;

    ''' link the old list off the new node '''
    new_node.next = (head_ref);

    ''' move the head to point to the new node '''
    (head_ref) = new_node;
    return head_ref



def sortedIntersect(a, b):
    dummy = Node()
    tail = dummy
    dummy.next = None

    while a != None and b != None:
    	if a.data == b.data:
    		tail.next = push((tail.next), a.data)
    		tail = tail.next
    		a = a.next
    		b = b.next
    	elif a.data < b.data:
    		a = a.next
    	else:
    		b = b.next

    return (dummy.next)


if __name__ == '__main__':
	a = None
	b = None
	intersect = None

	a = push(a, 6)
	a = push(a, 5)
	a = push(a, 4)
	a = push(a, 3)
	a = push(a, 2)
	a = push(a, 1)

	b = push(b, 8)
	b = push(b, 6)
	b = push(b, 4)
	b = push(b, 2)

	print("First LinkedList : ", end="")
	printlist(a)

	print("Second LinkedList : ", end="")
	printlist(b)

	intersect = sortedIntersect(a, b)

	print("Linked list containing common items of a & b : ", end = '')
	printlist(intersect)
