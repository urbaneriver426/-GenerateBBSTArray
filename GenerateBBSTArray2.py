class BSTNode:
	
	def __init__(self, key, parent):
		self.NodeKey = key
		self.Parent = parent 
		self.LeftChild = None
		self.RightChild = None
		self.Level = 0
		
class BalancedBST:
		
	def __init__(self):
		self.Root = None

	def GenerateTree(self, a, node = None):
		if a:
			a.sort()
			if node is None:
				self.Root = BSTNode(a[len(a)//2], None)
				self.Root.Level = 1
				node = self.Root
				node.LeftChild = self.GenerateTree(a[:len(a)//2], node)
				node.RightChild = self.GenerateTree(a[(len(a)//2)+1:], node)
			else:
				new_node = BSTNode(a[len(a)//2], node)
				new_node.Level = node.Level + 1
				node = new_node
				node.LeftChild = self.GenerateTree(a[:len(a)//2], node)
				node.RightChild = self.GenerateTree(a[(len(a)//2)+1:], node)
				return node   

	def NodeCompare(self, node):
		if node is False:
			return False
		if node:
			if node.LeftChild:
				left_depth = self.NodeCompare(node.LeftChild)
			else:
				left_depth = None
			if node.RightChild:
				right_depth = self.NodeCompare(node.RightChild)
			else:
				right_depth = None
			#1.1. Case
			if left_depth is None and right_depth is None:
				return node.Level
			#1.2. Case
			if left_depth is None:
				return right_depth
			if right_depth is None:
				return left_depth
			#2. Case
			if left_depth == right_depth:
				return left_depth
			else:
				#3.1. Case
				if left_depth - right_depth == 1:
					return left_depth
				if right_depth - left_depth == 1:
					return right_depth
				#3.2. Case
				else:
					return False 

	def IsBalanced(self, root_node):
		if root_node:
			if root_node.LeftChild:
				left_depth = self.NodeCompare(root_node.LeftChild)
			else:
				left_depth = None
			if root_node.RightChild:
				right_depth = self.NodeCompare(root_node.RightChild)
			else:
				right_depth = None
			if left_depth and right_depth:
				if left_depth == right_depth:
						return True
				if left_depth > right_depth:
					if left_depth - right_depth <= 1:
						return True
					else:
						return False
				else:
					if  right_depth - left_depth <= 1:
						return True
					else:
						return False
			else:
				if left_depth:
					if left_depth - root_node.Level <= 1:
						return True
					else:
						return False 
				if right_depth:
					if right_depth - root_node.Level <= 1:
						return True
					else:
						return False
				else:
					return True
		else:
			return None
		return False
