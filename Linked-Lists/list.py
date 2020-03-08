# Class for nodes

class Node:
	def __init__(self, data):
		self.data  = data
		self.next = None

class LinkedList:
	# initialise empty list
	def __init__(self):
		self.head = None

	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			# iterate through nodes
			cur_node = cur_node.next


	def append(self, data):
		new_node = Node(data)
		# if first node is not present, insert here
		if self.head is None:
			self.head = new_node
			return
		
		# set variable last node as the current node
		last_node = self.head

		# while node is not null, increment 'last node' to be the next node by setting it to the pointer
		while last_node.next:
			last_node = last_node.next
		# set next node on final head to be the new node
		last_node.next = new_node
		
	def prepend(self, data):
		new_node = Node(data)
		# set the new nodes next to the be the first node in the list
		new_node.next = self.head
		# set the first node to the new node 
		self.head = new_node

	def insert_between(self, prev_node, data):
		if not prev_node:
			print("Non existing node")
			return

		new_node = Node(data)

		new_node.next = prev_node.next
		prev_node.next = new_node


	def delete_node(self, key):
		cur_node = self.head

		if cur_node and cur_node.data == key:
			self.head = cur_node.next
			cur_node = None
			return

		prev = None
		while cur_node and cur_node.data != key:
			prev = cur_node
			cur_node = cur_node.next

		if cur_node is None:
			return 

		prev.next = cur_node.next
		cur_node = None

	def delete_node_at_position(self, pos):
		cur_node = self.head

		if pos == 0:
			self.head = cur_node.next
			cur_node = None
			return

		prev = None
		count = 0
		# loop through nodes untill find key node	
		while cur_node and count != pos:
			prev = cur_node
			cur_node = cur_node.next
			count += 1

		if cur_node is None:
			return

		prev.next = cur_node.next
		cur_node = None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.prepend('0')

# to retrieve nodes
print(llist.head.data)
print(llist.head.next.data)

llist.insert_between(llist.head.next, "G")
llist.delete_node("B")
llist.delete_node_at_position(2)
llist.print_list()