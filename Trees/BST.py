'''
This file implements the Binary Search Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree file.
'''

from Trees.BinaryTree import BinaryTree, Node

class BST(BinaryTree):
	'''
	FIXME:
	BST is currently not a subclass of BinaryTree.
	You should make the necessary changes in the class declaration line above 
	and in the constructor below.
	'''

	def __init__(self, xs=None):
		'''
		FIXME:
		If xs is a list (i.e. xs is not None),
		then each element of xs needs to be inserted into the BST.
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
		Thus, if you create a variable using the command BST([1,2,3])
		it's __repr__ will return "BST([1,2,3])"

		For the BST, type(self).__name__ will be the string "BST",
		but for the AVLTree, this expression will be "AVLTree".
		Using this expression ensures that all subclasses of BST will have a correct implementation of __repr__,
		and that they won't have to reimplement it.
		'''
		return type(self).__name__+'('+str(self.to_list('inorder'))+')'


	def is_bst_satisfied(self):
		'''
		Whenever you implement a data structure,
		the first thing to do is to implement a function that checks whether
		the structure obeys all of its laws.
		This makes it possible to automatically test whether insert/delete functions
		are actually working.
		'''
		if self.root:
			return BST._is_bst_satisfied(self.root)
		return True

	@staticmethod
	def _is_bst_satisfied(node):
		'''
		FIXME:
		Implement this method.
		The lecture videos have the exact code you need,
		except that their method is an instance method when it should have been a static method.
		'''

		is_left = True
		is_right = True

		if node.left:
			if node.value > node.left.value:
				is_left =  BST._is_bst_satisfied(node.left)
			else:
				return False
		if node.right:
			if node.value < node.right.value:
				is_right =  BST._is_bst_satisfied(node.right)
			else:
				return False

		return is_right and is_right

	def insert(self, value):
		'''
		Inserts value into the BST.
		'''
		if self.root is None:
			self.root = Node(value)
		else:
			BST._insert(self.root, value)


	@staticmethod
	def _insert(node, value):
		'''
		FIXME:
		Implement this function.
		The lecture videos have the exact code you need,
		except that their method is an instance method when it should have been a static method.
		'''

		if value < node.value:
			if node.left is None:
				node.left = Node(value)
			else:
				BST._insert(node.left, value)
		elif value > node.value:
			if node.right is None:
				node.right = Node(value)
			else:
				BST._insert(node.right, value)
		else:
			print('Value is already present in tree.')
				

	def insert_list(self, xs):
		'''
		Given a list xs, insert each element of xs into self.

		FIXME:
		Implement this function.
		'''

		for x in xs:
			self.insert(x)

	def __contains__(self, value):
		return self.find(value)


	def find(self, value):
		'''
		Returns whether value is contained in the BST.
		'''
		if self.root:
			if BST._find(self.root, value):
				return True
		else:
			return False


	@staticmethod
	def _find(node, value):
		'''
		FIXME:
		Implement this function.
		The lecture videos have the exact code you need,
		except that their method is an instance method when it should have been a static method.
		'''

		if value > node.value and node.right:
			return BST._find(node.right,  value)
		elif value < node.value and node.left:
			return BST._find(node.left, value)
		if value == node.value:
			return True
		else:
			return False

	def find_smallest(self):
		'''
		Returns the smallest value in the tree.

		FIXME:
		Implement this function.
		This function is not implemented in the lecture notes,
		but if you understand the structure of a BST it should be easy to implement.

		HINT:
		Create a recursive staticmethod helper function,
		similar to how the insert and find functions have recursive helpers.
		'''

		if self.root.left is None:
			return self.root.value
		elif self.root:
			return BST._find_smallest(self.root)

	@staticmethod
	def _find_smallest(node):
		
		assert node is not None
		if node.left is None:
			return node.value
		else:
			return BST._find_smallest(node.left)


	def find_largest(self):
		'''
		Returns the largest value in the tree.

		FIXME:
		Implement this function.
		This function is not implemented in the lecture notes,
		but if you understand the structure of a BST it should be easy to implement.
		'''

		if self.root.right is None:
			return self.root.value
		else:
			return BST._find_largest(self.root)
	
	@staticmethod
	def _find_largest(node):
		
		if node.right is None:
			return node.value
		else:
			return BST._find_largest(node.right)
		

	def remove(self,value):
		'''
		Removes value from the BST. 
		If value is not in the BST, it does nothing.

		FIXME:
		implement this function.
		There is no code given in any of the lecture videos on how to implement this function,
		but the video by HMC prof Colleen Lewis explains the algorithm.

		HINT:
		You must have find_smallest/find_largest working correctly 
		before you can implement this function.

		HINT:
		Use a recursive helper function.
		'''

		self.root = BST._remove(self.root,value)
		'''		
		if self.root:
			if self.root.value == value:
				#Case #3 where there are two branches
				if self.root.left and self.root.right:
					store_rootval = BST._find_smallest(self.root)
					BST._remove(self.root, store_rootval)
					self.root.value = store_rootval
				#Case #2 where only one branch
				elif self.root.left or self.root.right:
					if self.root.left:
						self.root.value = self.root.left.value
						self.root.left = None
					if self.root.right:
						self.root.value = self.root.right.value
						self.root.right = None
					#Case #1 where it is a leaf
				else:
					self.root = None
			else:
				BST._remove(self.root,value)
		'''

	@staticmethod
	def _remove(node, value):
		if node == None:
			return None
		if value < node.value:
			node.left = BST._remove(node.left, value)
		elif value > node.value:
			node.right = BST._remove(node.right, value)
		else:
			if node.left is None and node.right is None:
				return None
			if node.right and node.left is None:
				store = node.right
				return store
			if node.left and node.right is None:
				store = node.left
				return store

			most_left = BST._find_smallest(node.right)

			node.value = most_left

			node.right = BST._remove(node.right, node.value)

		return node
		

		'''
		if node.left:
			if node.left.value == value:
				#Case 3: The node with value has a left and right branch
				if node.left.left and node.left.right:
					node.left.value = BST._find_largest(node.left.left)
					BST._remove(node.left,node.left.value)
				#Case 2: The node with value has either a left or right branch, don't need the nested if but for organization sake
				if node.left.left or node.left.right:
					if node.left.left:
						node.left = node.left.left
					else:
						node.left = node.left.right
				#Case 1: The node with value is a leaf
					node.left = None
		
		if node.right:
			if node.right.value == value:
				#Case 3: The node with value has a left and right branch
				if node.right.left and node.right.right:
					node.right.value = BST._find_smallest(node.right.right)
					BST._remove(node.right, node.right.value)
				#Case 2: The node with value has either a left or right branch, don't need the nested if but for organization sake
				if node.right.left or node.right.right:
					if node.right.left:
						node.right = node.right.left
					if node.right.right:
						node.right = node.right.right
				#Case 1: The node with value is a leaf
				node.right = None
		
		if node.right:
			if node.right.value > value:
				BST._remove(node.left, value)
		if node.left:
			BST._remove(node.right, value)
		
		return ('Whoops infitie')

		'''

	def remove_list(self, xs):
		'''
		Given a list xs, remove each element of xs from self.

		FIXME:
		Implement this function.
		'''
		if xs:
			for x in xs:
				self.remove(x)


