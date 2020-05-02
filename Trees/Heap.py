
from Trees.BinaryTree import BinaryTree, Node

class Heap(BinaryTree):
	'''
	FIXME:
	Heap is currently not a subclass of BinaryTree.
	You should make the necessary changes in the class declaration line above 
	and in the constructor below.
	'''
		
	def __init__(self, xs=None):
		'''
		FIXME:
		If xs is a list (i.e. xs is not None),
		then each element of xs needs to be inserted into the Heap.
		'''
		super().__init__()

		if xs:
			self.insert_list(xs)

	def __repr__(self):
		'''
		Notice that in the BinaryTree class,
		we defined a __str__ function,
		but not a __repr__ function.
		Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
		Thus, if you create a variable using the command Heap([1,2,3])
		it's __repr__ will return "Heap([1,2,3])"

		For the Heap, type(self).__name__ will be the string "Heap",
		but for the AVLTree, this expression will be "AVLTree".
		Using this expression ensures that all subclasses of Heap will have a correct implementation of __repr__,
		and that they won't have to reimplement it.
		'''
		return type(self).__name__+'('+str(self.to_list('inorder'))+')'


	def is_heap_satisfied(self):
		'''
		Whenever you implement a data structure,
		the first thing to do is to implement a function that checks whether
		the structure obeys all of its laws.
		This makes it possible to automatically test whether insert/delete functions
		are actually working.
		'''
		if self.root:
			return Heap._is_heap_satisfied(self.root)
		return True

	@staticmethod
	def _is_heap_satisfied(node):
		'''
		FIXME:
		Implement this method.
		The lecture videos have the exact code you need,
		except that their method is an instance method when it should have been a static method.
		'''
		left = True
		right = True
		
		if node.left:
			if node.value > node.left.value:
				return False
			else:
				left = Heap._is_heap_satisfied(node.left)

		if node.right:
			if node.value > node.right.value:
				return False
			else:
				right = Heap._is_heap_satisfied(node.right)
		
		return left and right

	def insert(self, value):
		'''
		Inserts value into the heap.
		'''
		if self.root is None:
			self.root = Node(value)
			self.root.descendents = 1
		else:
			Heap._insert(self.root, value)

	@staticmethod
	def _insert(node, value):
		'''
		FIXME:
		Implement this function.
		'''
		if node == None:
			return None
		
		if node.left and node.right:
			node.left = Heap._insert(node.left,value)
			if node.value > node.left.value:
				return Heap._move_up(node,value)

		if node.left == None:
			node.left = Node(value)
			if node.value > node.left.value:
				return Heap._move_up(node, value)

		elif node.right == None:
			node.right = Node(value)
			if node.value > node.right.value:
				return Heap._move_up(node, value)

		return node

	@staticmethod
	def _move_up(node,value):
		if Heap._is_heap_satisfied(node) == True:
			return node
		if node.left and node.left.value > node.value:
			node.left = Heap._move_up(node.left,value)
		if node.right and node.right.value > node.value:
			node.right = Heap._move_up(node.right,value)
		if node.left:
			if node.left.value == value:
				new = node.left.value
				newl = node.value

				node.value = new
				node.left.value = newl

		if node.right:
			if node.right.value == value: 
				new = node.right.value
				newr = node.value

				node.value = new
				node.right.value = newr

		return node
	

	def insert_list(self, xs):
		'''
		Given a list xs, insert each element of xs into self.

		FIXME:
		Implement this function.
		'''
		
		for x in xs:
			self.insert(x)

	def find_smallest(self):
		'''
		Returns the smallest value in the tree.

		FIXME:
		Implement this function.
		This function is not implemented in the lecture notes,
		but if you understand the structure of a Heap it should be easy to implement.

		HINT:
		Create a recursive staticmethod helper function,
		similar to how the insert and find functions have recursive helpers.
		'''
		if self:
			return self.root.value


	def remove_min(self):
		'''
		Removes the minimum value from the Heap. 
		If the heap is empty, it does nothing.

		FIXME:
		Implement this function.
		'''
		
		if self.root == None:
			return None
		elif self.root.left == None and self.root.right == None:
			self.root = None
		else:
			new_right = Heap._find_right(self.root)
			self.root = Heap._remove(self.root)
			if new_right == self.root.value:
				return None
			else:
				self.root.value = new_right
			if Heap._is_heap_satisfied(self.root) == False:
				return Heap._move_down(self.root)

	@staticmethod
	def _remove(node):
		if node ==  None: 
			return None
		elif node.right:
			node.right = Heap._remove(node.right)
		elif node.left:
			node.left = Heap._remove(node.left)
		else: 
			if node.right is None and node.left is None: 
				return None
	
		return node

	@staticmethod
	def _find_right(node):
		if node.left == None and node.right == None:
			return node.value
		elif node.right:
			return Heap._find_right(node.right)
		elif node.left:
			return Heap._find_right(node.left)
	
	@staticmethod
	def _move_down(node):
		if node.left == None and node.right == None:
			return node

		if node.left and (node.right == None or node.left.value <= node.right.value):
			if node.left.value < node.value:
				new_p = node.left.value
				new_l = node.value

				node.value = new_p
				node.left.value = new_l

			node.left = Heap._move_down(node.left)

		elif node.right and (node.left == None or node.right.value <= node.left.value):
			if node.right.value < node.value:
				new_p = node.right.value
				new_r = node.value

				node.value = new_p
				node.right.value = new_r

			node.right = Heap._move_down(node.right)

		return node














