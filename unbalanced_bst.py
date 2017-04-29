class Node(object):
    """
    Binary tree node - Handles recursive binary search tree logic
    """
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
    def insert(self, data):
        """
        Populates the appropriate tree node in the binary tree
        """
        if self.value > data:
            if self.left is not None:
                return self.left.insert(data)
            self.left = Node(data)
            return True
        elif self.value < data:
            if self.right is not None:
                return self.right.insert(data)
            self.right = Node(data)
            return True
        # No dupes
        return False
    
    def find(self, data):
        """
        Locates the appropriate tree node in the binary tree
        """
        if self.value > data:
            if self.left is not None:
                return self.left.find(data)
            return False
        elif self.value < data:
            if self.right is not None:
                return self.right.find(data)
            return False
        # Found it
        return True
    
    def preorder(self):
        """
        Recursively traverses the binary tree starting at the root
        """
        print str(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def postorder(self):
        """
        Recursively traverses the binary tree starting at the far left
        leaf node and eventually ending at the root
        """
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print str(self.value)
    
    def inorder(self):
        """
        Recursively traverses the binary tree in order from the far left leaf
        node to the far right leaf node
        """
        if self.left:
            self.left.inorder()
        print str(self.value)
        if self.right:
            self.right.inorder()
   
    def get_branches(self, node):
        """
        Split up all branch paths in a tree via pre-order traversal
        """
        if node.left is None and node.right is None:
            return [node.value]

        branches = []
        for branch in self.get_branches(node.left) + self.get_branches(node.right):
            if not isinstance(branch, list):
                branch = [branch]
            branches.append([node.value] + branch) 

        return branches 

class Tree(object):
    """
    Binary tree - acts as an interface to the tree node recursion logic
    """
    def __init__(self):
        self.root = None
    
    def insert(self, *data):
        """
        Inserts data into the tree
        """
        for element in data:
            self._insert(element)
            
    def _insert(self, data):
        if self.root is not None:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    
    def find(self, data):
        """
        Returns True if the value is found, False otherwise
        """
        if self.root is not None:
            return self.root.find(data)
        return False
    
    def preorder(self):
        """
        Performs a pre-order traversal of the tree.  Use this
        when traversal starting at the root is beneficial.
        """
        if self.root is not None:
            print 'PreOrder'
            self.root.preorder()
        else:
            print 'Empty Tree'
            
    def postorder(self):
        """
        Performs a post-order traversal of the tree.  Use this
        when traversing the leaves of the tree ending at the
        root is beneficial.
        """
        if self.root is not None:
            print 'PostOrder'
            self.root.postorder()
        else:
            print 'Empty Tree'
            
    def inorder(self):
        """
        Performs an in order traversal of the tree.  Use this
        when a sorted list is desired.
        """
        if self.root is not None:
            print 'InOrder'
            self.root.inorder()
        else:
            print 'Empty Tree'
   
    def get_branches(self):
        """
        Performs a pre-order traversal and returns a list of all
        branches in the tree starting at the root.
        """
        if self.root is not None:
            return self.root.get_branches(self.root)
